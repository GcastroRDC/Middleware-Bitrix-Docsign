import requests

def handleErrorIntegrationFields(tokenBitrix,idDeal,reasonError):

    endpointCrmDealUpdate = f"https://dominio.bitrix24.com.br/rest/crm.deal.update?auth={tokenBitrix}"
   
    headers = {

        "Authorization": f"Bearer {tokenBitrix}",
        "Content-Type": "application/json"
    }


    data = {

        "ID": idDeal,  # ID do negócio
         # Campos a serem atualizados
        "FIELDS": {
                
                   "UF_CRM_1733491181916":"Erro Integração",
                   "UF_CRM_1733491110611":str(reasonError),
                   "UF_CRM_1732412352707":"Erro"

        } 
    }

    # Fazendo a requisição POST para a API
    response = requests.post(endpointCrmDealUpdate, headers=headers, json=data)

    # Verificando a resposta
    if response.status_code == 200:
        
        return {"status":True}
       
    else:
         return {"status":False}