def getRegional(idRegional):
    
    listRegional =  [

                {
                        
                    "ID": 35931,
                    "VALUE":"NO/NE"
                },
                {
                    "ID": 35929,
                    "VALUE":"S/SE/C.OESTE"
                },
                {
                    "ID": 35945,
                    "VALUE":"OPERADORAS NACIONAL"
                }
               
            ]

    for regional in listRegional:

        if regional["ID"] == int(idRegional):

            return regional["VALUE"]
        
    return None