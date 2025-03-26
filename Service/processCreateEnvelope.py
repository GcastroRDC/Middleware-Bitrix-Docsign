from Api.DocSign.token.getTokenApiDocSign import getTokenApiDocSign
from Controllers.DocSign.envelopeSchemeBuilder import envelopeSchemeBuilder
from Controllers.DocSign.getUrlEnvelope import getUrlEnvelope
from Security.Authorization.accessPermissionVerify import accessPermissionVerify
from Api.Bitrix.token.getTokenApiBitrix import getTokenApiBitrix
from Notification.notificationIntegracao.BitrixDocSign.routers.createEnvelope.notificationSent import notificationSent
from Notification.notificationIntegracao.BitrixDocSign.routers.createEnvelope.notificationCommercialConditions import notificationCommercialConditions
from Notification.notificationIntegracao.BitrixDocSign.routers.createEnvelope.notificationError import notificationError
from Api.Bitrix.endpoints.crmDealGetAll import crmDealGetAll
from Api.Bitrix.endpoints.crmDealUpdate import crmDealUpdate
from Handle.HandleError.handleErrorResponse import handleErrorResponse
from Handle.HandleError.handleErrorLogging import handleErrorLogging
from Handle.HandleError.handleMultipleErrors import handleMultipleErrors
from Handle.HandleError.handleErrorIntegrationFields import handleErrorIntegrationFields
import requests

