from Controllers.Bitrix.getSegment import getSegment
from Controllers.Bitrix.getSubRegional import getSubRegional

def getB2BSalesManager(idSegment,idSubRegion):


    SegmentName = getSegment(idSegment)
    subRegionalName = getSubRegional(idSubRegion)

    if SegmentName:

        match SegmentName:

            case "Corporativo" | "ISP" | "Governo":

                listManagersByRegion =  [

                            {
                                "ID": "N1",
                                "NAME": "NOME",
                                "EMAIL":"EMAIL"
                            },
                            {
                                "ID": "N2",
                                "NAME": "NOME",
                                "EMAIL":"EMAIL"
                            },

                             {
                                "ID": "N3",
                                "NAME": "NOME",
                                "EMAIL":"EMAIL"
                            },
                             {
                                "ID": "N4",
                                "NAME": "NOME",
                                "EMAIL":"EMAIL"
                            },
                             {
                                "ID": "S1",
                                "NAME": "NOME",
                                "EMAIL":"EMAIL"
                            },
                            {
                                "ID": "S2",
                                "NAME": "NOME",
                                "EMAIL":"EMAIL"
                            },
                            {
                                "ID": "S3",
                                "NAME": "NOME",
                                "EMAIL":"EMAIL"
                            },
                             {
                                "ID": "S4",
                                "NAME": "NOME",
                                "EMAIL":"EMAIL"
                            }
                            
                        
                        ]

                for manageRegion in listManagersByRegion:

                    if manageRegion["ID"] == str(subRegionalName):
                        
                        return {
                            
                            "status":True,
                            "name":manageRegion["NAME"],
                            "email":manageRegion["EMAIL"]
                

                            }
                return  {
                            
                            "status":False,
                            "name":None,
                            "email":None

                            }
            
           
            case "Operadoras":

                listManagersByRegion =  [

                            {
                                "ID": "OPERADORAS NACIONAL",
                                "NAME": "NOME",
                                "EMAIL":"EMAIL"
                            }
                           
                        
                        ]


                return {
                            
                            "status":True,
                            "name":manageRegion["NAME"],
                            "email":manageRegion["EMAIL"]
                

                            }
    
            
            
    return  {
                            
            "status":False,
            "name":None,
            "email":None

            }