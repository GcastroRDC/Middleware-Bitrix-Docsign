import requests

def crmDealUpdate(tokenBitrix, idDeal, values):

    endpointCrmDealUpdate = f"https://dominio.bitrix24.com.br/rest/crm.deal.update?auth={tokenBitrix}"
   
    headers = {

        "Authorization": f"Bearer {tokenBitrix}",
        "Content-Type": "application/json"
    }


    data = {
        "ID": idDeal,  # ID do negócio
        "FIELDS": values  # Campos a serem atualizados
    }

    # Fazendo a requisição POST para a API
    response = requests.post(endpointCrmDealUpdate, headers=headers, json=data)

    # Verificando a resposta
    if response.status_code == 200:
        
        return {"status":True}
       
    else:
         return {"status":False}
