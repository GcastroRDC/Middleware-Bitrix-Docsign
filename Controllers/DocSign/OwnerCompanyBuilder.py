def ownerCompanyBuilder(dataCrmDealOwner):

    dataOwnerCompany = {

                "representanteLegalContratanteN1":{

                    "nome":dataCrmDealOwner['representanteLegalContratanteN1'],
                    "email":dataCrmDealOwner['emailRepresentanteLegalContratanteN1'],
                    "cpf":dataCrmDealOwner['cpfRepresentanteLegalContratanteN1'],
                    "telefone":dataCrmDealOwner['telefoneRepresentanteLegalContratanteN1'],
                    "celular":dataCrmDealOwner['celularRepresentanteLegalContratanteN1']

                },

                "testemunhaContratanteN1":{

                    "nome":dataCrmDealOwner['testemunhaContratanteN1'],
                    "email":dataCrmDealOwner['testemunhaContratanteN1'],
                    "cpf":dataCrmDealOwner['cpfTestemunhaContratanteN1']

                }
            }
    
    return dataOwnerCompany