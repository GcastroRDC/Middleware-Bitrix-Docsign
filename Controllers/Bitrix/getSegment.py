
def getSegment(idSegment):

  
    listSegments =  [
                {
                    "ID": 12414,
                    "VALUE": "Corporativo"
                },
                {
                    "ID": 12422,
                    "VALUE": "ISP"
                },
                {
                    "ID": 12424,
                    "VALUE": "Operadoras"
                },
                {
                    "ID": 17491,
                    "VALUE": "Governo"
                }
            ]

    for segment in listSegments:

        if segment["ID"] == int(idSegment):
 
            return segment["VALUE"]

   
    return None