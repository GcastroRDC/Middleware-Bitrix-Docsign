import logging
import os
from flask import jsonify

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
    level=logging.INFO,              # Define o nível de logging
    format='%(asctime)s - %(levelname)s - %(message)s'  # Formato da mensagem
)

def handleEvents(idDeal, message, statusCode,typeEvent):

    if idDeal:

        logging.info(f"Deal:{idDeal} | TypeEvent:{typeEvent} | StatusCode:{statusCode}| Message: {message}")

    logging.info(f"TypeEvent:{typeEvent} | StatusCode:{statusCode}| Message: {message}")

    return {"status":True,"typeEvent":typeEvent}