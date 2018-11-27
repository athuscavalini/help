# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Aluno
from cursos.models import Turma, Curso, HorasFaltadas, Matricula
from .forms import PostForm
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import random

##################### View de pesquisa de alunos #####################
# View que renderiza a lista de alunos dado uma pesquisa por nome, cpf ou numero de matricula
@login_required
def pesquisa(request): 
    alunos = Aluno.objects.order_by('nome')
    context = {}
    query = request.GET.get("pesquisa")
    context['query'] = query
    if query:
        alunos = (alunos.filter(nome__icontains=query)) or (alunos.filter(cpf__icontains=query)) or (alunos.filter(numero_matricula__icontains=query))
        context['alunos'] = alunos
    return render(request, 'pesquisa.html', context)

##################### View de lista de alunos #####################
# View que retorna uma lista de alunos ordenados por ordem alfabetica
@login_required
def lista(request):
    alunos = Aluno.objects.order_by('nome')
    return render(request, 'lista.html', {'alunos':alunos})

############## View para criar pauta ##############
# View utilizada para criar uma relação de um aluno com as horas
# faltadas pelo mesmo em uma turma
def cria_matricula(aluno):
    matricula = Matricula()
    matricula.aluno = aluno
    matricula.horas_faltadas = 0
    matricula.situacao = "M"
    matricula.save()
    return matricula

def cria_espera(aluno):
    matricula = Matricula()
    matricula.aluno = aluno
    matricula.horas_faltadas = 0
    matricula.situacao = "E"
    matricula.save()
    return matricula

def aluno_ta_inscrito(turma, aluno):
    for a in turma:
        if a.aluno.numero_matricula == aluno.numero_matricula:
            return True
    return False

def busca_matricula(turma, aluno):
    for matricula in turma:
        if matricula.aluno.numero_matricula == aluno.numero_matricula:
            return matricula
    return None

##################### View para matricula de um aluno numa turma #####################
# View que matricula um aluno numa turma ou insere o aluno numa lista de espera
def matricula_aluno(request, query, aluno):
    for t in query:
        turma = Turma.objects.get(codigo=t)
        if(aluno_ta_inscrito(turma.alunos_inscritos.all(),aluno) == True):
            messages.warning(request, aluno.nome +' já está inscrito na turma ' + turma.curso.nome + '-' + turma.codigo, extra_tags='alert')
        elif((aluno_ta_inscrito(turma.alunos_espera.all(),aluno) == True) and turma.alunos_inscritos.count() < turma.vagas_presencial):
            matricula = busca_matricula(turma.alunos_espera.all(), aluno)
            matricula.situacao = "M"
            matricula.save()
            turma.alunos_espera.remove(matricula)
            turma.alunos_inscritos.add(matricula)
            messages.success(request,  aluno.nome +' foi movido(a) da lista de espera para a turma ' + turma.curso.nome + '-' + turma.codigo)
        elif(turma.alunos_inscritos.count() < turma.vagas_presencial):
            matricula = Matricula()
            matricula.aluno = aluno
            matricula.horas_faltadas = 0
            matricula.situacao = "M"
            matricula.save()
            turma.alunos_inscritos.add(matricula)
            messages.success(request,  aluno.nome +' foi inscrito(a) na turma ' + turma.curso.nome + '-' + turma.codigo)
        else:
            if(aluno_ta_inscrito(turma.alunos_espera.all(),aluno) == True):
                messages.info(request, 'O aluno(a) ' + aluno.nome + ' já está inscrito(a) na lista de espera da turma ' + turma.curso.nome + '-' + turma.codigo)    
            elif (turma.alunos_espera.count() < turma.vagas_lista_espera):
                matricula = Matricula()
                matricula.aluno = aluno
                matricula.horas_faltadas = 0
                matricula.situacao = "E"
                matricula.save()
                turma.alunos_espera.add(matricula)
                messages.info(request, 'Turma cheia, ' + aluno.nome + ' foi inscrito(a) na lista de espera da turma ' + turma.curso.nome + '-' + turma.codigo)
            else:
                messages.warning(request, 'Turma, e lista de espera cheias, ' + aluno.nome + ' nao foi inscrito(a) na turma ' + turma.curso.nome + '-' + turma.codigo)


def esta_matriculado(aluno, turmas):
    for turma in turmas:
        for m in turma.alunos_inscritos.all():
            if m.aluno == aluno:
                return True
    return False

##################### View de detalhamento de um aluno #####################
# View que renderiza um aluno de acordo com a "pk"
# View que permite inserir um aluno numa turma ou lista de espera
@login_required
def detalhes(request, pk):
    context = {}
    aluno = get_object_or_404(Aluno, pk=pk)
    turmas = Turma.objects.all()
    context['aluno'] = aluno
    context['turmas'] = turmas
    matriculado = esta_matriculado(aluno,turmas)
    context['matriculado'] = matriculado
    query = request.GET.getlist("turma")
    try:
        if query: # Se query for verdadeiro o aluno será inserido em uma ou mais turmas
            matricula_aluno(request, query, aluno)
    except Turma.DoesNotExist:
        turma = None
    return render(request, 'detalhes.html', context)

##################### View auxiliar pra criar matricula #####################
# View que cria um numero de matricula concatenando a data do cadastro com 
# mais 4 digitos aleatorios
def cria_matricula():
    data_hoje = datetime.now().strftime("%Y%m%d")
    while len(data_hoje)<11:
        n = random.randint(0,9)
        data_hoje+= `n`
    numero_matricula = int(data_hoje)
    return numero_matricula

##################### View novo aluno #####################
# View utilizada para cadastrar um novo aluno no banco de dados
@login_required
def novo(request): 
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            now = datetime.now();
            post = form.save(commit=False)
            post.data_entrada = timezone.now()
            post.save()
            while True: # while pra criar uma matricula unica para o aluno
                num_matricula = cria_matricula() 
                if not Aluno.objects.filter(numero_matricula=num_matricula).exists():
                    break
            post.numero_matricula = num_matricula
            post.save()
            return redirect('aluno:detalhes', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'novo_editar.html', {'form': form})

##################### View de edicao de um aluno #####################
# View que recupera um aluno do banco de dados acordo com a "pk" e
# renderiza para edicao
@login_required
def editar(request, pk): # Funcao para editar um aluno
    post = get_object_or_404(Aluno, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('aluno:detalhes', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'novo_editar.html', {'form': form, 'post': post})

##################### View de remocao de um aluno #####################
# View que remove um aluno de acordo com a "pk"
@login_required
def remover(request, pk): # Funcao para remover um aluno
    context = {}
    aluno = get_object_or_404(Aluno, pk=pk)
    nome = aluno.nome
    context['nome']= nome
    aluno.delete()
    return render(request,'confirmacao.html', context)