from funcoes import*

print("------------ESTACIONAMENTO--------------")
vagas = int(input("Digite o total de vagas disponíveis: "))
total_vagas = 0
limpar_tela()
estacionamento = {}


while True:
    print("------------ESTACIONAMENTO--------------")
    escolha = opcoes()
    limpar()

    if escolha == "1":
        if total_vagas <= vagas:
            inserirVeiculo(estacionamento)
            limpar()
            total_vagas += 1
            vagas -= 1
        else:
            print("Estacionamento cheio.")
            limpar()
    elif escolha == "2":
        removerVeiculo(estacionamento, vagas, input("Digite a placa do veículo que deseja remover: ").upper())
        limpar()
    elif escolha == "3":
        placa = input("Digite a placa do veículo que deseja buscar: ").upper()
        buscarVeiculo(estacionamento, placa)
        input("Pressione Enter para voltar ao menu.")
        limpar()
    elif escolha == "4":
        listarVagasOcupadas(estacionamento)
        input("Pressione Enter para voltar ao menu.")
        limpar()
    elif escolha == "5":
        listarVagasDisponiveis(vagas)
        limpar()
    elif escolha == "6":
        print("Programa encerrado....")
        limpar()
        break
    else:
        print("Por favor, digite uma opção válida.")
        limpar()