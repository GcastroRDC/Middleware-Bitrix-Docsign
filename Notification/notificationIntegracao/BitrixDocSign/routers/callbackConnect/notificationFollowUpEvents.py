import requests
import json
from jinja2 import Template
from Templates.templatesIntegracao.BitrixDocSign.routers.callbackConnect.tplFollowUpEvents import templateFollowUpApproval,templateFollowUpSignature,templateFollowUpSignatureClient

tplSignature = templateFollowUpSignature
tplApproval = templateFollowUpApproval

def notificationFollowUpEvents(token,idDeal,dicValues):

    endpoint = f"https://dominio.bitrix24.com.br/rest/crm.timeline.comment.add?auth={token}"

    # Participantes que somente aprovam o contrato
    rolesNameApproval = ["Backoffice","Advogado Administrativo B2B"]

    if dicValues["roleName"] in rolesNameApproval:
           
        template = Template(templateFollowUpApproval)
        dicValues["reason"] = "Aprovação Concluída"

    if dicValues["roleName"] not in rolesNameApproval:
        
        template = Template(templateFollowUpSignature)
        dicValues["reason"] = "Assinatura Concluída"

    templateEvents = template.render(
          
                nameRecipient=dicValues["name"],
                roleNameRecipient=dicValues["roleName"],
                emailRecipient=dicValues["email"],
                reasonRecipient=dicValues["reason"]            
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