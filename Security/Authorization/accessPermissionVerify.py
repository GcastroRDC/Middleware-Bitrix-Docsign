from dotenv import load_dotenv
import os

load_dotenv()
AUTHORIZATIONTOKEN = os.environ['AuthorizationToken']

def accessPermissionVerify(tokenRequest):

    tokenInvalidStates = [None,""]

    if tokenRequest in tokenInvalidStates:
          
          return {
               "status":False,
               "message":"Status: Error | Method: verifyAuthorization | Mensagem: Token Não Informado",
               "codeErro":401
               }
    
    elif tokenRequest != AUTHORIZATIONTOKEN:

        return {
             
             "status":False,
             "message":"Status: Error | Method: verifyAuthorization | Mensagem: Token Inválido",
             "codeErro":403

             }

    return {
         
         "status":True,
         "message":"Authorized authentication",
         "codeErro":200
         }
    
