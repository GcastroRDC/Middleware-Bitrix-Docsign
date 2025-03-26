import requests
import json
from jinja2 import Template

tpl = None

def NotificationSent(token,idDeal):

    endpoint = f"https://dominio.bitrix24.com.br/rest/crm.timeline.comment.add?auth={token}"

    template = Template(tpl)
    renderedTemplate = template.render()

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