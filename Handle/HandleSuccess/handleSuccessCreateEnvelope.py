from flask import  jsonify

def handleSuccessCreateEnvelope(status,statusCode,message):

    messageSuccess = {
                
                "status": status,
                "message": message,
                "statusCode":statusCode
            }

    return jsonify(messageSuccess), statusCode