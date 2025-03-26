import requests

def getUrlEnvelope(tokenDocsign,envelopeId,listConstants):

    """
        Função para obter a URL do envelope criado.
        
        Parâmetros:

        - listConstants: Lista com variaveis de ambiente
        - envelopeId: ID do envelope.
        - tokenDocsign: Token de acesso OAuth para autenticação.

        Retorna:

        - URL do documento (se houver) ou uma mensagem de erro.
        """
    basePath = listConstants['BASEURL']

    resourcePath = f"{basePath}/restapi/v2.1/accounts/{listConstants['ACCOUNTID']}/envelopes/{envelopeId}/documents"

    headers = {

    "Authorization": f"Bearer {tokenDocsign}",
    "Content-Type": "application/json"

    }
    
    response = requests.get(resourcePath, headers=headers)
    

    if response.status_code == 200:

        documents = response.json() 
    
        # Verificando se há documentos no envelope
        if 'documents' in documents and len(documents['documents']) > 0:

            document = documents['documents'][0]  # Considerando o primeiro documento

            return {"status":True,"url":document['url']} # Retorna a URL do documento
        else:
            return False
    else:
        
        return False