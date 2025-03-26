import requests
import os
from dotenv import load_dotenv

load_dotenv()

info_appLocal = (f'{os.environ["clientId"]}',f'{os.environ["clientSecrety"]}')
client_id,secret_id = info_appLocal

endpoint = 'http://dominio.bitrix24.com.br/oauth/token/?'

diretorio = os.path.dirname(os.path.abspath(__file__))

# Caminho completo para o arquivo refreshToken.txt
pathFileRefreshToken = os.path.join(diretorio, "refreshToken.txt")

def getTokenApiBitrix():
            
            with open(pathFileRefreshToken,"r") as arquivo:
                       
                       refresh_token_Base = arquivo.read() 
            
            endpointAuth = f'{endpoint}client_id={client_id}&grant_type=refresh_token&client_secret={secret_id}&refresh_token={refresh_token_Base}' 

            response = requests.get(endpointAuth)

            if response.status_code == 200:

                data = response.json()

                with open(pathFileRefreshToken, "w") as arquivo:
                        
                        arquivo.write(data['refresh_token'])

                return print({
                        "status":True,
                        "token":data['access_token']
                        })
            
            return {
                    "status":False,
                    "token":None
                    }


