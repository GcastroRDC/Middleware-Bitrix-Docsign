import requests
import json

def crmTimelineCommentFileClient(tokenBitrix, idDeal, clientType, listFiles):

    endpointCrmTimelineCommentAdd = f"https://dominio.bitrix24.com.br/rest/crm.timeline.comment.add?auth={tokenBitrix}"

    # Mapeamento de clientType para os arquivos e suas respectivas posições
    fileMapping = {

        "Base": ["Prévia Ordem de Serviço", "Manual de Operações", "Ementa das Assinaturas"],  # Arquivos para "Base"
        "Novo": ["Prévia Ordem de Serviço", "Manual de Operações", "Prévia Contrato", "Ementa das Assinaturas"]  # Arquivos para "Novo"
    }

    # Verifica se o clientType existe no mapeamento
    if clientType not in fileMapping:

        return {"status": False}

    # Pega os arquivos para o tipo de cliente específico
    filesNames = fileMapping[clientType]

    # Filtra os arquivos a serem processados
    # Para "Novo" os arquivos nas posições 0 e 2, para "Base" apenas 0
    keyFilesWanted = [0] if clientType == "Base" else [0, 2]

    for key, file in enumerate(listFiles):

        if key in keyFilesWanted:

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

            
            response = requests.post(endpointCrmTimelineCommentAdd, data=json.dumps(bodyData), headers={'Content-Type': 'application/json'})

            if response.status_code == 200:

                continue
            
            return {"status": False}  
        
    return {"status": True} 
