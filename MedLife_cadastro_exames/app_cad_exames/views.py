from django.shortcuts import render, redirect
from .models import Usuario, Exame

def cadastrar_exame(request):
    if request.method == 'POST':
        nome_exame = request.POST.get('nome_exame')
        data_exame = request.POST.get('data_exame')
        email = request.POST.get('email')

        # Verificar se o usuário com o e-mail fornecido existe
        usuario = Usuario.objects.filter(email=email).first()


        if usuario:
            # Associar o exame ao usuário existente
            novo_exame = Exame(nome_exame=nome_exame, data_exame=data_exame, email=email, usuario=usuario)
            novo_exame.save()
            return redirect('ver_exames')
        else:
            # Lidar com o caso em que o usuário não existe
            # Você pode mostrar uma mensagem de erro ou criar um novo usuário, dependendo da sua lógica de negócios
            return render(request, 'usuarios/home.html')
    else:
        return render(request, 'usuarios/cadastrar_exame.html')

# Create your views here.
def home(request):
    return render(request, 'usuarios/home.html')

def ver_exames(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        # Verificar se o usuário com o e-mail fornecido existe
        usuario = Usuario.objects.filter(email=email).first()

        if usuario:
            # Se o usuário existir, filtrar os exames associados a ele
            exames = Exame.objects.filter(usuario=usuario)
            return render(request, 'usuarios/ver_exames.html', {'exames': exames, 'usuario': usuario})

        else:
            # Caso o usuário não exista
            return render(request, 'usuarios/ver_exames.html', {'error_message': 'Usuário não encontrado'})

    else:
        return render(request, 'usuarios/ver_exames.html')

def cadastrar_me(request):
    if request.method == 'POST':
        novo_usuario = Usuario()
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.email = request.POST.get('email')
        novo_usuario.senha = request.POST.get('senha')
        novo_usuario.save()
        return render(request, 'usuarios/home.html')
        

    return render(request, 'usuarios/cadastrar_me.html')

def exames(request):
    if request.method == 'POST':
        novo_exame = Exame()
        novo_exame.nome_exame = request.POST.get('nome_exame')
        novo_exame.data_exame = request.POST.get('data_exame')
        novo_exame.save()

    return render(request, 'usuarios/ver_exames.html', {'exames': Exame.objects.all()})
