from flask import  jsonify

def handleSuccessEnvelopeStatesEvents(status,statusCode,message):

    messageSuccess = {
                
                "status": status,
                "message": message
            }

    return jsonify(messageSuccess), statusCode