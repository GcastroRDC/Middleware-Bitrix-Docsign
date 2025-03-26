import requests
import logging
import os

# Obtém o diretório absoluto do script atual
diretorioAtual = os.path.dirname(os.path.abspath(__file__))

# Subir para a pasta raiz (dois níveis para sair de API/Bitrix)
raizProjeto = os.path.dirname(os.path.dirname(diretorioAtual))

# Cria o caminho completo para o arquivo de log dentro da pasta Logs
pathFileRepositoryLogs = os.path.join(raizProjeto, "logs", "repository.log")

# Configuração básica do logging
logging.basicConfig(

    filename=pathFileRepositoryLogs,# Diretório com o arquivo onde os logs serão salvos
    level=logging.ERROR,              # Define o nível de logging
    format='%(asctime)s - %(levelname)s - %(message)s'  # Formato da mensagem
)

def crmCompanyGet(tokenBitrix,idCompany,idDeal):

    endpointCrmCompanyGet = f"https://dominio.bitrix24.com.br/rest/crm.company.get?auth={tokenBitrix}"
    # Parâmetros da consulta, incluindo o ID da empresa
    params = {

        'ID': idCompany 
    }

    # Enviando a requisição GET para a API
    response = requests.get(endpointCrmCompanyGet, params=params)

    # Verificando o status da resposta
    if response.status_code == 200:
       
        company_data = response.json()
        
         # Verifica se a chave "result" existe e contém dados
        if 'result' in company_data:

            company_info = company_data['result']
            
            # Extraindo os campos específicos
            nome_empresa = company_info.get('TITLE', None)
            cnpj_empresa = company_info.get('UF_CRM_1649100163', None)
            numero_empresa = company_info.get('UF_CRM_1649099988', None)
            bairro_empresa = company_info.get('UF_CRM_1649100035', None)
            cep_empresa = company_info.get('UF_CRM_1649100017', None)
            endereco_empresa = company_info.get('UF_CRM_1649099949', None)
            representante_empresa = company_info.get('UF_CRM_6661AE50F14F3', None)
            email_representante = company_info.get('UF_CRM_1624303718', None)
            cpf_representante = company_info.get('UF_CRM_1730896486599', None)
            
            fieldsCompany = {

                'nome': nome_empresa,
                'cnpj': cnpj_empresa,
                'numero': numero_empresa,
                'bairro': bairro_empresa,
                'cep': cep_empresa,
                'endereco': endereco_empresa,
                'representante': representante_empresa,
                'emailRepresentante': email_representante,
                'cpfRepresentante': cpf_representante
            }

            # Array para armazenar as chaves com erros
            fieldsCompanyError = []
            
            # Percorre todos os campos
            for chave, valor in fieldsCompany.items():

                # Verifica se o valor está vazio ou é None
                if not valor or not str(valor).strip():

                    fieldsCompanyError.append(chave)  # Adiciona a chave ao array de erros  
            
            # Valida se o array "fieldsCompanyError" está vazio, caso sim significa que não temos campos com valores vazios ou nulos.
            if not fieldsCompanyError:

                return {

                    "status":True,
                    "values":fieldsCompany,
                    "type":"success"
                    }
            
            else:

    
                return {
                    "status":False,
                    "values":None,
                    "type":"empty"
                    }

        return {
            "status":False,
            "values":None,
            "type":"error"
            }

    else:
       
       return {
           "status":False,
           "values":None,
           "type":"error"
           }
