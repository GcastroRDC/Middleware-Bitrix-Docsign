import requests

def crmDealGetValues(tokenBitrix,idDeal):

    endpointCrmDealGet = f"https://dominio.bitrix24.com.br/rest/crm.deal.get?auth={tokenBitrix}"
   
    params = {

        'ID': idDeal 
    }

    # Enviando a requisição GET para a API
    response = requests.get(endpointCrmDealGet, params=params)

    # Verificando o status da resposta
    if response.status_code == 200:

        dealData = response.json()
        
         # Verifica se a chave "result" existe e contém dados
        if 'result' in dealData:

            dealInfo = dealData['result']
            
            # Extração dos campos específicos
            clientType = dealInfo.get('UF_CRM_1732228475718',None)
            envelopeId = dealInfo.get('UF_CRM_1733491040620',None)
            idFluxoTrabalhoAtivo = dealInfo.get('UF_CRM_1740673411', None)
           
            # Construção de um dicionário com os valores que desejo buscar do negócio
            fieldsDeal ={
                
                "clientType":clientType,
                "envelopeId":envelopeId,
                "idFluxoTrabalhoAtivo":idFluxoTrabalhoAtivo
              
            }

             # Lista para armazenar as chaves com erros
            fieldsDealError = []
            
            # Percorre todos os campos do dicionario "fieldsDeal"
            for chave, valor in fieldsDeal.items():

                # Verifica se o valor está vazio ou é None
                if not valor or not str(valor).strip():

                    fieldsDealError.append(chave)  # Adiciona a chave a lista "fieldsDealError" 
            
             # Valida se a lista "fieldsDealError" está vazia, caso sim significa que não temos campos obrigatórios vazios ou nulos
            if not fieldsDealError:
                
                return {
                    "status":True,
                    "values":fieldsDeal
                    }
            
            # Caso não, significa que temos campos obrigatórios vazios ou nulos,reportando uma notificação ao usuário na timeline do negócio para correção dos dados.
            else:
                  return {
                      
                      "status":False,
                      "values":None,
                      "type":"emptyFields"
                      }

        return {

            "status":False,
            "values":None,
            "type":"notFoundDealValues"
            }
    
    else:

        return {

            "status":False,
            "values":None,
            "type":"error"
            }