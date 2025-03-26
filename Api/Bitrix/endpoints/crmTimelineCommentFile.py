import requests
import json

def crmTimelineCommentFile(tokenBitrix,idDeal,clientType,listFiles):
    
    endpointCrmTimelineCommentAdd = f"https://dominio.bitrix24.com.br/rest/crm.timeline.comment.add?auth={tokenBitrix}"

    filesNames = []

    limit = 0

    if clientType == "Base":
         
         filesNames.extend(["Ordem de Serviço","Manual de Operações","Ementa das Assinaturas"])
         limit = 2
    
    if clientType == "Novo":

        filesNames.extend(["Ordem de Serviço", "Manual de Operações", "Contrato", "Ementa das Assinaturas"])
        limit = 3

    for key, file in enumerate(listFiles):

        if key > limit: 

            break  

        # Verifica se o índice está dentro do limite de fileNames
        fileName = filesNames[key] if key < len(filesNames) else f"Documento_{key + 1}"

        bodyData = {
             
            "fields": {
                "ENTITY_ID": idDeal,
                "ENTITY_TYPE": "deal",
                "AUTHOR_ID": "2762",
                "COMMENT": f"Segue em anexo o documento: {fileName}",
                "FILES": {
                     
                    "fileData": [
                         
                        f"{fileName}.pdf", 
                        file
                    ]
                }
            }
        }

        # Enviar a solicitação POST
        response = requests.post(endpointCrmTimelineCommentAdd, data=json.dumps(bodyData), headers={'Content-Type': 'application/json'})

        if response.status_code == 200:

            continue
        
        return {"status": False}

    return {"status": True}