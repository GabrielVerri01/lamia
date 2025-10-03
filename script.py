#CONVERTENDO GRAUS
# celsius = float(input('digite quantos graus celsius esta:'))
#
# fahrenheit = celsius * 9/5 + 32
# print(f' convertendo para fahrenheit o valor de {celsius}° celsius fica {fahrenheit }')


#TABUADA
# numero = int(input(' diga qual numero voce deseja saber a tabuada: '))
# for i in range(1, 11):
#     valor = numero * i
#     print(f'{i} * {numero} = {valor}')


#CONTADOR 1 A 100
# for i in range(1,101):
#     print(i)
#     i +=1


#PALINDROMO
# palavra = input("diga um palavra: ")
# palavra_invertida = palavra[::-1]
#
# if palavra == palavra_invertida:
#     print('essa palavra é um palíndromo!')
# else:
#     print('essa palavra não é um palíndromo!')


#SOMAR NUMEROS DA LISTA
# nums = [2,4,6,8,10]
# soma = nums[0] + nums[1] + nums[2] + nums[3] + nums[4]
# print(f' a soma dos numeros da lista é {soma}')


#MAIOR E MENOR NUMERO DA LISTA
# numeros = [5, 12, 3, 9, 21, 4]
#
# maior = numeros[0]
# menor = numeros[0]
#
# for numero in numeros:
#     if numero > maior:
#         maior = numero
#     if numero < menor:
#         menor = numero
#
# print(f"Maior número: {maior}")
# print(f"Menor número: {menor}")


#CALCULADORA
# operacao = input("me passe a operacao que deseja operar: ")
# n1 = float(input('me diga o primeiro numero:'))
# n2 = float(input('me diga o segundo numero:'))
#
# if operacao == 'adicao':
#     print(n1 + n2)
# elif operacao == 'subtracao':
#     print(n1 - n2)
# elif operacao == 'multiplicacao':
#     print(n1 * n2)
# elif operacao == 'divisao':
#     print(n1 / n2)
# else:
#     print(' nao encontramos essa operacao!')


#CONTAR VOGAIS
# frase = input('digite uma palavra ou frase qualquer: ')
#
# vogais = 'aeiouAEIOU'
# contador = 0
#
# for letra in frase:
#     if letra in vogais:
#         contador+=1
#
#
# print(f'a palavra ou frase acima tem {contador} vogais')


#ADIVINHACAO DE NUMERO
# import random
# numero_secreto = random.randint(1,100)
#
# tentativas = 0
# acertou = False
# print('bem vindo ao jogo. aqui voce devera tentar adivinhart qual numero estou pensando.')
#
# while not acertou:
#     try:
#         chute = int(input('Pode comecar, qual o seu palpite?'))
#         tentativas+=1
#
#         if chute < 1 or chute >100:
#             print('digite um numero valido, entre 1 e 100:')
#         elif chute < numero_secreto:
#             print('chute muito baixo, tente um mais alto!')
#         elif chute > numero_secreto:
#             print('numero muito alto, tente um numero mais baixo!')
#         else:
#             print(f'voce acertou o numero secreto em {tentativas} tentativas, era {numero_secreto}')
#             acertou = True
#
#     except ValueError:
#         print('digite um valor valido')


#NOME INVERSO
# nome = input('diga o seu nome:')
# invertida = nome[::-1]
# print(invertida)


#GERADOR DE SENHA
# import random
# n1 = str(random.randint(1,9))
# n2 = str(random.randint(1,9))
# n3 = str(random.randint(1,9))
# n4 = str(random.randint(1,9))
#
# senha = (n1 + n2 + n3 + n4)
# print(senha)

#3.1
# a = int(input("Digite o primeiro número: "))
# b = int(input("Digite o segundo número: "))
# # Complete abaixo
# soma = a + b
# print("A soma é:", str(soma) )

#3.2
# numero = int(input('digite qualquer numero: '))
# if numero > 0:
#     print('o seu numero é positivo')
# elif numero < 0:
#     print('seu numero é negativo')
# elif numero == 0:
#     print('seu numero é igual a zero')
# else:
#     print('sla que porra é seu numero')





from flask import Flask, render_template, redirect, url_for, flash, request

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

# @app.route('/login')
# def login():
#     return render_template('login.html')

@app.route('/logado')
def logado():
    return render_template('logado.html')

email_correto = "gabrielverri0108@gmail.com"
senha_correta = "gvpn0108"
@app.route('/login', methods=['GET','POST'])
def login():
    mensagem = ''

    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        if email == email_correto and senha == senha_correta:
            # mensagem = 'Login bem-sucedido'
            return redirect(url_for('logado'))
        else:
            mensagem = 'Login ou senha incorretos'

    return render_template('login.html', mensagem = mensagem)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/encomendas')
def encomendas():
    return render_template('encomendas.html')

if __name__ == '__main__':
    app.run(debug=True)

