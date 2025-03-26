import requests
import json
from jinja2 import Template
from Templates.templatesIntegracao.BitrixDocSign.routers.createEnvelope.tplCommercialConditions import templateCommercialConditions

tplSent = templateCommercialConditions

def notificationCommercialConditions(token,idDeal,dataCrmDeal):

    endpoint = f"https://dominio.bitrix24.com.br/rest/crm.timeline.comment.add?auth={token}"

    template = Template(tplSent)

    templateSentCommercialConditions = template.render(
           
                contractingCompany=dataCrmDeal["razaoSocialContratante"],
                clientType=dataCrmDeal["tipoCliente"],
                product=dataCrmDeal["servicoContratado"],
                velocity=dataCrmDeal["velocidade"],
                availability=dataCrmDeal["disponibilidade"],
                CommercialObservations=dataCrmDeal["observacoesCondicaoComercial"],
                contractNumber=dataCrmDeal["numeroContrato"],
                serviceOrder=dataCrmDeal["numeroOrdemServico"],
                dateHire=dataCrmDeal["dataContratacao"],
                dateExtinction=dataCrmDeal["dataExtincao"],
                InvoiceDueDate=dataCrmDeal["dataVencimentoFatura"],
                duration=dataCrmDeal["duracao"],
                monthValue=dataCrmDeal["valorMensalPorExtenso"],
                totalContractValue=dataCrmDeal["valorTotalContrato"],
                installationDeadline=dataCrmDeal["prazoInstalacao"],
                installationRate=dataCrmDeal["taxaInstalacao"],
                InstallationInstallments=dataCrmDeal["numeroParcelasInstalacao"],
                installationModel=dataCrmDeal["modeloInstalacao"]
        ) 
    
    bodyData = {
                
        "fields":
                    {
                    
                        "ENTITY_ID":idDeal,
                        "ENTITY_TYPE": "deal",
                        "AUTHOR_ID":"2762",
                        f"COMMENT": str(templateSentCommercialConditions)
                    
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