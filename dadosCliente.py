import math

import pandas as pd

def buscarDadosMonday():

    monday = pd.read_excel('monday.xlsx', skiprows=(0, 1), dtype={'CONTA BTG': str, 'CONTA XP': str})

    ultLin = monday.iloc[-1].name

    listaClientes = []

    lin = 2

    for lin in range(ultLin + 1):

        nbBTG = monday.loc[lin, "CONTA BTG"]

        if type(nbBTG) == float and math.isnan(nbBTG):
            nbBTG = "-"
        
        nbXP = monday.loc[lin, "CONTA XP"]

        if type(nbXP) == float and math.isnan(nbXP):
            nbXP = "-"

        # Pega o nome
        nomeCliente = monday.loc[lin, "Name"]

        # Pega o nb
        nbVeneto = monday.loc[lin, "CONTA VENETO"]

        cpf = monday.loc[lin, "CPF / CNPJ"]

        # Pega o nome do Officer
        officer = monday.loc[lin, "FARMER"]

        cliente = {
                'nbVeneto': nbVeneto,
                'nome': nomeCliente,
                'cpf': cpf,
                'officer':officer,
                'nbBTG': nbBTG,
                'nbXP': nbXP,
        }

        listaClientes.append(cliente)

    return listaClientes