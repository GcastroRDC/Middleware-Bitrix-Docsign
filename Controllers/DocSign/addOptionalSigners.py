def addOptionalSigners(envelopeSchemeDefault, DealValues):
    """
    Função para adicionar a testemunha 1 ao scheme do envelope em caso de sua existência.
  

    Parâmetros:
        envelopeSchemeDefault (dict): O esquema padrão do envelope DocSign.
        DealValues (dict): Os valores extraídos do negócio, incluindo os campos de representantes e testemunhas.

    Retorna:
        dict: O esquema de envelope atualizado com a testemunha 1, se houver.
    """
    counter = 0  # Contador para os assinantes adicionais

    # Verifica se o campo 'testemunhaContratanteN1' está preenchido
    if DealValues["testemunhaContratanteN1"]:
        
        # Adiciona a testemunha N1 no esquema de envelope
        envelopeSchemeDefault["templateRoles"].append({
            "roleName": "Testemunha",  
            "name": DealValues["testemunhaContratanteN1"],  # Nome da primeira testemunha
            "email": DealValues.get("emailTestemunhaContratanteN1", ""),  # E-mail da primeira testemunha
            "signingOrder": len(envelopeSchemeDefault["templateRoles"]) + 1,
            "tabs": {
         
                    "textTabs": [

           
                            ],

                    "signHereTabs": [
                    {
                        "tabLabel": "assinaturaTestemunha",  # Referência ao campo existente
                        "required": True  # Torna a assinatura obrigatória
                    }
                ]
                        
                     }  
        })

        counter += 1

        dataTestemunhasContratante = [

             {"roleName":"Testemunha","name":DealValues["testemunhaContratanteN1"], "email":DealValues["emailTestemunhaContratanteN1"]},
        ]

        return {

            "status":True,
            "scheme":envelopeSchemeDefault,
            "witness":dataTestemunhasContratante,
            "counter":counter
            }
    
    return {
        "status":False,
        "scheme":envelopeSchemeDefault,
        "dataWitness":None,
        "counter":counter
        }
