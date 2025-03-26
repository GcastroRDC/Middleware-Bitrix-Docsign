import logging
import os
from Security.Authorization.maskTokenRequest import maskTokenRequest

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

def handleLogRequest(app,url):

    logger = logging.getLogger(app)

    maskedURL = maskTokenRequest(url)
    
    logger.info(f"Requisição Recebida: {maskedURL}")