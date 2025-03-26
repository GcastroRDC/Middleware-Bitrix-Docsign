from flask import jsonify
"""
Handle para tratar exceções dos blocos try/except gerados pelas funções do middleware

Name: handleErrorException
Params: 
dependencies: 
methods:

"""
def handleErrorException(statusCode,exception):

    messageExcept = {
                
                "message": exception,
                "statusCode":statusCode
            }
   
    return jsonify(messageExcept), statusCode