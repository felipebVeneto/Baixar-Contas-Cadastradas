import pandas as pd

def criarListaGeral(listaGeral, dataFormatada):

    listaContas = pd.read_excel('Contas Cadastradas Template.xlsx', skiprows=(0, 1))
    
    numLinhas = listaContas.shape[0]

    if numLinhas > 0:
        lin = numLinhas + 1
    else:
        lin = 1

    for cliente in listaGeral:

        nomeCliente = cliente['nome']
        nbVeneto = cliente['nbVeneto']
        contas = cliente['contas']

        for conta in contas:
            
            instituicao = conta['instituicao']
            banco = conta['banco']
            agencia = conta['agencia']
            numConta = conta['numConta']
            tipoConta = conta['tipoConta']
            contaVeneto = conta['contaVeneto']
            nbCorretora = conta['nbCorretora']

            listaContas.loc[lin, "NB"] = nbVeneto
            listaContas.loc[lin, "NOME"] = nomeCliente
            listaContas.loc[lin, "CORRETORA"] = contaVeneto
            listaContas.loc[lin, "NB CORRETORA"] = nbCorretora
            listaContas.loc[lin, "BANCO"] = banco
            listaContas.loc[lin, "AGENCIA"] = agencia
            listaContas.loc[lin, "CONTA"] = numConta
            listaContas.loc[lin, "TIPO"] = tipoConta
            listaContas.loc[lin, "INSTITUICAO"] = instituicao

            lin += 1
    dataFormatada = dataFormatada.replace("/", ".")
    nomeArq = f'Contas Cadastradas - {dataFormatada}.xlsx'
    listaContas.to_excel(nomeArq, index=False)