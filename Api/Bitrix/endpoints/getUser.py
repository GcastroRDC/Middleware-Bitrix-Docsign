import requests

def userGet(tokenBitrix,idUser):

    endpointUserGet = f"https://dominio.bitrix24.com.br/rest/user.get?auth={tokenBitrix}"
    # Parâmetros da consulta, incluindo o ID da empresa
    params = {

        'ID': idUser 
    }

    # Enviando a requisição GET para a API
    response = requests.get(endpointUserGet, params=params)

    # Verificando o status da resposta
    if response.status_code == 200:
       
        user_data = response.json()
        
         # Verifica se a chave "result" existe e contém dados
        if 'result' in user_data:

            user_info = user_data['result']
            
            # Extraindo os campos específicos
            userName = user_info.get('NAME', None)
            userEmail = user_info.get('EMAIL', None)

            fieldsUser = {

                "userName":userName,
                "userEmail":userEmail
            }

            return {

                    "status":True,
                    "values":fieldsUser,
                    "type":"success"

                    }
        
        return {
                    "status":False,
                    "values":None,
                    "type":"empty"

                    }
        
    return {

            "status":False,
            "values":None,
            "type":"error"

            }