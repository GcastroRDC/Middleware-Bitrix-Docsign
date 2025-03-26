from Controllers.DocSign.getValueTabs import getValueTabs
from Handle.HandleEvents.handleEvents import handleEvents
from Api.Bitrix.endpoints.crmTimelineCommentFileClient import crmTimelineCommentFileClient
from Api.Bitrix.endpoints.crmDealGetValues import crmDealGetValues
from Api.Bitrix.endpoints.crmDealUpdate import crmDealUpdate
from Controllers.DocSign.findRecipientById import findRecipientById
from Api.Bitrix.endpoints.terminateWorkflow import terminateWorkflow
from Handle.HandleError.handleErrorResponse import handleErrorResponse
from Handle.HandleError.handleErrorLogging import handleErrorLogging
from Notification.notificationIntegracao.BitrixDocSign.routers.callbackConnect.notificationFollowUpEvents import notificationFollowUpEvents
from Notification.notificationIntegracao.BitrixDocSign.routers.callbackConnect.notificationSignatureClient import notificationSignatureClient
from Handle.HandleError.handleErrorIntegrationFields import handleErrorIntegrationFields
from Notification.notificationIntegracao.BitrixDocSign.routers.callbackConnect.notificationRecipientsEvents import notificationRecipientsEvents
from Notification.notificationIntegracao.BitrixDocSign.routers.callbackConnect.notificationError import notificationError

