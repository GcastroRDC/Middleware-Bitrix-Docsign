import requests
import json

def envelopeResent(tokenDocSign,listConstants,envelopeId):

    basePath = listConstants['BASEURL']
    """
    Reenvia um lembrete para os destinatários de um envelope pendente.

    Args:
        base_url (str): URL base da API DocuSign (ex.: "https://demo.docusign.net/restapi").
        account_id (str): ID da conta DocuSign.
        envelope_id (str): ID do envelope.
        access_token (str): Token de acesso OAuth 2.0.

    Returns:
        dict: Resposta da API.
    """
    url = f"{basePath}/restapi/v2.1/accounts/{listConstants['ACCOUNTID']}/envelopes/{envelopeId}/notification"

    headers = {

        "Authorization": f"Bearer {tokenDocSign}",
        "Content-Type": "application/json"
    }
     
    payload = {
        "notification": {
            "remind": True
        }
    }
    
    response = requests.put(url, headers=headers, data=json.dumps(payload))
   

    if response.status_code == 200:

        return {"status": True}
    
    else:
 
        return {"status": False}

