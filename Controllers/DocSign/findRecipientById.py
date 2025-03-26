
def findRecipientById(recipientId,jsonEvent):

    for signer in jsonEvent["data"]["envelopeSummary"]["recipients"]["signers"]: 
           
            if signer["recipientId"] == recipientId:

                return {"status":True,"signer":signer}
            
    return  {"status":False,"signer":None}