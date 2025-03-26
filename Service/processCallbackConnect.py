from Controllers.DocSign.AnalyzeEventsCallbackConnect import AnalyzeEventsCallbackConnect
from Security.Authorization.accessPermissionVerify import accessPermissionVerify
from Api.Bitrix.token.getTokenApiBitrix import getTokenApiBitrix
from Notification.notificationIntegracao.BitrixDocSign.routers.callbackConnect.notificationSuccess import notificationSuccess
from Handle.HandleError.handleErrorResponse import handleErrorResponse
from Handle.HandleError.handleErrorLogging import handleErrorLogging
from Handle.HandleError.handleMultipleErrors import handleMultipleErrors
from Handle.HandleError.handleErrorIntegrationFields import handleErrorIntegrationFields

def processCallbackConnect(tokenRequest,jsonEvent):
        
         # Validação da Autorização de Acesso
        dataAuthorization = accessPermissionVerify(tokenRequest)
        if not dataAuthorization['status']:
            
            handleErrorLogging(
                 
                 None,dataAuthorization['message'],
                 dataAuthorization['codeErro']

                 )
            
            response = handleErrorResponse(
                 
                 dataAuthorization['message'],
                401

                 )
            
            return response
        
         # Token API REST Bitrix24
        dataTokenBitrix = getTokenApiBitrix()
        if not dataTokenBitrix["status"]:

            handleErrorLogging(
                 
                 None,
                 "Status: Error | Method: getTokenApiBitrix | Mensagem: Erro na geração do token da API Bitrix24",
                 401

                 )
            
            response = handleErrorResponse(
                 
                 "Status: Error | Method: getTokenApiBitrix | Message: Erro na geração do token da API Bitrix24",
                 401

                 )

            return response
        
        dataEventsCallbackConnect = AnalyzeEventsCallbackConnect(dataTokenBitrix["token"],jsonEvent)
     
        # Eventos de Envelope follow up
        statusEventsFollowUp = [
               
               "envelope-voided",
               "envelope-declined",
               "recipient-completed",
               "recipient-declined",
               "recipient-voided",
               "recipient-finish-later",
               "unknown"
               ]
        
        #Evento de conclusão do envelope
        if dataEventsCallbackConnect["status"] and dataEventsCallbackConnect["typeEvent"] == "envelope-completed":
          
            notificationSuccess(
                    
                    dataTokenBitrix["token"],
                    dataEventsCallbackConnect["idDeal"]

                    )
               
            return {
                    
                         "status":True,
                         "statusCode":200,
                         "message":"Assinatura do contrato concluida com sucesso!"

                         }
               
        # Eventos do envelope/recipient para notificação de ações do envelope
        if dataEventsCallbackConnect["status"] and dataEventsCallbackConnect["typeEvent"] in statusEventsFollowUp:
               
                return {
                    
                         "status":True,
                         "statusCode":200,
                         "message":f"Tipo Evento:{dataEventsCallbackConnect['typeEvent']} | Evento Follow-Up"

                         }
        if "idDeal" in dataEventsCallbackConnect:
                
                
                handleErrorIntegrationFields(dataTokenBitrix["token"],dataEventsCallbackConnect["idDeal"],"Erro no processamento dos eventos do callback Connect")
                response = handleMultipleErrors(
               
                        method={
                                
                                "token":dataTokenBitrix["token"],
                                "idDeal":dataEventsCallbackConnect["idDeal"],
                                "router":"callback.connect",
                                "name":"AnalyzeEventsCallbackConnect",
                                "errorType":dataEventsCallbackConnect["type"],
                                "method":dataEventsCallbackConnect["method"]
                           
                               }
                 )

                return response
        
        
        response = handleMultipleErrors(
               
                 method={
                        
                        "token":dataTokenBitrix["token"],
                        "idDeal":None,
                        "router":"callback.connect",
                        "name":"AnalyzeEventsCallbackConnect",
                        "errorType":dataEventsCallbackConnect["type"],
                        "method":dataEventsCallbackConnect["method"]
                   
                       }
             )
        
        return response
        
   
             

            

        

        
             




