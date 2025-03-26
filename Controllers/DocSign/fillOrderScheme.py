# Filtra o scheme Padrão para deixa-lo em conformidade com a quantidade de assinaturas do grupo estabelecido.
def fillOrderScheme(schemeEnvelope,amountSignatures):
    
    schemeEnvelope["templateRoles"] = [

        role for role in schemeEnvelope["templateRoles"]

        if role["signingOrder"] <= int(amountSignatures)
    ]

    return schemeEnvelope
