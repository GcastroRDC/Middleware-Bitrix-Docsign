import os
import json
from dotenv import load_dotenv

def getEnviroments():

    load_dotenv()

    ACCOUNTID = os.environ['accountID']
    DOCUMENTTEMPLATES = os.environ['documentTemplates']
    BRANDID = os.environ['brandID']
    SERVERKEY = os.environ['serverKey']
    SERVERCRT = os.environ['serverCrt']
    BASEURL = os.environ['baseUrl']

    # Converte a string JSON para um dicionário
    documentTemplates = json.loads(DOCUMENTTEMPLATES)

    dicEnviroments = {

            "ACCOUNTID":ACCOUNTID,
            "DOCUMENTTEMPLATES":documentTemplates,
            "BRANDID":BRANDID,
            "SERVERKEY":SERVERKEY,
            "SERVERCRT":SERVERCRT,
            "BASEURL":BASEURL
        }
    
    return dicEnviroments
