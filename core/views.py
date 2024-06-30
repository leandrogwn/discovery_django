from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Ola {} de {} anos</h1>'.format(nome, idade))

def soma(request, n1, n2):
    res = n1+n2
    return HttpResponse('A soma do número {} com o número {} é igual a {}'.format(n1, n2, res))

def multiplicar(request, n1, n2):
    res = n1*n2
    return HttpResponse('A multiplicação do número {} com o número {} é igual a {}'.format(n1, n2, res))

def dividir(request, n1, n2):
    res = n1/n2
    return HttpResponse('A divisão do número {} com o número {} é igual a {}'.format(n1, n2, res))

def subtrair(request, n1, n2):
    res = n1-n2
    return HttpResponse('A subtração do número {} com o número {} é igual a {}'.format(n1, n2, res))