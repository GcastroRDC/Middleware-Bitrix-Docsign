from Controllers.DocSign.envelopeConfig import TARGET_GROUPFIRST,TARGET_GROUPSECOND,TARGET_GROUPTHIRD,TARGET_GROUPFOURTH

def GroupSignature(totalValue,contractTime):

    if 0 < int(contractTime) <= TARGET_GROUPFOURTH:

        match int(totalValue):

            case v if v <=  TARGET_GROUPFIRST:

                return{

                    "status":True,
                    "amountSigners":7,
                    "groupSigners":"firstGroup"
                   
                    }
            

            case v if TARGET_GROUPFIRST < v <= TARGET_GROUPSECOND:
                 
                
                 return{
                     
                    "status":True,
                    "amountSigners":8,
                    "groupSigners":"secondGroup"
                   
                    }

            case v if v >= TARGET_GROUPTHIRD:

             
                return{
                    
                    "status":True,
                    "amountSigners":8,
                    "groupSigners":"thirdGroup"
                   
                    }
            case _:
                 
                 print(f"Grupo Desconhecido:",totalValue,contractTime)
                 return{
                     
                    "status":False,
                    "amountSigners":0,
                    "groupSigners":None
                    
                    }
            
    
    return{
        
            "status":True,
            "amountSigners":8,
            "groupSigners":"fourthGroup"
           
        }


 