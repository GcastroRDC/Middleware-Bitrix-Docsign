# -----------------------------------------  Regras Alçada de Assinatura:

# regra: Valor total menor ou igual a 240.000
TARGET_GROUPFIRST = 240000 

# regra: Valor total maior do que 240.000 e menor ou igual a 999.999
TARGET_GROUPSECOND = 999999 

# regra: Valor total igual ou acima de 1.000.000
TARGET_GROUPTHIRD = 1000000 

# regra: Tempo de Contrato acima de 36M, indiferente do Valor.
TARGET_GROUPFOURTH = 36  

#--------------------------------------------- Participantes Padrão da Alçada de Assinatura ----------------------------------------------------------------------
BACKOFFICE = {
    
    "name":"NOME",
    "email":"EMAIL" 
}

ADVOGADO_ADM_B2B = {
    
    "name":"NOME",
    "email":"EMAIL" 
}

GERENTE_EXECUTIVO_DESENVOLVIMENTO_COMERCIAL = {

    "name":"NOME",
    "email":"EMAIL"

}


DIRETOR_COMERCIAL = {

    "name":"NOME",
    "email":"EMAIL"


}

GERENTE_EXECUTIVO_PREVENDAS = {

    "name":"NOME",
    "email":"EMAIL"
}


N1_B2B = {

    "name":"NOME",
    "email":"EMAIL"
}


N1_FINANCEIRO = {

    "name":"NOME",
    "email":"EMAIL"
}

# -------------------------------------------- Grupos Ordenados Com os Participantes da Alçada de Assinatura -------------------------------------------------------
# ALTERAR A ORDEM DOS GRUPO SOMENTE NOS SEGUINTES CASOS: REMOÇÃO OU ADIÇÃO DE NOVOS PARTICIPANTES NA ALÇADA DE ASSINATURA. NÃO ESQUEÇA DE ALTERAR O SCHEME PADRÃO APÓS AS ALTERAÇÕES!          
GROUPFIRST = [

    {"roleName":"Backoffice","name":BACKOFFICE["name"], "email":BACKOFFICE["email"]},
    {"roleName":"Executivo de Vendas","name": "", "email": ""}, # Responsável pelo negócio
    {"roleName":"Gerente de Vendas B2B","name": "", "email": ""}, # Varia conforme a regional do negócio
    {"roleName":"Cliente","name": "", "email": ""},
    {"roleName":"Advogado Administrativo B2B","name":ADVOGADO_ADM_B2B["name"], "email":ADVOGADO_ADM_B2B["email"]},
    {"roleName":"Gerente Executivo Comercial","name":"" , "email":""}, # Varia conforme a regional do negócio
    {"roleName":"Gerente Executivo de Desenvolvimento Comercial","name":GERENTE_EXECUTIVO_DESENVOLVIMENTO_COMERCIAL["name"], "email":GERENTE_EXECUTIVO_DESENVOLVIMENTO_COMERCIAL["email"]}

]

GROUPSECOND = [

    {"roleName":"Backoffice","name":BACKOFFICE["name"], "email":BACKOFFICE["email"]},
    {"roleName":"Executivo de Vendas","name": "", "email": ""}, # Varia conforme a regional do negócio
    {"roleName":"Gerente Executivo Comercial","name":"", "email":""},
    {"roleName":"Cliente","name": "", "email": ""},
    {"roleName":"Advogado Administrativo B2B","name":ADVOGADO_ADM_B2B["name"], "email":ADVOGADO_ADM_B2B["email"]},
    {"roleName":"N3 Pre Vendas","name":"", "email":""}, # Varia conforme a regional do negócio
    {"roleName":"Diretor Comercial","name":DIRETOR_COMERCIAL["name"], "email":DIRETOR_COMERCIAL["email"]},
    {"roleName":"Gerente Executivo Pre Vendas","name":GERENTE_EXECUTIVO_PREVENDAS["name"], "email": GERENTE_EXECUTIVO_PREVENDAS["email"]}

]

GROUPTHIRD = [

    {"roleName":"Backoffice","name":BACKOFFICE["name"], "email":BACKOFFICE["email"]},
    {"roleName":"Diretor Comercial","name":DIRETOR_COMERCIAL["name"] , "email":DIRETOR_COMERCIAL["email"]},
    {"roleName":"Gerente Executivo Pre Vendas","name":GERENTE_EXECUTIVO_PREVENDAS["name"], "email":GERENTE_EXECUTIVO_PREVENDAS["email"]},
    {"roleName":"Cliente","name": "", "email": ""},
    {"roleName":"Advogado Administrativo B2B","name":ADVOGADO_ADM_B2B["name"], "email":ADVOGADO_ADM_B2B["email"]},
    {"roleName":"Gerente Executivo de Desenvolvimento Comercial","name": GERENTE_EXECUTIVO_DESENVOLVIMENTO_COMERCIAL["name"], "email":GERENTE_EXECUTIVO_DESENVOLVIMENTO_COMERCIAL["email"]},
    {"roleName":"N1 B2B","name": N1_B2B["name"], "email":N1_B2B["email"]},
    {"roleName":"N1 Financeiro","name": N1_FINANCEIRO["name"], "email":N1_FINANCEIRO["email"]}
]

GROUPFOURTH = [

    {"roleName":"Backoffice","name":BACKOFFICE["name"], "email":BACKOFFICE["email"]},
    {"roleName":"Diretor Comercial","name":DIRETOR_COMERCIAL["name"] , "email":DIRETOR_COMERCIAL["email"]},
    {"roleName":"Gerente Executivo Pre Vendas","name":GERENTE_EXECUTIVO_PREVENDAS["name"], "email":GERENTE_EXECUTIVO_PREVENDAS["email"]},
    {"roleName":"Cliente","name": "", "email": ""},
    {"roleName":"Advogado Administrativo B2B","name":ADVOGADO_ADM_B2B["name"], "email":ADVOGADO_ADM_B2B["email"]},
    {"roleName":"Gerente Executivo de Desenvolvimento Comercial","name": GERENTE_EXECUTIVO_DESENVOLVIMENTO_COMERCIAL["name"], "email":GERENTE_EXECUTIVO_DESENVOLVIMENTO_COMERCIAL["email"]},
    {"roleName":"N1 B2B","name": N1_B2B["name"], "email":N1_B2B["email"]},
    {"roleName":"N1 Financeiro","name": N1_FINANCEIRO["name"], "email":N1_FINANCEIRO["email"]}
]
