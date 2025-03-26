from Templates.templatesIntegracao.BitrixDocSign.routers.envelopeStatesEvents.tplResent import templateResent
import requests
import json
from jinja2 import Template

tpl = templateResent

def notificationResent(token,idDeal,envelopeId):

    endpoint = f"https://dominio.bitrix24.com.br/rest/crm.timeline.comment.add?auth={token}"

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