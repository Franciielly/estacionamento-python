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
4 - Listar Vagas Ocupadas
5 - Listar Vagas Livres 
6 - Sair
"""

    resposta = input(menu + "Digite uma opção: ")
    return resposta

def inserirVeiculo(estacionamento):
    placa = input("Digite a placa: ").upper()
    estacionamento[placa] = [input("Digite o nome do proprietário do veículo: ").upper(),
                            input("Digite o número da vaga ocupada: ").upper(),
                            input("Digite o modelo do veículo: ").upper(),
                            input("Digite a cor do veículo: ").upper(),
                            input("Digite a hora de entrada: ")]

    
def removerVeiculo(estacionamento, vagas, total_vagas, placa):
    lista = estacionamento.get(placa) 
    if lista != None:
        print("Nome...........: " + lista[0])
        print("Vaga...........: " + lista[1])
        print("Modelo.........: " + lista[2])
        print("Cor............: " + lista[3])
        print("Hora...........: " + lista[4])
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
        print("Vaga...........: " + lista[1])
        print("Modelo.........: " + lista[2])
        print("Cor............: " + lista[3])
        print("Hora...........: " + lista[4])
    else:
        print("Veículo não encontrado.")

def listarVagasDisponiveis(vagas):
    print(f"Há {vagas} vagas disponíveis")

def listarVagasOcupadas(estacionamento):
    if estacionamento:
        for placa, dados in estacionamento.items():
            print(f"Placa: {placa} - Vaga: {dados[1]}")
    else:
        print("Nenhuma vaga ocupada.")

    

