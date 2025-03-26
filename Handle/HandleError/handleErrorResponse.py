from flask import jsonify

"""
Handle para tratar os erros quando gerados pelas funções do middleware

Name: handleError
Params: str:message,int:statusCode
dependencies: Flask
methods:jsonify

"""

def handleErrorResponse(message, statusCode):

   messageErrorResponse = {
                
                "message": message,
                "statusCode":statusCode
            }
   
   return messageErrorResponse