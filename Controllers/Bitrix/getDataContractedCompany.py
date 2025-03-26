def getDataContractedCompany(companyName):

    listDataComapny =  [
                {
                    "NOME": "NOME EMPRESA",
                    "CNPJ": "CNPJ EMPRESA",
                    "ENDERECO":"ENDEREÇO EMPRESA",
                    "NUMERO":"NUMERO EMPRESA",
                    "BAIRRO":"BAIRRO EMPRESA",
                    "CIDADE":"CIDADE EMPRESA",
                    "CEP":"CEP EMPRESA",
                    "TELEFONE":"TELEFONE EMPRESA",
                    "EMAIL":"EMAIL EMPRESA"
                   

                },
                {
                   
                    "NOME": "NOME EMPRESA",
                    "CNPJ": "CNPJ EMPRESA",
                    "ENDERECO":"ENDEREÇO EMPRESA",
                    "NUMERO":"NUMERO EMPRESA",
                    "BAIRRO":"BAIRRO EMPRESA",
                    "CIDADE":"CIDADE EMPRESA",
                    "CEP":"CEP EMPRESA",
                    "TELEFONE":"TELEFONE EMPRESA",
                    "EMAIL":"EMAIL EMPRESA"

                }
                
            ]
    
    for company in listDataComapny:

        if company["NOME"] == str(companyName):
            
            return {
                
                "status":True,
                "nome":company["NOME"],
                "cnpj":company["CNPJ"],
                "endereco":company["ENDERECO"],
                "numero":company["NUMERO"],
                "bairro":company["BAIRRO"],
                "cidade":company["CIDADE"],
                "cep":company["CEP"],
                "telefone":company["TELEFONE"],
                "email":company["EMAIL"]
            }

    
    return None