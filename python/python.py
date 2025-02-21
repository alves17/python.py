# Função para determinar o signo
def descobrir_signo(dia, mes):
    if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        return "Áries"
    elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        return "Touro"
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        return "Gêmeos"
    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        return "Câncer"
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        return "Leão"
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        return "Virgem"
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        return "Libra"
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        return "Escorpião"
    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 22):
        return "Sagitário"
    elif (mes == 12 and dia >= 23) or (mes == 1 and dia <= 19):
        return "Capricórnio"
    elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        return "Aquário"
    elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
        return "Peixes"
    else:
        return "Data inválida"

# Loop principal
while True:
    try:
        # Entrada de dados
        dia = int(input("\nDigite o dia do seu nascimento: "))
        mes = int(input("Digite o mês do seu nascimento (1 a 12): "))

        # Processamento e saída
        signo = descobrir_signo(dia, mes)
        print(f"Seu signo é: {signo}")

    except ValueError:
        print("Por favor, insira valores numéricos válidos para o dia e o mês.")
        continue  # Volta ao início se a entrada for inválida

    # Pergunta se deseja continuar
    continuar = input("Deseja consultar outro signo? (s/n): ").strip().lower()

    if continuar == 'n':
        print("\nMuito obrigada! 😊")
        break  # Encerra o programa
    elif continuar != 's':
        print("\nOpção inválida! O programa será encerrado.")
        print("Muito obrigada! 😊")
        break  # Encerra se o usuário não digitar 's' ou 'n'


