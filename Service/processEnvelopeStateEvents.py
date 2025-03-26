from Controllers.DocSign.envelopeDeclined import envelopeDeclined
from Controllers.DocSign.envelopeResent import envelopeResent
from Api.DocSign.token.getTokenApiDocSign import getTokenApiDocSign
from Security.Authorization.accessPermissionVerify import accessPermissionVerify
from Api.Bitrix.token.getTokenApiBitrix import getTokenApiBitrix
from Api.Bitrix.endpoints.crmDealGetValues import crmDealGetValues
from Api.Bitrix.endpoints.crmDealUpdate import crmDealUpdate
from Notification.notificationIntegracao.BitrixDocSign.routers.createEnvelope.notificationError import notificationError
from Notification.notificationIntegracao.BitrixDocSign.routers.envelopeStatesEvents.notificationError import notificationError
from Notification.notificationIntegracao.BitrixDocSign.routers.envelopeStatesEvents.notificationDeclined import notificationDeclined
from Notification.notificationIntegracao.BitrixDocSign.routers.envelopeStatesEvents.notificationResent import notificationResent
from Handle.HandleError.handleErrorResponse import handleErrorResponse
from Handle.HandleError.handleErrorLogging import handleErrorLogging
from Handle.HandleError.handleMultipleErrors import handleMultipleErrors
from Handle.HandleError.handleErrorIntegrationFields import handleErrorIntegrationFields

def processEnvelopeStateEvents(idDeal,tokenRequest,dicEnviroments,eventType,eventReason):

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
                     "reason":"Requisição não autorizada!",
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
    
    dataCrmDealGetValues = crmDealGetValues(dataTokenBitrix["token"],idDeal)
    if not dataCrmDealGetValues["status"]:
          
          handleErrorIntegrationFields(dataTokenBitrix["token"],idDeal,"Erro ao consultar dados do negócio")

          response = handleMultipleErrors(
                
              method={
                        
                        "token":dataTokenBitrix["token"],
                        "idDeal":idDeal,
                        "router":"envelope.state.events",
                       "name":"crmDealGetValues",
                       "errorType":dataCrmDealGetValues["type"]
                   
                       }
                
             )
          
          return response

    envelopeId = dataCrmDealGetValues["values"]["envelopeId"]

    match str(eventType):

       case "voided":

              dataEnvelopeDeclined = envelopeDeclined(
                    
                  dataTokenDocSign["token"],
                  dicEnviroments,
                  eventReason,
                  envelopeId
                 
                  )
            
              if not dataEnvelopeDeclined["status"]:
                  
                  handleErrorIntegrationFields(dataTokenBitrix["token"],idDeal,"Erro ao anular o contrato")

                  response = handleMultipleErrors(
                     
                     method={
                            "token":dataTokenBitrix["token"],
                            "idDeal":idDeal,
                            "router":"envelope.state.events",
                            "name":"envelopeDeclined",
                            "errorType":dataEnvelopeDeclined["type"]
                            
                            }

                  )
        
                  return response
              

              valuesFieldsDeal = {
                   
                   "UF_CRM_1733491181916":"envelope-voided",
                   "UF_CRM_1733491110611":"Contrato anulado",
                   "UF_CRM_1732412352707":"Anulado"
                   
            }

              dataCrmDealUpdate = crmDealUpdate(dataTokenBitrix["token"],idDeal,valuesFieldsDeal)
            
              if not dataCrmDealUpdate["status"]:
               
               handleErrorIntegrationFields(dataTokenBitrix["token"],idDeal,"Erro ao atualizar os campos da integração no negócio")

               dicValuesError = {
                    
                    "status":400,
                     "reason":"Evento: Anular Contrato | Erro ao atualizar os campos da integração no negócio",
                     "method":"crmDealUpdate"
                     }
          
               notificationError(dataTokenBitrix["token"],idDeal,dicValuesError)

               handleErrorLogging(
                     
                     idDeal,
                       "Status: Error | Method: crmDealUpdate | Event: envelope-declined | Message: Erro ao atualizar os campos da integração no negócio",
                       400

                       )
                
               response = handleErrorResponse(
                     
                     "Status: Error | Method: crmDealUpdate | Event: envelope-declined | Message: Erro ao atualizar os campos da integração no negócio", 
                     400

                     )
                
               return response
              
              dataNotificationDeclined = notificationDeclined(
                    
                    dataTokenBitrix["token"],
                    idDeal,
                    envelopeId

                    )

              if not dataNotificationDeclined["status"]:

                     handleErrorIntegrationFields(dataTokenBitrix["token"],idDeal,"Erro ao inserir comentário na timeline do negócio")

                     dicValuesError = {
                    
                    "status":400,
                     "reason":"Erro ao inserir comentário na timeline do negócio | Evento: Anulação de contrato",
                     "method":"notificationDeclined"
                     }
                  
                     notificationError(dataTokenBitrix["token"],idDeal,dicValuesError)

                     handleErrorLogging(

                     idDeal,
                     "Status: timelineCommentError | Method: notificationDeclined | Mensagem: Erro ao inserir comentário na timeline do negócio",
                     400

                     )

                     response = handleErrorResponse(
                     
                     "Status: timelineCommentError | Method: notificationDeclined | Message: Erro ao inserir comentário na timeline do negócio",
                     400

                     )
                  
                     return response
           
              return {
                 
                 "status":True,
                 "statusCode":200,
                 "message":"Envelope anulado com sucesso!"

                 }

       case _:

              handleErrorIntegrationFields(dataTokenBitrix["token"],idDeal,"Tipo de evento solicitado desconhecido")

              dicValuesError = {
                    
                    "status":"notFoundEnvelopeEventType",
                     "reason":"Tipo de evento solicitado desconhecido",
                     "method":"processEnvelopeStateEvents"

                     }
                  
              notificationError(dataTokenBitrix["token"],idDeal,dicValuesError)

              handleErrorLogging(

                     idDeal,
                     "Status: notFoundEnvelopeEventType | Method: processEnvelopeStateEvents | Mensagem:Tipo de evento solicitado desconhecido",
                     400

                     )

              response = handleErrorResponse(
                     
                     "Status: notFoundEnvelopeEventType | Method: processEnvelopeStateEvents | Message: Tipo de evento solicitado desconhecido",
                     400

                     )
                  
              return response