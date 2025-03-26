from flask import  jsonify

def handleSuccessCallbackConnect(status,statusCode,message):
 

    messageSuccess = {

                    "status": status,
                    "message": message
                }

    return jsonify(messageSuccess), statusCode