def recipientAnalyzeEvents(TokenBitrix, jsonEvent):

    statusEvent = jsonEvent["event"]
    recipientId = jsonEvent["data"]["recipientId"]

    match str(statusEvent):

        case "recipient-completed":
   
            dataValueTabs = getValueTabs(jsonEvent)
            if not dataValueTabs['status']:
                
                return {
                    
                    "status": False,
                    "type": "notFoundTabs",
                    "method":"recipientAnalyzeEvents"
                }
            

            idDeal = dataValueTabs["idDeal"]
            recipient = findRecipientById(recipientId,jsonEvent)

            if not recipient["status"]:
                return {
                    
                    "status": False,
                    "idDeal":idDeal,
                    "type": "notFoundRecipient",
                    "method":"recipientAnalyzeEvents"
                }
            
            # Verifica se a parte que concluiu a assinatura foi o "Cliente"
            if recipient['signer']['roleName'] == "Cliente":

                allFiles = dataValueTabs["allFiles"]

                dataCrmDealGetValues = crmDealGetValues(TokenBitrix,idDeal)

                if not dataCrmDealGetValues["status"]:

                    return {
                        
                        "status":False,
                        "idDeal":idDeal,
                        "type":dataCrmDealGetValues["type"],
                        "method":"recipientAnalyzeEvents"
                    }
                
                # Atualiza o campo "Contrato assinado pelo cliente? = SIM"
                valuesFieldsDeal = {
                   
                   "UF_CRM_1740662766":1,
                    
          
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
                

                clientType = dataCrmDealGetValues["values"]["clientType"]
                idFluxoTrabalhoAtivo = dataCrmDealGetValues["values"]["idFluxoTrabalhoAtivo"]

                dataCrmTimelineFile = crmTimelineCommentFileClient(TokenBitrix, idDeal,clientType,allFiles)

                if not dataCrmTimelineFile["status"]:

                        return {

                            "status": False,
                            "idDeal":idDeal,
                            "type": "timelineCommentFileError",
                            "method":"recipientAnalyzeEvents"
                        }
                    
                dataTerminateWorkflow = terminateWorkflow(TokenBitrix,idFluxoTrabalhoAtivo,idDeal)

                if not dataTerminateWorkflow["status"]:

                            return {

                            "status": False,
                            "idDeal":idDeal,
                            "type": "terminateWorkflowError",
                            "method":"recipientAnalyzeEvents"
                        }
                    
                dicRecipientValuesClient = {

                    "roleName":recipient['signer']['roleName'],
                    "name":recipient['signer']['name'],
                    "email":recipient['signer']['email'],
                    "reason":None

                        }
                    
                notificationSignatureClient(TokenBitrix,idDeal,dicRecipientValuesClient)
                        

            dicRecipientValues = {

                "roleName":recipient['signer']['roleName'],
                "name":recipient['signer']['name'],
                "email":recipient['signer']['email'],
                "reason":None
            }

            notificationFollowUpEvents(TokenBitrix,idDeal,dicRecipientValues)

            return handleEvents(

                idDeal,
                f"Role:{recipient['signer']['roleName']} | Name: {recipient['signer']['name']} | Envelope Assinado/Aprovado por Destinatário",
                200,
                str(statusEvent)

                )
            
        case "recipient-declined":

            # Processa quando o envelope é Anulado (status voided)
            dataValueTabs = getValueTabs(jsonEvent)
            if not dataValueTabs['status']:
                return {
                    "status": False,
                    "type": "notFoundTabs",
                    "method":"recipientAnalyzeEvents"
                }

            idDeal = dataValueTabs["idDeal"]
            recipient  = findRecipientById(recipientId,jsonEvent)

            if not recipient["status"]:

                return {
                    
                    "status": False,
                    "idDeal":idDeal,
                    "type": "notFoundRecipient",
                    "method":"recipientAnalyzeEvents"
                }
            
            declinedReason = recipient['signer']["declinedReason"]

            dicDeclinedValues ={

                "statusEvent":"Recusado",
                "roleName":recipient['signer']['roleName'],
                "name":recipient['signer']['name'],
                "email":recipient['signer']['email'],
                 "reason":declinedReason
                

            }

            notificationRecipientsEvents(TokenBitrix,idDeal,dicDeclinedValues)
           
            return handleEvents(
                          idDeal,
                         f"Role:{recipient['signer']['roleName']} | Name: {recipient['signer']['name']} | Envelope Recusado por Destinatário",
                         200,
                         str(statusEvent)
                         )
            
        case "recipient-voided":

            # Processa quando o envelope é recusado (status declined)
            dataValueTabs = getValueTabs(jsonEvent)
            if not dataValueTabs['status']:
                return {
                    "status": False,
                    "type": "notFoundTabs",
                    "method":"recipientAnalyzeEvents"
                }

            idDeal = dataValueTabs["idDeal"]
            recipient  = findRecipientById(recipientId,jsonEvent)
            
            if not recipient["status"]:
                return {
                    
                    "status": False,
                    "idDeal":idDeal,
                    "type": "notFoundRecipient",
                    "method":"recipientAnalyzeEvents"
                }
            voidedReason = recipient['signer']["voidedReason"] 

            dicVoidedValues ={

                "statusEvent":"Anulado",
                "roleName":recipient['signer']['roleName'],
                "name":recipient['signer']['name'],
                "email":recipient['signer']['email'],
                "reason":voidedReason
                

            }

            notificationRecipientsEvents(TokenBitrix,idDeal,dicVoidedValues)
           
            return handleEvents(

                          idDeal,
                         f"Role:{recipient['signer']['roleName']} | Name: {recipient['signer']['name']} | Envelope Anulado por Destinatário",
                         200,
                         str(statusEvent)
                         )
            
        case "recipient-finish-later":

               # Processa quando o envelope é recusado (status declined)
            dataValueTabs = getValueTabs(jsonEvent)
            if not dataValueTabs['status']:
                return {
                    "status": False,
                    "type": "notFoundTabs",
                    "method":"recipientAnalyzeEvents"
                }

            idDeal = dataValueTabs["idDeal"]
            recipient  = findRecipientById(recipientId,jsonEvent)
            if not recipient["status"]:
                return {
                    
                    "status": False,
                    "idDeal":idDeal,
                    "type": "notFoundRecipient",
                    "method":"recipientAnalyzeEvents"
                }
          
            dicFinishLaterValues = {

                "statusEvent":"Finalizar Mais tarde",
                "roleName":recipient['signer']['roleName'],
                "name":recipient['signer']['name'],
                "email":recipient['signer']['email'],
                "reason":"Desejo finalizar minha assinatura mais tarde."
                

            }

            notificationRecipientsEvents(TokenBitrix,idDeal,dicFinishLaterValues)
           
            return handleEvents(
                          idDeal,
                         f"Role:{recipient['signer']['roleName']} | Name: {recipient['signer']['name']} | Finalizar a Assinatura do Envelope Mais Tarde",
                         200,
                         str(statusEvent)
                         )
       
        case _:

            dicEventValues ={

                "statusEvent":"unknown",
                "reason":f"Evento desconhecido do destinatário | Tipo Evento: {str(statusEvent)}",
                "method":"recipientAnalyzeEvents"

            }

            notificationError(TokenBitrix,idDeal,dicEventValues)
            return handleEvents(idDeal,"Evento desconhecido do destinatário",400,"unknown")