def processCreateEnvelope(tokenRequest,idDeal,environmentVariables):
    
    if not idDeal:
               
               handleErrorLogging(None,"ID do negócio não identificado.",400)
               response = handleErrorResponse("ID do negócio não identificado.",400)

               return response
     
     # Token API REST Bitrix24
    dataTokenBitrix = getTokenApiBitrix()
    if not dataTokenBitrix["status"]:

          handleErrorLogging(
                 
                 idDeal,
                 "Status: Error | Method: getTokenApiBitrix | Mensagem: Erro na geração do token da API Bitrix24",
                 401

                 )
            
             
          response = handleErrorResponse(
                 
                 "Status: Error | Method: getTokenApiBitrix | Message: Erro na geração do token da API Bitrix24",
                 401

                 )

          return response
               
     # Validação da Autorização de Acesso
    dataAuthorization = accessPermissionVerify(tokenRequest)
    if not dataAuthorization['status']:
          
          handleErrorIntegrationFields(dataTokenBitrix["token"],idDeal,"Requisição não autorizada")

          dicValuesError = {
                    
                    "status":401,
                     "reason":"Requisição não autorizada",
                     "method":"verifyAuthorization"
            }

          notificationError(dataTokenBitrix["token"],idDeal,dicValuesError)

          handleErrorLogging(
                 
                 idDeal,dataAuthorization['message'],
                 dataAuthorization['codeErro']

                 )
          response = handleErrorResponse(
                 
                 dataAuthorization['message'],
                 dataAuthorization['codeErro']

                 )
            
          return response
        
    
          
    # Token JWT da API REST DocSign
    dataTokenDocSign = getTokenApiDocSign()
    if not dataTokenDocSign["status"]:
          
          handleErrorIntegrationFields(dataTokenBitrix["token"],idDeal,"Erro na geração do token da API DocSign")

          dicValuesError = {
                    
                    "status":401,
                     "reason":"Erro na geração do token da API DocSign",
                     "method":"getTokenApiDocSign"
            }
          
          notificationError(dataTokenBitrix["token"],idDeal,dicValuesError)

          handleErrorLogging(

                 idDeal,
                 "Status: Error | Method: getTokenApiDocSign | Mensagem: Erro na geração do token da API DocSign",
                 401

                 )
          response = handleErrorResponse(
                 
                 "Status: Error | Method: getTokenApiDocSign | Message: Erro na geração do token da API DocSign",
                 401

                 )
          return response

    # GET dos dados do negócio
    dataCrmDeal = crmDealGetAll(
             
             dataTokenBitrix["token"],
             idDeal
             
             )
    
    if not dataCrmDeal["status"]:
          
          handleErrorIntegrationFields(dataTokenBitrix["token"],idDeal,"Erro ao consultar dados do negócio")

          response = handleMultipleErrors(
                  
                  method={
                        "token":dataTokenBitrix["token"],
                        "idDeal":idDeal,
                        "router":"create.envelope",
                       "name":"crmDealGetAll",
                       "errorType":dataCrmDeal["type"],
                       "fieldsError":dataCrmDeal["fieldsError"]
                       }

                  )
        
          return response

    dicCrmDealValues = {

            "idDeal":idDeal,
            "deal":dataCrmDeal["values"]
        }
    
    
    dataFinalEnvelopeScheme = envelopeSchemeBuilder(
             
            dataTokenDocSign["token"],
            environmentVariables,
            dicCrmDealValues

            )
    
    
    if not dataFinalEnvelopeScheme["status"]:
             
            handleErrorIntegrationFields(dataTokenBitrix["token"],idDeal,"Erro na geração do scheme do envelope")

            response = handleMultipleErrors(
                   
                  method={

                        "token":dataTokenBitrix["token"],
                        "idDeal":idDeal,
                        "router":"create.envelope",
                        "name":"envelopeSchemeBuilder",
                        "errorType":dataFinalEnvelopeScheme["type"]
                   
                       }
                 

                  )
             
     
            return response
        
    response = requests.post(
             
             dataFinalEnvelopeScheme["resourcePath"],
             headers=dataFinalEnvelopeScheme["headers"],
             json=dataFinalEnvelopeScheme["body"]

             )
    
    dataJsonEnvelope = response.json()

    getUrlEnvelope(dataTokenDocSign["token"],dataJsonEnvelope['envelopeId'],environmentVariables)


    statusCodeSuccessCreateEnvelope = [200,201]

    if response.status_code in statusCodeSuccessCreateEnvelope:
            
            result = response.json()
            envelopeId = result["envelopeId"]

            valuesFieldsDeal = {
                   
                   "UF_CRM_1733491040620":envelopeId,
                   "UF_CRM_1733491181916":"envelope-sent",
                   "UF_CRM_1733491110611":"Contrato enviado",
                   "UF_CRM_1732412352707":"Enviado",
                   "UF_CRM_1732274853376":"Sim"
            }

            dataCrmDealUpdate = crmDealUpdate(dataTokenBitrix["token"],idDeal,valuesFieldsDeal)
            
            if not dataCrmDealUpdate["status"]:

               handleErrorIntegrationFields(dataTokenBitrix["token"],idDeal,"Erro ao atualizar os campos da integração o negócio")

               dicValuesError = {
                    
                    "status":400,
                     "reason":"Erro ao atualizar os campos da integração no negócio",
                     "method":"crmDealUpdate"

                     }
          
               notificationError(dataTokenBitrix["token"],idDeal,dicValuesError)

               handleErrorLogging(
                     
                     idDeal,
                       "Status: Error | Method: crmDealUpdate | Message: Erro ao atualizar os campos da integração no negócio",
                       400

                       )
                
               response = handleErrorResponse(
                     
                     "Status: Error | Method: crmDealUpdate | Message: Erro ao atualizar os campos da integração no negócio", 
                     400

                     )
                
               return response

            dataNotificationCommercial = notificationCommercialConditions(

                  dataTokenBitrix["token"],
                  idDeal,
                  dataCrmDeal["values"]
                  ) 
                 
            if not dataNotificationCommercial:
               
               handleErrorIntegrationFields(dataTokenBitrix["token"],idDeal,"Erro na inserção do comentário com as condições comerciais na timeline do negócio.")

               dicValuesError = {
                    
                    "status":400,
                     "reason":"Erro na inserção do comentário com as condições comerciais na timeline do negócio.",
                     "method":"notificationCommercialConditions"

                     }
          
               notificationError(dataTokenBitrix["token"],idDeal,dicValuesError)

               handleErrorLogging(
                     
                     idDeal,
                       "Status: Error | Method: notificationCommercialConditions | Message: Erro na inserção do comentário com as condições comerciais na timeline do negócio.",
                       400

                       )
                
               response = handleErrorResponse(
                     
                     "Status: Error | Method: notificationCommercialConditions | Message: Erro na inserção do comentário com as condições comerciais na timeline do negócio.", 
                     400

                     )
                
               return response

            dataNotificationSentSuccess = notificationSent(
                 
                 dataTokenBitrix["token"],
                 idDeal,
                 envelopeId,
                 dataFinalEnvelopeScheme["dataRecipients"]
                 )
            
            if not dataNotificationSentSuccess["status"]:
               
               handleErrorIntegrationFields(dataTokenBitrix["token"],idDeal,"Erro na inserção do comentário com a ordem de assinatura do contrato na timeline do negócio.")

               dicValuesError = {
                    
                    "status":400,
                     "reason":"Erro na inserção do comentário com a ordem de assinatura do contrato na timeline do negócio.",
                     "method":"NotificationSent"
                     }
          
               notificationError(dataTokenBitrix["token"],idDeal,dicValuesError)

               handleErrorLogging(
                     
                     idDeal,
                       "Status: Error | Method: NotificationSent | Message: Erro na inserção do comentário com a ordem de assinatura do contrato na timeline do negócio.",
                       400

                       )
                
               response = handleErrorResponse(
                     
                     "Status: Error | Method: NotificationSent | Message: Erro na inserção do comentário com a ordem de assinatura do contrato na timeline do negócio.", 
                     400

                     )
                
               return response
            
            return {
                 
                 "status":True,
                 "statusCode":200,
                 "message":"Envelope enviado com sucesso!"

                 }
    
    handleErrorIntegrationFields(dataTokenBitrix["token"],idDeal,"Erro no envio do envelope")

    dicValuesError = {
                    
                    "status":400,
                     "reason":"Erro no envio do envelope.",
                     "method":"request.post"
                     }
          
    notificationError(dataTokenBitrix["token"],idDeal,dicValuesError)
    
    handleErrorLogging(
                     
                     idDeal,
                       "Status: Error | Method: request.post | Message: Erro no envio do envelope.",
                       400

                       )
                
    response = handleErrorResponse(
                     
                     "Status: Error | Method: request.post | Message: Erro no envio do envelope.", 
                     400

                     )
                
    return response
   
            
        
       

          