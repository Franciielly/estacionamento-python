import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def limpar():
    time.sleep(2)
    limpar_tela()

def opcoes():
    menu = """
1 - Inserir Veículo
2 - Remover Veículo
3 - Buscar Veículo
4 - Quantidade de Vagas Ocupadas
5 - Quantidade de Vagas Livres 
6 - Sair
"""

    resposta = input(menu + "Digite uma opção: ")
    return resposta

def inserirVeiculo(estacionamento):
    placa = input("Digite a placa: ").upper()
    estacionamento[placa] = [input("Digite o nome do proprietário do veículo: ").upper(),
                            input("Digite o modelo do veículo: ").upper(),
                            input("Digite a cor do veículo: ").upper(),
                            input("Digite a hora de entrada: ")]

    
def removerVeiculo(estacionamento, vagas, total_vagas, placa):
    lista = estacionamento.get(placa) 
    if lista != None:
        print("Nome...........: " + lista[0])
        print("Modelo.........: " + lista[1])
        print("Cor............: " + lista[2])
        print("Hora...........: " + lista[3])
        resposta = input("Deseja retirar veículo: ").upper()
        if resposta == "SIM": 
            del estacionamento[placa]
            print("Veículo removido.")
            vagas += 1
            total_vagas -= 1
            return vagas, total_vagas
        elif resposta == "NÃO" or resposta == "NAO":
            print("Remoção cancelada.")
        else:
            print("Digite apenas SIM ou NÃO.")
        

def buscarVeiculo(estacionamento, placa):
    lista = estacionamento.get(placa) 
    if lista != None:
        print("Nome...........: " + lista[0])
        print("Modelo.........: " + lista[1])
        print("Cor............: " + lista[2])
        print("Hora...........: " + lista[3])
    else:
        print("Veículo não encontrado.")

def listarVagasDisponiveis(vagas):
    print(f"Há {vagas} vagas disponíveis")

def listarVagasOcupadas(estacionamento, total_vagas):
    if estacionamento:
        print(f"Total de vagas ocupadas: {total_vagas}")
        for placa, dados in estacionamento.items():
            print(f"Placa: {placa} -")
    else:
        print("Nenhuma vaga ocupada.")

    

