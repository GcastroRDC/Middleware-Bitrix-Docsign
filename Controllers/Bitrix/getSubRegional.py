def getSubRegional(idSubRegional):
    
    listSubRegional =  [

                {
                        
                    "ID": 17979,
                    "VALUE":"N1"
                },
                {
                    "ID": 17981,
                    "VALUE":"N2"
                },
                {
                    "ID": 17983,
                    "VALUE":"N3"
                },
                   {
                        
                    "ID": 17985,
                    "VALUE":"N4"
                },
                {
                    "ID": 17987,
                    "VALUE":"S1"
                },
                {
                    "ID": 17991,
                    "VALUE":"S2"
                },
                   {
                        
                    "ID": 36299,
                    "VALUE":"S3"
                },
                {
                    "ID": 36301,
                    "VALUE":"S4"
                },
                {
                    "ID": 36303,
                    "VALUE":"OPERADORAS NACIONAL"
                }
               
            ]

    for subRegional in listSubRegional:

        if subRegional["ID"] == int(idSubRegional):

            return subRegional["VALUE"]
        
    return None