import requests
from Controllers.DocSign.getEnvelopeStatus import getEnvelopeStatus

def envelopeDeclined(tokenDocSign,listConstants,reasonCancel,envelopeId):

    envelopeStatusAllowed = ["sent","delivered"]

    basePath = listConstants['BASEURL']

    """
    Cancela/Anula um envelope na DocuSign.

    Args:
        base_url (str): URL base da API DocuSign (ex.: "https://demo.docusign.net/restapi").
        account_id (str): ID da conta DocuSign.
        envelope_id (str): ID do envelope a ser cancelado.
        access_token (str): Token de acesso OAuth 2.0.
        motivo (str): Motivo para cancelar o envelope.

    Returns:
        dict: Resposta da API.
    """
    url = f"{basePath}/restapi/v2.1/accounts/{listConstants['ACCOUNTID']}/envelopes/{envelopeId}"
    
    
    headers = {

    "Authorization": f"Bearer {tokenDocSign}",
    "Content-Type": "application/json"

    }
    
    data = {
          
        "status": "voided",
        "voidedReason": reasonCancel
    }

    if not envelopeId:
         {
        "status": False,
        "type":"envelopeIdEmpty"
        }


    dataEnvelopeStatus = getEnvelopeStatus(tokenDocSign,listConstants,envelopeId)
   
    if dataEnvelopeStatus["statusEnvelope"] in envelopeStatusAllowed:
          
        response = requests.put(url, headers=headers, json=data)

        if response.status_code == 200:
            
            return {"status": True}
        
        else:

            return {
                "status": False,
                "type":"error"
                }
        
    if dataEnvelopeStatus["statusEnvelope"] == "voided":

        return {
        "status": False,
        "type":"statusVoided"
        }

    if  dataEnvelopeStatus["statusEnvelope"] == "declined":

        return {
        "status": False,
        "type":"statusDeclined"
        }

    return {
        "status": False,
        "type":"statusNotAllowed"
        }