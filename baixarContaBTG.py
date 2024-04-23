import requests


def baixarContaBTG(nbBTG, tokenJWT, contasCliente, logErros):


    url = f'https://access.btgpactualdigital.com/op/api/withdrawal/v2/accounts/{nbBTG}'

    headers = {
                'Authorization': 'JWT ' + tokenJWT,
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
                'X-System-From': 'RMADMIN'
                }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:

        data = response.json()

        contas = data['accounts']
        print('Conta BTG')
        print('--------------------------------------')
        for conta in contas:
            
            instituicao = conta['financialInstitution']['name']
            banco = conta['financialInstitution']['number']
            agencia = conta['agency']['agencyNumber']
            numConta = conta['accountNumber']
            tipoConta = conta['accountType']

            conta = {
                     'instituicao': instituicao,
                     'banco': banco,
                     'agencia': agencia,
                     'numConta': numConta,
                     'tipoConta': tipoConta,
                     'contaVeneto': 'BTG',
                     'nbCorretora': nbBTG,
            }

            contasCliente.append(conta)
               
        return contasCliente, logErros
    else:
        print(f'Não foi possível baixar as contas BTG - Response: {response.status_code}')
        logErros.append({
            'conta': nbBTG,
            'response': response.status_code,
            'corretora':'BTG'
        })
        return [], logErros