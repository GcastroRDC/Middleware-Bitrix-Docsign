import requests
import json
from jinja2 import Template
from Templates.templatesIntegracao.BitrixDocSign.routers.createEnvelope.tplErrorEmptyFields import templateErrorEmptyFields

tpl = templateErrorEmptyFields

def notificationErrorEmptyFields(token,idDeal,dicValues):

    endpoint = f"https://dominio.bitrix24.com.br/rest/crm.timeline.comment.add?auth={token}"

    template = Template(tpl)

    formattedFields = "\n".join(
           
        f"{role}\n{'-' * 30}"
        for role in dicValues['fields']
    )

    templateErrorEmptyFieldsCreateEnvelope = template.render(

          status=dicValues["status"],
          method=dicValues["method"],
          reason=dicValues["reason"],
          fields=formattedFields
                
    ) 
       
    bodyData = {
                
        "fields":
                    {
                    
                        "ENTITY_ID":idDeal,
                        "ENTITY_TYPE": "deal",
                        "AUTHOR_ID":"2762",
                        f"COMMENT": templateErrorEmptyFieldsCreateEnvelope
                    
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