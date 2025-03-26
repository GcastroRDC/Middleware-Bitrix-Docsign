from Handle.HandleError.handleErrorResponse import handleErrorResponse
from Handle.HandleError.handleErrorLogging import handleErrorLogging
from Notification.notificationIntegracao.BitrixDocSign.routers.callbackConnect.notificationError import notificationError
from Notification.notificationIntegracao.BitrixDocSign.routers.createEnvelope.notificationError import notificationError
from Notification.notificationIntegracao.BitrixDocSign.routers.envelopeStatesEvents.notificationError import notificationError
from Notification.notificationIntegracao.BitrixDocSign.routers.createEnvelope.notificationErrorEmptyFields import notificationErrorEmptyFields

"""
Handle para tratar múltiplos erros de uma mesma função do middleware
Name: handleMultipleErrors
Params: **kwargs
dependencies: handleErrorResponse e handleErrorLogging
methods:handleErrorLogging e handleErrorResponse

"""
def handleMultipleErrors(**kwargs):

    for key,value in kwargs.items():

            if value["router"] == "create.envelope":

                if value["name"] == "crmDealGetAll":

                    match str(value["errorType"]):

                        case "error":

                            dicValuesError = {

                                    "status":"Error",
                                    "reason":"Erro ao consultar dados do negócio.",
                                    "method":"crmDealGetAll"
                                }
                            
                            if value["idDeal"]:
                            
                                notificationError(value["token"],value["idDeal"],dicValuesError)

                            handleErrorLogging(None,"Status: Error | Method: crmDealGetAll | Mensagem: Erro ao consultar dados do negócio.",400)
                            response = handleErrorResponse("Status: Error | Method: crmDealGetAll | Mensagem: Erro ao consultar dados do negócio.", 400)

                            return response
                    
                        case "notFoundDealValues":

                            dicValuesError = {

                                    "status":"notFoundDealValues",
                                    "reason":"Dados do negócio não encontrados.",
                                    "method":"crmDealGetAll"
                                }
                            
                            if value["idDeal"]:
                            
                                notificationError(value["token"],value["idDeal"],dicValuesError)
                                
                            handleErrorLogging(None,"Status: notFoundDealValues | Method: crmDealGetAll | Mensagem: Dados do negócio não encontrados.",400)
                            response = handleErrorResponse("Status: notFoundDealValues | Method: crmDealGetAll | Mensagem: Dados do negócio não encontrados.", 400)

                            return response
                        
                        case "emptyFields":

                            dicValuesError = {

                                    "status":"emptyFields",
                                    "reason":"Foram enviados campos do negócio com valor vazio obrigatórios na elaboração do contrato.",
                                    "method":"crmDealGetAll",
                                    "fields":value["fieldsError"]
                                }
                            
                            if value["idDeal"]:
                                
                                notificationErrorEmptyFields(value["token"],value["idDeal"],dicValuesError)

                            handleErrorLogging(value["idDeal"],"Status: emptyFields | Method: crmDealGetAll | Mensagem: Foram enviados campos do negócio com valor vazio obrigatórios na elaboração do contrato.",400)
                            response = handleErrorResponse("Status: emptyFields | Method: crmDealGetAll | Mensagem: Foram enviados campos do negócio com valor vazio obrigatórios na elaboração do contrato.", 400)

                            return response
                        
                        case _:

                            dicValuesError = {

                                    "status":"unknown",
                                    "reason":"Erro desconhecido ao consultar dados do negócio",
                                    "method":"crmDealGetAll"
                                }

                            if value["idDeal"]:
                                
                                notificationError(value["token"],value["idDeal"],dicValuesError)

                            handleErrorLogging(value["idDeal"],"Status: unknown | Method: crmDealGetAll | Mensagem:Erro desconhecido ao consultar dados do negócio",400)
                            response = handleErrorResponse("Status: unknown | Method: crmDealGetAll | Mensagem:Erro desconhecido ao consultar dados do negócio", 400)

                            return response
                
                        
                if value["name"] == "envelopeSchemeBuilder":

                    match value["errorType"]:
                        
                        case "notFoundSalesManager":

                            dicValuesError = {

                                    "status":"notFoundSalesManager",
                                    "reason":"Dados do Gerente de Vendas B2B não encontrado.",
                                    "method":"envelopeSchemeBuilder"
                                }
                            
                            if value["idDeal"]:
                                
                                notificationError(value["token"],value["idDeal"],dicValuesError)
                            
                            handleErrorLogging(value["idDeal"],"Status: notFoundSalesManager | Method: envelopeSchemeBuilder | Mensagem: Dados do Gerente de Vendas B2B não encontrado.",400)
                            response = handleErrorResponse("Status: notFoundSalesManager | Method: envelopeSchemeBuilder | Mensagem: Dados do Gerente de Vendas B2B não encontrado.", 400)

                            return response
                        
                        case "notFoundExecutiveManager":

                            dicValuesError = {

                                    "status":"notFoundExecutiveManager",
                                    "reason":" Dados do Gerente Executivo de Vendas não encontrado.",
                                    "method":"envelopeSchemeBuilder"
                                }
                            
                            if value["idDeal"]:
                                
                                notificationError(value["token"],value["idDeal"],dicValuesError)
                            
                            handleErrorLogging(value["idDeal"],"Status: notFoundExecutiveManager | Method: envelopeSchemeBuilder | Mensagem: Dados do Gerente Executivo de Vendas não encontrado.",400)
                            response = handleErrorResponse("Status: notFoundExecutiveManager | Method: envelopeSchemeBuilder | Mensagem: Dados do Gerente Executivo de Vendas não encontrado.", 400)

                            return response
                        
                        
                        case "NotFoundGroupSignature":

                            dicValuesError = {

                                    "status":"NotFoundGroupSignature",
                                    "reason":"Grupo de participantes da alçada de assinaturas não encontrado.",
                                    "method":"envelopeSchemeBuilder"
                                }

                            if value["idDeal"]:
                                
                                notificationError(value["token"],value["idDeal"],dicValuesError)
                            
                            handleErrorLogging(value["idDeal"],"Status: NotFoundGroupSignature | Method: envelopeSchemeBuilder | Mensagem: Grupo da alçada de assinaturas não identificado",400)
                            response = handleErrorResponse("Status: NotFoundGroupSignature | Method: envelopeSchemeBuilder | Mensagem: Grupo da alçada de assinaturas não identificado", 400)

                            return response
                        
                        case "notFoundIdTemplate":

                            dicValuesError = {

                                    "status":"notFoundIdTemplate",
                                    "reason":"ID do modelo a ser enviado no envelope não foi encontrado.",
                                    "method":"envelopeSchemeBuilder"
                                }

                            if value["idDeal"]:
                                
                                notificationError(value["token"],value["idDeal"],dicValuesError)
                            
                            handleErrorLogging(value["idDeal"],"Status: notFoundIdTemplate | Method: envelopeSchemeBuilder | Mensagem: ID do modelo a ser enviado no envelope não foi encontrado.",400)
                            response = handleErrorResponse("Status: notFoundIdTemplate | Method: envelopeSchemeBuilder | Mensagem: ID do modelo a ser enviado no envelope não foi encontrado.", 400)

                            return response
                        
                        case "errorFinalScheme":

                            dicValuesError = {

                                    "status":"errorFinalScheme",
                                    "reason":"Erro na construção do scheme final do envelope.",
                                    "method":"envelopeSchemeBuilder"
                                }
                                
                            
                            if value["idDeal"]:
                                
                                notificationError(value["token"],value["idDeal"],dicValuesError)
                            
                            handleErrorLogging(value["idDeal"],"Status: errorFinalScheme | Method: envelopeSchemeBuilder | Mensagem:  Erro na construção do scheme final do envelope.",400)
                            response = handleErrorResponse("Status: errorFinalScheme | Method: envelopeSchemeBuilder | Mensagem:  Erro na construção do scheme final do envelope.", 400)

                            return response
                        
                        case _:

                            dicValuesError = {

                                    "status":"unknown",
                                    "reason":"Erro desconhecido na construção do envelope.",
                                    "method":"envelopeSchemeBuilder"
                                }
                            
                            if value["idDeal"]:
                                
                                notificationError(value["token"],value["idDeal"],dicValuesError)
                            
                            handleErrorLogging(value["idDeal"],"Status: unknown | Method: envelopeSchemeBuilder | Mensagem: Erro desconhecido na construção do envelope.",400)
                            response = handleErrorResponse("Status: unknown | Method: envelopeSchemeBuilder | Mensagem: Erro desconhecido na construção do envelope.", 400)

                            return response
                
                else:
                     
                    dicValuesError = {

                                        "status":"errorMethodNotIdentified",
                                        "reason":f"Método:{value['name']} | Método não identificado na rota {value['router']} para tratar o erro da integração.",
                                        "method":"handleMultipleErrors"
                                    }
                    
                    if value["idDeal"]:
                        
                        notificationError(value["token"],value["idDeal"],dicValuesError)

                    handleErrorLogging(value["idDeal"],f"Status: errorMethodNotIdentified | Method: handleMultipleErrors | Mensagem: Método não identificado na rota {value['router']} para tratar o erro da integração.",400)
                    response = handleErrorResponse(f"Status: errorMethodNotIdentified | Method: handleMultipleErrors | Mensagem: Método não identificado na rota {value['router']} para tratar o erro da integração.", 400)

                    return response
            
            if value["router"] == "callback.connect":

                if value["name"] == "analyzeEventsCallbackConnect": 

                    match value["errorType"]:

                        case "notFoundTabs":
                            
                            handleErrorLogging(value["idDeal"],f"Status: notFoundTabs | Method: {value['method']} | Mensagem: Não foi possível extrair as tabs da estrutura de dados do evento do Callback Connect",400)
                            response = handleErrorResponse(f"Status: notFoundTabs | Method: {value['method']} | Mensagem: Não foi possível extrair as tabs da estrutura de dados do evento do Callback Connect", 400)

                            return response
                        
                        case "timelineCommentError":

                            if value["idDeal"]:

                                dicValuesError = {

                                    "status":"timelineCommentError",
                                    "reason":"Erro ao inserir o comentário na timeline do negócio",
                                    "method":value['method']
                                }
 
                                notificationError(value["token"],value["idDeal"],dicValuesError)

                                handleErrorLogging(value["idDeal"],f"Status: timelineCommentError | Method: {value['method']} | Mensagem: Erro ao inserir o comentário na timeline do negócio.",400)
                                response = handleErrorResponse(f"Status: timelineCommentError | Method: {value['method']} | Mensagem: Erro ao inserir o comentário na timeline do negócio.", 400)

                                return response
                            
                            handleErrorLogging(value["idDeal"],f"Status: timelineCommentError | Method: {value['method']} | Mensagem: Erro ao inserir o comentário na timeline do negócio.",400)
                            response = handleErrorResponse(f"Status: timelineCommentError | Method: {value['method']} | Mensagem: Erro ao inserir o comentário na timeline do negócio.", 400)

                            return response
                        
                        case "notFoundTypeEvent":

                                dicValuesError = {

                                    "status":"notFoundTypeEvent",
                                    "reason":"Tipo de Evento não identificado",
                                    "method":value['method']
                                }

                                if value["idDeal"]:
                                    
                                    notificationError(value["token"],value["idDeal"],dicValuesError)

                                handleErrorLogging(value["idDeal"],f"Status: notFoundTypeEvent | Method: {value['method']} | Mensagem: Tipo de Evento não identificado",400)
                                response = handleErrorResponse(f"Status: notFoundTypeEvent | Method: {value['method']} | Mensagem: Tipo de Evento não identificado", 400)

                                return response
                        
                        case "notFoundRecipient":

                                dicValuesError = {

                                    "status":"notFoundRecipient",
                                    "reason":"Destinatário não identificado",
                                    "method":value['method']
                                }

                                if value["idDeal"]:
                                    
                                    notificationError(value["token"],value["idDeal"],dicValuesError)

                                handleErrorLogging(value["idDeal"],f"Status: notFoundRecipient | Method: {value['method']} | Mensagem: Destinatário não identificado",400)
                                response = handleErrorResponse(f"Status: notFoundRecipient | Method: {value['method']} | Mensagem: Destinatário não identificado", 400)

                                return response
                        
                        case "error":

                            dicValuesError = {

                                    "status":"Error",
                                    "reason":"Erro ao consultar dados do negócio.",
                                    "method":"crmDealGetValues"
                                }
                            
                            if value["idDeal"]:
                                
                                notificationError(value["token"],value["idDeal"],dicValuesError)

                            handleErrorLogging(value["idDeal"],"Status: Error | Method: crmDealGetValues | Mensagem: Erro ao consultar dados do negócio.",400)
                            response = handleErrorResponse("Status: Error | Method: crmDealGetValues | Mensagem: Erro ao consultar dados do negócio.", 400)

                            return response
                    
                        case "notFoundDealValues":

                            dicValuesError = {

                                    "status":"notFoundDealValues",
                                    "reason":"Dados do negócio não encontrados.",
                                    "method":"crmDealGetValues"
                                }
                            
                            if value["idDeal"]:
                                
                                notificationError(value["token"],value["idDeal"],dicValuesError)

                            handleErrorLogging(value["idDeal"],"Status: notFoundDealValues | Method: crmDealGetValues | Mensagem: Dados do negócio não encontrados.",400)
                            response = handleErrorResponse("Status: notFoundDealValues | Method: crmDealGetValues | Mensagem: Dados do negócio não encontrados.", 400)

                            return response
                        
                        case "emptyFields":

                            dicValuesError = {

                                    "status":"emptyFields",
                                    "reason":"Dados consultados do envelope estão nulos ou vazios.",
                                    "method":"crmDealGetValues"
                                }

                            if value["idDeal"]:
                                
                                notificationError(value["token"],value["idDeal"],dicValuesError)

                            handleErrorLogging(value["idDeal"],"Status: emptyFields | Method: crmDealGetValues | Mensagem: Dados consultados do envelope estão nulos ou vazios.",400)
                            response = handleErrorResponse("Status: emptyFields | Method: crmDealGetValues | Mensagem: Dados consultados do envelope estão nulos ou vazios.", 400)

                            return response
                        
                        case "terminateWorkflowError":

                            dicValuesError = {

                                    "status":"terminateWorkflowError",
                                    "reason":"Erro ao terminar o fluxo de trabalho ativo.",
                                    "method":value['method']
                                }
                                
                            
                            if value["idDeal"]:
                                
                                notificationError(value["token"],value["idDeal"],dicValuesError)

                            handleErrorLogging(value["idDeal"],f"Status: terminateWorkflowError | Method: {value['method']} | Mensagem: Erro ao terminar o fluxo de trabalho ativo.",400)
                            response = handleErrorResponse(f"Status: terminateWorkflowError | Method: {value['method']} | Mensagem: Erro ao terminar o fluxo de trabalho ativo.", 400)

                            return response
                        
                      
                        case _:

                            if value["idDeal"]:

                                dicValuesError = {

                                    "status":"unknown",
                                    "reason":"Evento desconhecido",
                                    "method":{value['method']}
                                }

                                notificationError(value["token"],value["idDeal"],dicValuesError)

                                handleErrorLogging(value["idDeal"],f"Status: unknown | Method: {value['method']} | Mensagem: Evento desconhecido",400)
                                response = handleErrorResponse(f"Status: unknown | Method: {value['method']} | Mensagem: Evento desconhecido", 400)

                                return response

                            handleErrorLogging(value["idDeal"],f"Status: unknown | Method: {value['method']} | Mensagem:  Evento não identificado",400)
                            response = handleErrorResponse(f"Status: unknown | Method: {value['method']} | Mensagem:  Evento não identificado", 400)

                            return response

               
            if value["router"] == "envelope.state.events":
                
                if value["name"] == "crmDealGetValues":
                        
                        match value["errorType"]:
                            
                            case "error":

                                dicValuesError = {

                                        "status":"Error",
                                        "reason":"Erro ao consultar dados do negócio.",
                                        "method":"crmDealGetValues"
                                    }
                                
                                if value["idDeal"]:
                                    
                                    notificationError(value["token"],value["idDeal"],dicValuesError)

                                handleErrorLogging(value["idDeal"],"Status: Error | Method: crmDealGetValues | Mensagem: Erro ao consultar dados do negócio.",400)
                                response = handleErrorResponse("Status: Error | Method: crmDealGetValues | Mensagem: Erro ao consultar dados do negócio.", 400)

                                return response
                            
                            case "notFoundDealValues":

                                dicValuesError = {

                                        "status":"notFoundDealValues",
                                        "reason":"Dados do negócio não encontrados.",
                                        "method":"crmDealGetValues"
                                    }
                                
                                if value["idDeal"]:
                                    
                                    notificationError(value["token"],value["idDeal"],dicValuesError)

                                handleErrorLogging(value["idDeal"],"Status: notFoundDealValues | Method: crmDealGetValues | Mensagem: Dados do negócio não encontrados.",400)
                                response = handleErrorResponse("Status: notFoundDealValues | Method: crmDealGetValues | Mensagem: Dados do negócio não encontrados.", 400)

                                return response

                            case "emptyFields":

                                dicValuesError = {

                                        "status":"emptyFields",
                                        "reason":"Dados consultados do envelope estão nulos ou vazios.",
                                        "method":"crmDealGetValues"
                                    }
                                
                                if value["idDeal"]:
                                    
                                    notificationError(value["token"],value["idDeal"],dicValuesError)

                                handleErrorLogging(value["idDeal"],"Status: emptyFields | Method: crmDealGetValues | Mensagem: Dados consultados do envelope estão nulos ou vazios.",400)
                                response = handleErrorResponse("Status: emptyFields | Method: crmDealGetValues | Mensagem: Dados consultados do envelope estão nulos ou vazios.", 400)

                                return response
                             
                            case _:  

                                dicValuesError = {

                                        "status":"unknown",
                                        "reason":"Erro desconhecido ao consultar dados do negócio",
                                        "method":"crmDealGetValues"
                                    }
                                
                                if value["idDeal"]:
                                    
                                    notificationError(value["token"],value["idDeal"],dicValuesError)

                                handleErrorLogging(value["idDeal"],"Status: unknown | Method: crmDealGetValues | Mensagem: Erro desconhecido ao consultar dados do negócio",400)
                                response = handleErrorResponse("Status: unknown | Method: crmDealGetValues | Mensagem: Erro desconhecido ao consultar dados do negócio", 400)

                                return response
                            
                if value["name"] == "envelopeDeclined":

                    mensagem = None
                  
                    match str(value["errorType"]):
                        
                        case "statusNotAllowed":
                              
                              mensagem = "Status do envelope não permitido pra anulação."

                        case "error":
                              
                              mensagem = "Erro ao anular o envelope."

                        case "statusVoided":
                              
                              mensagem = "Não é possivel anular um envelope com status de anulado. Verifique se não está tentando anular um envelope que já tenha sido dado como anulado."

                        case "statusDeclined":
                              
                              mensagem = "Não é possivel anular um envelope com status de recusado. Verifique se não está tentando anular um envelope que já tenha sido dado como recusado."

                        case "envelopeIdEmpty":
                              
                               mensagem = "O campo 'Envelope ID' está vazio e é obrigatório para anulação do envelope. Isso pode ter ocorrido por falha ou instabilidade na integração no momento da criação do envelope."
                        
                        case _:  

                                mensagem = "Erro desconhecido ao tentar anular o envelope."
            
                    dicValuesError = {
                        
                        "status":400,
                        "reason":mensagem,
                        "method":"envelopeDeclined"
                        
                        }
                    
                    if value["idDeal"]:
                        
                        notificationError(value["token"],value["idDeal"],dicValuesError)

                    handleErrorLogging(

                        value["idDeal"],
                        "Status: Error | Method: envelopeDeclined | Mensagem: {} ".format(mensagem),
                        400

                        )
                    response = handleErrorResponse(
                        
                        "Status: Error | Method: envelopeDeclined | Message: {} ".format(mensagem),
                        400

                        )
                    
                    return response
                
                else:
                     
                    dicValuesError = {

                                        "status":"errorMethodNotIdentified",
                                        "reason":f"Método:{value['name']} | Método não identificado na rota {value['router']} para tratar o erro da integração.",
                                        "method":"handleMultipleErrors"
                                    }

                    if value["idDeal"]:
                        
                        notificationError(value["token"],value["idDeal"],dicValuesError)
    
                    response = handleErrorResponse(f"Status: errorMethodNotIdentified | Method: handleMultipleErrors | Mensagem: Método não identificado na rota {value['router']} para tratar o erro da integração.", 400)
    
                    return response
            
            else:
                 
                dicValuesError = {

                                        "status":"errorRouteNotIdentified",
                                        "reason":f"Rota: {value['router']} | Rota não identificada para tratar o erro da integração.",
                                        "method":"handleMultipleErrors"
                                    }
                if value["idDeal"]:
                    
                    notificationError(value["token"],value["idDeal"],dicValuesError)
                    
                response = handleErrorResponse("Status: errorRouteNotIdentified | Method: handleMultipleErrors | Mensagem: Rota não identificada para tratar o erro da integração.", 400)

                return response
                 
                

                
        
            

            

                     



                    
                    

