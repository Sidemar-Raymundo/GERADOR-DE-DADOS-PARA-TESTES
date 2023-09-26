import random
import os

print('Bem vindo ao gerador de dados de testes, para finalizar o programa digite "parar".')

nomes = ["Ana", "João", "Maria", "Carlos", "Sofia"]
emails = ["ana@email.com", "joao@email.com",
          "maria@email.com", "carlos@email.com", "sofia@email.com"]

telefones = ["(123) 456-7890", "(987) 654-3210",
             "(555) 123-4567", "(777) 888-9999", "(888) 777-9999"]

cidades = ["Nova York", "Los Angeles", "Chicago", "Miami", "Dallas"]

estados = ["Califórnia", "Texas", "Nova York", "Flórida", "Illinois"]

while True:
    print('Escolha um ou mais números abaixo para serem gerados aleatoriamente')

    print("[1] nomes")
    print("[2] e-mails")
    print("[3] telefones")
    print("[4] cidades")
    print("[5] estados")

    escolha = input('Digite uma ou mais opções acima. ')

    if 'parar' in escolha:
        break

    dados_gerados = []

    opção_invalida = False

    for opcao in escolha:
        if opcao.isdigit() and 1 <= int(opcao) <= 5:
            opcao = int(opcao)
            opção_invalida = True
        else:
            print("Opção inválida. Digite uma opção válida (1 a 5).")
            break  # Retornar ao início do loop em caso de entrada inválida

        if opcao == 1: 
            dado = random.choice(nomes)
        elif opcao == 2:
            dado = random.choice(emails)
        elif opcao == 3:
            dado = random.choice(telefones)
        elif opcao == 4:
            dado = random.choice(cidades)
        elif opcao == 5:
            dado = random.choice(estados)

        dados_gerados.append(dado)
        print(dado)
        if opção_invalida == True:
            arquivo = input('Gostaria de transformar esses dados em arquivos? s/n ')

        if arquivo.lower() == 's':
            with open('dados.txt', 'a', newline='') as arquivo_saida:
            # 1 MINHA FORMA ORIGINAL CRIADA: ⬇️
                arquivo_saida.write("\n".join(dados_gerados) + "\n")
            #  2 FUNCIONA ASSIM TAMBEM  ⬇️
            #  for dado in dados_gerados:
            #     arquivo_saida.write(dado + "\n")


            #  3 FUNCIONA ASSIM TAMBEM ⬇️
            #  for dado in dados_gerados:
            #     arquivo_saida.write(dado + os.linesep)
                 


                