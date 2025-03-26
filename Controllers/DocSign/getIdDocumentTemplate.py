def getIdDocumentTemplate(documentTemplates,clientType, groupSigners):

    # Verifica se o template existe
    if clientType in documentTemplates:

        # Itera sobre os itens dentro da lista
        for item in documentTemplates[clientType]:

            # Verifica se a chave existe dentro do item
            if groupSigners in item:
               
                return {"status":True,"IdTemplate":item[groupSigners]}
      
    return {"status":False,"IdTemplate":None}