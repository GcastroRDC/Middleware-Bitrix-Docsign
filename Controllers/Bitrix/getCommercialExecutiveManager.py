from Controllers.Bitrix.getRegional import getRegional

def getCommercialExecutiveManager(idRegional):

    selectedRegional = getRegional(idRegional)

    if selectedRegional:

        listRegional =  [

                    {
                        "ID": "NO/NE",
                        "NAME": "NOME",
                        "EMAIL":"EMAIL"
                    },
                    {
                        "ID": "S/SE/C.OESTE",
                        "NAME": "NOME",
                        "EMAIL":"EMAIL"
                    },
                    {
                        "ID": "OPERADORAS NACIONAL",
                        "NAME": "NOME",
                        "EMAIL":"EMAIL"
                    }
                    
                    
                     
                ]

        for regional in listRegional:
            
            if regional["ID"] == str(selectedRegional):
                
                return {

                    "status":True,
                    "name":regional["NAME"],
                    "email":regional["EMAIL"]

                    }
        
        
        return {
                    "status":False,
                    "name":None,
                    "email":None

                    }
    
    
    return       {
                    "status":False,
                    "name":None,
                    "email":None

                    }