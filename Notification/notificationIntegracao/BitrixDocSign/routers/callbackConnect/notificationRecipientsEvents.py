import requests
import json
from jinja2 import Template
from Templates.templatesIntegracao.BitrixDocSign.routers.callbackConnect.tplRecipientsEvents import templateRecipientEvents

tplRecipientsEvents = templateRecipientEvents


def notificationRecipientsEvents(token,idDeal,dicValues):

    endpoint = f"https://dominio.bitrix24.com.br/rest/crm.timeline.comment.add?auth={token}"


    template = Template(tplRecipientsEvents)

    templateEvents = template.render(

                statusEvent=dicValues["statusEvent"],
                reason=dicValues["reason"],
                roleNameRecipient=dicValues["roleName"],
                nameRecipient=dicValues["name"],
                emailRecipient=dicValues["email"]
  
        ) 
    
    bodyData = {
              
        "fields":
                    {
                    
                        "ENTITY_ID":idDeal,
                        "ENTITY_TYPE": "deal",
                        "AUTHOR_ID":"2762",
                        f"COMMENT": templateEvents
                    
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