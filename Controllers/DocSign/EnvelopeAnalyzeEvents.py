from Api.Bitrix.endpoints.crmTimelineCommentFile import crmTimelineCommentFile
from Api.Bitrix.endpoints.crmDealGetValues import crmDealGetValues
from Controllers.DocSign.getValueTabs import getValueTabs
from Handle.HandleEvents.handleEvents import handleEvents
from Api.Bitrix.endpoints.crmDealUpdate import crmDealUpdate
from Handle.HandleError.handleErrorResponse import handleErrorResponse
from Handle.HandleError.handleErrorLogging import handleErrorLogging
from Handle.HandleError.handleErrorIntegrationFields import handleErrorIntegrationFields
from Notification.notificationIntegracao.BitrixDocSign.routers.callbackConnect.notificationEnvelopeEvents import notificationEnvelopeEvents
from Notification.notificationIntegracao.BitrixDocSign.routers.callbackConnect.notificationError import notificationError

def envelopeAnalyzeEvents(TokenBitrix, jsonEvent):

    statusEvent = jsonEvent["event"]
 
    match str(statusEvent):

       
        case "envelope-completed":
   
            dataValueTabs = getValueTabs(jsonEvent)
            if not dataValueTabs['status']:
                
                return {
                    
                    "status": False,
                    "type": "notFoundTabs",
                    "method":"envelopeAnalyzeEvents"
                }

            idDeal = dataValueTabs["idDeal"]
            allFiles = dataValueTabs["allFiles"]

            dataCrmDealGetValues = crmDealGetValues(TokenBitrix,idDeal)

            if not dataCrmDealGetValues["status"]:

                 return {
                     
                    "status":False,
                    "idDeal":idDeal,
                    "type":dataCrmDealGetValues["type"],
                    "method":"envelopeAnalyzeEvents"
                }
            
            clientType = dataCrmDealGetValues["values"]["clientType"]

            dataCrmTimelineFile = crmTimelineCommentFile(TokenBitrix, idDeal,clientType,allFiles)
            if not dataCrmTimelineFile["status"]:

                return {
                    
                    "status": False,
                    "idDeal":idDeal,
                    "type": "timelineCommentFileError",
                    "method":"envelopeAnalyzeEvents"
                }
            
            valuesFieldsDeal = {
                   
                   "UF_CRM_1733491181916":"envelope-completed",
                   "UF_CRM_1733491110611":"Assinatura do contrato concluida com sucesso",
                   "UF_CRM_1732412352707":"Concluida"
          
            }


            dataCrmDealUpdate = crmDealUpdate(TokenBitrix,idDeal,valuesFieldsDeal)
            
            if not dataCrmDealUpdate["status"]:

               handleErrorIntegrationFields(TokenBitrix,idDeal,"Erro ao atualizar os campos da integração o negócio")

               dicValuesError = {
                    
                    "status":400,
                     "reason":"Erro ao atualizar os campos da integração no negócio",
                     "method":"crmDealUpdate"

                     }
          
               notificationError(TokenBitrix,idDeal,dicValuesError)

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

            return {
                
                "status": True,
                "typeEvent": "envelope-completed",
                "idDeal":idDeal
 
            }

        case "envelope-voided":

            # Processa quando o envelope é Anulado (status voided)
            dataValueTabs = getValueTabs(jsonEvent)
            if not dataValueTabs['status']:
                return {

                    "status": False,
                    "type": "notFoundTabs",
                    "method":"envelopeAnalyzeEvents"
                }

            idDeal = dataValueTabs["idDeal"]

            voidedReason = "Contrato anulado por uma das partes!"
            dicVoidedValues ={

                "statusEvent":"Anulado",
                "reason":voidedReason


            }

            valuesFieldsDeal = {
                   
                   "UF_CRM_1733491181916":"envelope-voided",
                   "UF_CRM_1733491110611":"Contrato anulado",
                   "UF_CRM_1732412352707":"Anulado"
          
            }

            dataCrmDealUpdate = crmDealUpdate(TokenBitrix,idDeal,valuesFieldsDeal)
            
            if not dataCrmDealUpdate["status"]:

               handleErrorIntegrationFields(TokenBitrix,idDeal,"Erro ao atualizar os campos da integração o negócio")

               dicValuesError = {
                    
                    "status":400,
                     "reason":"Erro ao atualizar os campos da integração no negócio",
                     "method":"crmDealUpdate"

                     }
          
               notificationError(TokenBitrix,idDeal,dicValuesError)

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

            notificationEnvelopeEvents(TokenBitrix,idDeal,dicVoidedValues)

            response = handleEvents(idDeal,"Envelope Anulado",200,str(statusEvent))
           
            return response

        case "envelope-declined":
            # Processa quando o envelope é recusado (status declined)
            dataValueTabs = getValueTabs(jsonEvent)
            if not dataValueTabs['status']:
                return {
                    "status": False,
                    "type": "notFoundTabs",
                    "method":"envelopeAnalyzeEvents"
                }

            idDeal = dataValueTabs["idDeal"]
            declinedReason = "Contrato recusado por uma das partes!"

            dicDeclinedValues ={

                "statusEvent":"Recusado",
                "reason":declinedReason


            }

            valuesFieldsDeal = {
                   
                   "UF_CRM_1733491181916":"envelope-declined",
                   "UF_CRM_1733491110611":"Contrato recusado",
                   "UF_CRM_1732412352707":"Recusado"
          
            }

            dataCrmDealUpdate = crmDealUpdate(TokenBitrix,idDeal,valuesFieldsDeal)
            
            if not dataCrmDealUpdate["status"]:

               handleErrorIntegrationFields(TokenBitrix,idDeal,"Erro ao atualizar os campos da integração o negócio")

               dicValuesError = {
                    
                    "status":400,
                     "reason":"Erro ao atualizar os campos da integração no negócio",
                     "method":"crmDealUpdate"

                     }
          
               notificationError(TokenBitrix,idDeal,dicValuesError)

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


            notificationEnvelopeEvents(TokenBitrix,idDeal,dicDeclinedValues)
            response = handleEvents(idDeal,"Envelope Recusado",200,str(statusEvent))

            return response

       
        case _:

             # Processa quando o envelope é recusado (status declined)
            dataValueTabs = getValueTabs(jsonEvent)
            if not dataValueTabs['status']:
                return {
                    "status": False,
                    "type": "notFoundTabs",
                    "method":"envelopeAnalyzeEvents"
                }

            idDeal = dataValueTabs["idDeal"]

            dicEventValues ={

                "statusEvent":"unknown",
                "reason":f"Evento desconhecido do envelope | Tipo Evento: {str(statusEvent)}",
                "method":"envelopeAnalyzeEvents"

            }

            notificationError(TokenBitrix,idDeal,dicEventValues)
            response =  handleEvents(idDeal,"Evento desconhecido do envelope",400,"unknown")
            
            return response
