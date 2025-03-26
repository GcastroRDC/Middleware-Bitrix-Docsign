def addTabsToAllSigners(schemeOrdered, tabsList):
    
   
     # Itera sobre cada signer (papel de assinatura) no esquema
    for signer in schemeOrdered["templateRoles"]:
        # Garante que o 'tabs' e 'textTabs' existam antes de adicionar
        if "tabs" not in signer:

            signer["tabs"] = {}
            
        if "textTabs" not in signer["tabs"]:

            signer["tabs"]["textTabs"] = []
        
        # Adiciona as tabs no 'textTabs' para cada signer
        for tab in tabsList:

            signer["tabs"]["textTabs"].append(tab)

    return schemeOrdered
