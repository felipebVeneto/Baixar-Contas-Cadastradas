import pandas as pd

def criarLogErrosGeral(logErrosGeral, dataFormatada):

    logErros = pd.read_excel('Log Erros.xlsx', skiprows=(0, 1))
    
    numLinhas = logErros.shape[0]

    if numLinhas > 0:
        lin = numLinhas + 1
    else:
        lin = 1

    for cliente in logErrosGeral:
        nomeCliente = cliente['nome']
        nbVeneto = cliente['nbVeneto']  
        erros = cliente['erros']

        for erro in erros:
            
            conta = erro['conta']
            response = erro['response']
            corretora = erro['corretora']

            logErros.loc[lin, "NB"] = nbVeneto
            logErros.loc[lin, "NOME"] = nomeCliente
            logErros.loc[lin, "CONTA"] = conta
            logErros.loc[lin, "RESPONSE"] = response
            logErros.loc[lin, "CORRETORA"] = corretora
            lin += 1
    
    dataFormatada = dataFormatada.replace("/", ".")
    nomeArq = f'Log Erros - {dataFormatada}.xlsx'
    logErros.to_excel(nomeArq, index=False)