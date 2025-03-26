import requests
import json
from jinja2 import Template
from Templates.templatesIntegracao.BitrixDocSign.routers.createEnvelope.tplError import templateError

tpl = templateError

def notificationError(token,idDeal,dicValues):

    endpoint = f"https://dominio.bitrix24.com.br/rest/crm.timeline.comment.add?auth={token}"

    template = Template(tpl)

    templateErrorCreateEnvelope = template.render(

          status=dicValues["status"],
          method=dicValues["method"],
          reason=dicValues["reason"]
          
             
    ) 
       
    bodyData = {
                
        "fields":
                    {
                    
                        "ENTITY_ID":idDeal,
                        "ENTITY_TYPE": "deal",
                        "AUTHOR_ID":"2762",
                        f"COMMENT": templateErrorCreateEnvelope
                    
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