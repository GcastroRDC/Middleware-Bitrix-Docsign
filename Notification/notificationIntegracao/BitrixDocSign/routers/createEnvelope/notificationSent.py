import requests
import json
from jinja2 import Template
from Templates.templatesIntegracao.BitrixDocSign.routers.createEnvelope.tplSent import templateSent

tplSent = templateSent

def notificationSent(token,idDeal,envelopeId,dataGroupSigners):

    endpoint = f"https://dominio.bitrix24.com.br/rest/crm.timeline.comment.add?auth={token}"

    recipients = "\n".join(
           
        f"Função: {role['roleName']}\nNome: {role['name']}\nE-mail: {role['email']}\n{'-' * 40}"
        for role in dataGroupSigners
    )
    
    template = Template(tplSent)

    templateSentEvent = template.render(
          
                dataRecipients=recipients,
                envelopeID=envelopeId      
        ) 
    
    bodyData = {
                
        "fields":
                    {
                    
                        "ENTITY_ID":idDeal,
                        "ENTITY_TYPE": "deal",
                        "AUTHOR_ID":"2762",
                        f"COMMENT": str(templateSentEvent)
                    
                }
            }
    
    response = requests.post(
           endpoint,
           data=json.dumps(bodyData),
           headers={'Content-Type':'application/json'}
           )  

    if response.status_code == 200:
                 
            return {"status":True}
                
    else:
                   
            return {"status":False}