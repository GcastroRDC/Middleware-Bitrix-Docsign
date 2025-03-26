
import requests

def getEnvelopeStatus(tokenDocSign, listConstants, envelopeId):

    basePath = listConstants['BASEURL']
    
    url = f"{basePath}/restapi/v2.1/accounts/{listConstants['ACCOUNTID']}/envelopes/{envelopeId}"
    
    headers = {
        "Authorization": f"Bearer {tokenDocSign}"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:

        envelope_data = response.json()

        # Retorna o status atual do envelope
        return {
            "status":True,
            "statusEnvelope":envelope_data['status'] 
            } 
    else:

        return {
            "status":False,
            "statusEnvelope":None
            }
