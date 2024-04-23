from datetime import date
from baixarContaBTG import baixarContaBTG
from baixarContasXP import baixarContaXP
from criarListaGeral import criarListaGeral
from criarLogErrosGeral import criarLogErrosGeral
from dadosCliente import buscarDadosMonday

bearer = ''

tokenJWT = ''

dadosCliente = buscarDadosMonday()

listaContasGeral = []

logErrosGeral = []

dataHoje = date.today()
dataFormatada = dataHoje.strftime("%d/%m/%Y")

i = 0

for cliente in dadosCliente:

    i += 1

    contasCliente = []
    logErros = []

    nbVeneto = cliente['nbVeneto']
    nbBTG = cliente['nbBTG']
    nbXP = cliente['nbXP']
    nomeCliente = cliente['nome']

    print(f'Rodando cliente: {nomeCliente}')

    if nbXP != '-':
        contasCliente, logErros = baixarContaXP(nbXP, bearer, contasCliente, logErros)

    if nbBTG != '-':
        contasCliente, logErros = baixarContaBTG(nbBTG, tokenJWT, contasCliente, logErros)
    
    print(len(contasCliente))
    print(f'cliente numero {i}')

    if len(contasCliente) > 0:
        dadosCliente = {
            'nome': nomeCliente,
            'nbVeneto': nbVeneto,
            'contas': contasCliente
        }

        listaContasGeral.append(dadosCliente) 
    
    if len(logErros) > 0:
        dadosErro = {
            'nome': nomeCliente,
            'nbVeneto': nbVeneto,
            'erros': logErros
        }

        logErrosGeral.append(dadosErro)

criarLogErrosGeral(logErrosGeral, dataFormatada)
criarListaGeral(listaContasGeral, dataFormatada)
