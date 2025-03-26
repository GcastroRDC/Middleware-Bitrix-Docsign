from Controllers.DocSign.EnvelopeAnalyzeEvents import envelopeAnalyzeEvents
from Controllers.DocSign.recipientAnalyzeEvents import recipientAnalyzeEvents

def AnalyzeEventsCallbackConnect(tokenBitrix,jsonEvent):

    event = jsonEvent["event"]
   
     # Identifica o tipo do evento
    if str(event).startswith("recipient-"):
          
          response = recipientAnalyzeEvents(tokenBitrix,jsonEvent)

          return response
     
    
    elif str(event).startswith("envelope-"):
            
          response = envelopeAnalyzeEvents(tokenBitrix,jsonEvent)
          
          return response


    else:
            return {
                  
                  "status":False,
                  "type":"notFoundTypeEvent",
                  "method":"AnalyzeEventsCallbackConnect",
                  "typeEvent":None
                  }
