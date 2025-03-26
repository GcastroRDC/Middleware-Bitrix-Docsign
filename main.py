from flask import Flask, jsonify,request
from Enviroments.getEnviroments import getEnviroments
from Security.Authorization.getToken import getToken
from Security.Authorization.accessPermissionVerify import accessPermissionVerify
from Service.processCreateEnvelope import processCreateEnvelope
from Service.processCallbackConnect import processCallbackConnect
from Service.processEnvelopeStateEvents import processEnvelopeStateEvents
from Handle.HandleError.handleErrorLogging import handleErrorLogging
from Handle.HandleLogs.handleLogRequest import handleLogRequest
from Handle.HandleError.handleErrorResponse import handleErrorResponse
from Handle.HandleSuccess.handleSuccessCreateEnvelope import handleSuccessCreateEnvelope
from Handle.HandleSuccess.handleSuccessCallbackConnect import handleSuccessCallbackConnect
from Handle.HandleSuccess.handleSuccessEnvelopeStatesEvents import handleSuccessEnvelopeStatesEvents

app = Flask(__name__)

dicEnviroments = getEnviroments()

# Criptografa as requisições que contém a chave antes de salvar nos Logs (Tratamento de dados sensiveis)
@app.before_request
def logRequest():
    
    handleLogRequest(__name__,request.url)
  
@app.route('/middleware/docsign/create.envelope', methods=['POST'])
def createEnvelope():


        idDeal = request.args.get('idDeal')
        tokenRequest = getToken(request)
       
        response = processCreateEnvelope(
                
                tokenRequest,
                idDeal,
                dicEnviroments
                )
       
        
        if response["statusCode"] != 200:
               
               return jsonify(response),response["statusCode"]
        
        return handleSuccessCreateEnvelope(
                
                    "Success",
                    response["statusCode"],
                    response["message"]

                    )
            
@app.route('/middleware/docsign/callback.connect', methods=['POST'])
def callbackConnect():
   
        tokenRequest = getToken(request)

        response = processCallbackConnect(tokenRequest,request.get_json())
        
        if response["statusCode"] != 200:
               
               return jsonify(response),response["statusCode"]

        return handleSuccessCallbackConnect(
              
                    "Success",
                     response["statusCode"],
                     response["message"]

                    )

@app.route('/middleware/docsign/envelope.state.events', methods=['POST'])
def envelopeStateEvents():
       
       idDeal = request.args.get('idDeal')
       tokenRequest = getToken(request)
       eventType = request.args.get('eventType')
       reason = request.args.get('reason')

       response = processEnvelopeStateEvents(

              idDeal,
              tokenRequest,
              dicEnviroments,
              eventType,
              reason

              )
 
       if response["statusCode"] != 200:
               
               return jsonify(response),response["statusCode"]
       
       return handleSuccessEnvelopeStatesEvents(
              
                    "Success",
                     response["statusCode"],
                     response["message"]

       )

# Rota para validação do funcionamento da aplicação na VM
@app.route('/middleware/docsign/healthcheck', methods=['GET'])
def healthcheck():
        
    tokenRequest = getToken(request)

    # Validação da Autorização de Acesso
    dataAuthorization = accessPermissionVerify(tokenRequest)
    if not dataAuthorization['status']:
          
          handleErrorLogging(
                 
                 None,
                 dataAuthorization['message'],
                 dataAuthorization['codeErro']

                 )
            
          response = handleErrorResponse(
                 
                 dataAuthorization['message'],
                 dataAuthorization['codeErro']

                 )
            
          return jsonify(response),response["statusCode"]
    
    return jsonify({"status": "success", "message": "Middleware is up and running!"}), 200
       
if __name__ == '__main__':
         
    app.run(
          ssl_context=(
          dicEnviroments["SERVERCRT"],
          dicEnviroments["SERVERKEY"]),
          host='0.0.0.0',
          port=443
          )
