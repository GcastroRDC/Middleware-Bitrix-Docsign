import logging
import os


# Obtém o diretório atual
diretorio = os.path.dirname(os.path.abspath(__file__))

# Volta 2 pastas para alcançar a pasta "middleware"
diretorioMiddleware = os.path.join(diretorio, os.pardir, os.pardir)

# Cria o caminho completo para a pasta Logs
pathLogs = os.path.join(diretorioMiddleware, "Logs")

# Cria o caminho completo para o arquivo repository.log
pathFileRepositoryLogs = os.path.join(pathLogs, "repository.log")

# Configuração básica do logging
logging.basicConfig(

    filename=pathFileRepositoryLogs,# Diretório com o arquivo onde os logs serão salvos
    level=logging.ERROR,              # Define o nível de logging
    format='%(asctime)s - %(levelname)s - %(message)s'  # Formato da mensagem
)

"""
Handle para tratar os logs dos erros quando gerados pelas funções do middleware

Name: handleErrorLogging
Params: int:idDeal,str:message,int:statusCode
dependencies: Flask,logging e os
methods:jsonify,dirname,abspath,join,basicConfig,error

"""

def handleErrorLogging(idDeal, message, statusCode):

    if idDeal:

        logging.error(f"Deal:{idDeal} | Status Code:{statusCode}| Message: {message}")

    logging.error(f"Status Code:{statusCode}| Message: {message}")

    
