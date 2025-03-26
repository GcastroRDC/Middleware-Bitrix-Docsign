from Controllers.DocSign.envelopeConfig  import GROUPFIRST, GROUPSECOND, GROUPTHIRD, GROUPFOURTH
import copy

# Função para preencher os dados de signatários apenas onde estão vazios
def fillSigners(schemeOrdered, approvalGroupName, variableApprovers,dataWitness):

    # Variável para armazenar os dados do grupo de aprovadores correspondente
    dataSigners = None

    # Variável para armazenar a lista "variableApprovers" após a filtragem e ordenamento dos itens.
    variableApproversFormatted = None
    
    
    # Valida e Verifica a qual grupo de alçada será utilizado
    if approvalGroupName:

        match approvalGroupName:

            case "firstGroup":

                
                variableApprovers = [item for item in variableApprovers if item["identificador"] != "N3 Pre Vendas"]
                
                variableApproversFormatted = variableApprovers

                dataSigners = copy.deepcopy(GROUPFIRST) 
                
            case "secondGroup":

                variableApprovers = [item for item in variableApprovers if item["identificador"] != "Gerente Vendas B2B"]
                item = variableApprovers.pop(2)  
                variableApprovers.insert(1, item) 

                variableApproversFormatted = variableApprovers
                dataSigners = copy.deepcopy(GROUPSECOND) 

            case "thirdGroup":

                identifieRemoved = ["Executivo Vendas", "Gerente Vendas B2B", "Gerente Executivo Comercial","N3 Pre Vendas"]
                variableApprovers = [item for item in variableApprovers if item["identificador"] not in identifieRemoved]
               
                variableApproversFormatted = variableApprovers
                dataSigners = copy.deepcopy(GROUPTHIRD)

            case "fourthGroup":

                identifieRemoved = ["Executivo Vendas", "Gerente Vendas B2B", "Gerente Executivo Comercial","N3 Pre Vendas"]
                variableApprovers = [item for item in variableApprovers if item["identificador"] not in identifieRemoved]
               
                variableApproversFormatted = variableApprovers

                variableApproversFormatted = variableApprovers
                dataSigners = copy.deepcopy(GROUPFOURTH) 

            case _:

                variableApproversFormatted = None
                dataSigners = None

        # Filtra apenas os elementos vazios em dataSigners (onde name ou email são vazios)
        emptySigners = [signer for signer in dataSigners if not signer["name"] or not signer["email"]]
        variableApproversFormatted = variableApproversFormatted[:len(emptySigners)]  # Ajusta o tamanho de variableApprovers para coincidir com os vazios

    
        # Verifica se o grupo foi encontrado e preenche os dados
        if dataSigners and variableApproversFormatted:
           
            # Itera sobre os itens de signers vazios (emptySigners)
            for i, emptySigner in enumerate(emptySigners):
            
                # Preenche o nome e email se estiverem vazios
                if i < len(variableApproversFormatted):

                    approver = variableApproversFormatted[i]

                    if not emptySigner["name"]:

                        emptySigner["name"] = approver.get("name", "")

                    if not emptySigner["email"]:
                        emptySigner["email"] = approver.get("email", "")

            # Preenche o scheme com os dados atualizados de 'dataSigners'
            for i, role in enumerate(schemeOrdered["templateRoles"]):

                if i < len(dataSigners):

                    signer = dataSigners[i]
                    
                    role["roleName"] = signer["roleName"]
                    role["name"] = signer["name"]
                    role["email"] = signer["email"]

            if dataWitness["status"]:

                for item in dataWitness["witness"]:

                    dataSigners.insert(4,item)

            return {"status": True,"dataGroupSigners":dataSigners,"finalScheme": schemeOrdered}

        
        return {"status": False,"dataGroupSigners":None,"finalScheme": None}
    
    
    return {"status": False,"dataGroupSigners":None,"finalScheme": None}
