import requests


def baixarContaXP(nbXP, bearer, contasCliente, logErros):

    subscriptionKey = '14e2f53f870f4f729d4f5a300e3cac37'

    # Determina a URL para requisição
    url = f'https://api.xpi.com.br/hub-pj/api/v1/info-accounts/{nbXP}'

    # Determina os Headers da requisição
    headers = {'Ocp-Apim-Subscription-Key': subscriptionKey,
               'Authorization': 'Bearer ' + bearer,
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
               }

    # Realiza a requisição
    response = requests.get(url, headers=headers)

    # Verifica se a requisição obteve sucesso
    if response.status_code == 200:
        # Armazena o JSON retornado
        data = response.json()

        contas = data['data']['accounts']
        print('Conta XP')
        print('------------------------')

        for conta in contas:
            instituicao = conta['bankName']
            banco = conta['bank']
            agencia = conta['agency']
            numConta = conta['accountNumber']
            tipoConta = conta['accountType']

            conta = {
                'instituicao': instituicao,
                'banco': banco,
                'agencia': agencia,
                'numConta': numConta,
                'tipoConta': tipoConta,
                'contaVeneto': 'XP',
                'nbCorretora': nbXP,
            }

            contasCliente.append(conta)

        return contasCliente, logErros
    else:
        print(
            f'Não foi possível baixar as contas - Response:{response.status_code}')
        
        logErros.append({
            'conta': nbXP,
            'response': response.status_code,
            'corretora':'XP'
        })
        return [], logErros
