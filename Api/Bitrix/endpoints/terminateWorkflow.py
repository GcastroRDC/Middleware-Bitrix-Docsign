import requests

def terminateWorkflow(tokenBitrix, workflowId,IdDeal):

    # Monta a URL completa para o endpoint
    url = f"https://dominio.bitrix24.com.br/rest/bizproc.workflow.terminate?auth={tokenBitrix}"

    # Parâmetros necessários para a requisição
    params = {
        
        "ID": workflowId,  # ID do fluxo de trabalho que você deseja terminar
        "STATUS":"Fluxo encerrado pelo Middleware de integração Bitrix x DocSign",
        "DOCUMENT_ID":f"CRM_{IdDeal}",  # ID do documento/negócio que está associado ao fluxo
    }

    
    response = requests.post(url , params=params)
        
    if response.status_code == 200:
            
            return {"status": True}
            
    else:
           
            return {"status": False}


