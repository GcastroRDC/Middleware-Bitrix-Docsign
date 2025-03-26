from Templates.templatesIntegracao.BitrixDocSign.routers.envelopeStatesEvents.tplDeclined import templateDeclined
import requests
import json
from jinja2 import Template

tpl = templateDeclined

def notificationDeclined(tokenBitrix,idDeal,envelopeId):

    endpoint = f"https://dominio.bitrix24.com.br/rest/crm.timeline.comment.add?auth={tokenBitrix}"

    template = Template(tpl)
    renderedTemplate = template.render(envelopeID=envelopeId)

    bodyData = {
                
        "fields":
                    {
                    
                        "ENTITY_ID":idDeal,
                        "ENTITY_TYPE": "deal",
                        "AUTHOR_ID":"2762",
                        f"COMMENT": renderedTemplate
                    
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