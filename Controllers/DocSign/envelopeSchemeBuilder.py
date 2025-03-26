from Controllers.DocSign.GroupSignature import GroupSignature
from Controllers.DocSign.fillOrderScheme import fillOrderScheme
from Controllers.DocSign.fillSigners import fillSigners
from Controllers.DocSign.addOptionalSigners import addOptionalSigners
from Controllers.DocSign.addTabsToAllSigners import addTabsToAllSigners
from Controllers.DocSign.getIdDocumentTemplate import getIdDocumentTemplate
from Controllers.Bitrix.getB2BSalesManager import getB2BSalesManager
from Controllers.Bitrix.getCommercialExecutiveManager import getCommercialExecutiveManager
from Controllers.Bitrix.getN3PreSalesManager import getN3PreSalesManager
import datetime
from Controllers.DocSign.envelopeConfig import (
    
    BACKOFFICE,
    ADVOGADO_ADM_B2B,
    GERENTE_EXECUTIVO_DESENVOLVIMENTO_COMERCIAL,
    DIRETOR_COMERCIAL,
    GERENTE_EXECUTIVO_PREVENDAS,
    N1_B2B,
    N1_FINANCEIRO

    )

# Função para gerenciamento de erros do "envelopeSchemeBuilder"
def handleErrosEnvelopeScheme(status,type):

    return {"status":status,"type":type}

def envelopeSchemeBuilder(tokenDocSign,listConstants,listValuesEntity):

    basePath = listConstants['BASEURL']

    # Endpoint da Api Rest DocSign responsável pelo envio do envelope: https://demo.docusign.net/restapi/v2.1/accounts/{ID Acoount}/envelopes
    resourcePath = f"{basePath}/restapi/v2.1/accounts/{listConstants['ACCOUNTID']}/envelopes"

    headers = {

    "Authorization": f"Bearer {tokenDocSign}",
    "Content-Type": "application/json"

    }

    # Extrai os dados do Negócio
    DealValues = listValuesEntity["deal"]

    # Gerar o emailSubject
    emailSubject = f"Contrato comercial da sua empresa: {DealValues['empresaContratada']} e {DealValues['razaoSocialContratante']}"
    
    # Verificar o comprimento e garantir que não ultrapasse 100 caracteres
    if len(emailSubject) > 100:
        
        emailSubject = emailSubject[:100]  # Trunca para 100 caracteres

    # Scheme Padrão
    envelopeSchemeDefault = {

        "templateId": "",  # ID do Modelo
        "emailSubject": emailSubject,
        "templateRoles": [

             {
            
                "roleName": "", #BackOffice 1º Aprovador
                "name": "",  # Nome 
                "email": "",  # E-mail 
                "signingOrder": 1,  
                "tabs": {
         
                    "textTabs": [

           
                            ]
                     }
                
            },
            {
            
                "roleName": "",  
                "name": "",  # Nome 
                "email": "",  # E-mail 
                "signingOrder": 2,  
                "tabs": {
         
                    "textTabs": [

           
                            ]
                     }
                
            },
            {
              
                "roleName": "",  
                "name": "",  # Nome 
                "email": "",  # E-mail 
                "signingOrder": 3,
                "tabs": {
         
                    "textTabs": [

           
                            ]
                     }
            },
            {
        
                "roleName": "", 
                "name": "",  # Nome 
                "email": "",  # E-mail
                "signingOrder": 4,
                "tabs": {
         
                    "textTabs": [

           
                            ]
                     }
            },
            {
            
                "roleName": "",  
                "name": "",  # Nome 
                "email":"",  # E-mail 
                "signingOrder": 5,
                "tabs": {
         
                    "textTabs": [

           
                            ]
                     }
            },
            {
             
                "roleName": "",  
                "name": "",  # Nome 
                "email":"",  # E-mail 
                "signingOrder": 6,
                "tabs": {
         
                    "textTabs": [

           
                            ]
                     }
            },
            {
              
                "roleName": "",  
                "name": "",  # Nome 
                "email":"" ,  # E-mail 
                "signingOrder": 7,
                "tabs": {
         
                    "textTabs": [

           
                            ]
                     }
            },
            {
                
                "roleName": "",  
                "name":"",  # Nome
                "email": "",  # E-mail
                "signingOrder": 8,
                "tabs": {
         
                    "textTabs": [

           
                            ]
                     }
            }
           
        ],

        "status": "sent",
        "brandId":listConstants['BRANDID'] 
    }

    
    # Obtem o Gerente de Vendas B2B
    dataB2BSalesManager = getB2BSalesManager(

        DealValues["segmento"],
        DealValues["subRegional"]

        )
    
    # Trata a exceção da função "getB2BSalesManager"
    if not dataB2BSalesManager["status"]:

        response = handleErrosEnvelopeScheme(False,"notFoundSalesManager")

        return response


    # Obtem o Gerente Executivo Comercial
    dataCommercialExecutiveManager = getCommercialExecutiveManager(DealValues["regional"])
    
    
    # Trata a exceção da função "getCommercialExecutiveManager"
    if not dataCommercialExecutiveManager["status"]:
        
        response = handleErrosEnvelopeScheme(False,"notFoundExecutiveManager")

        return response
    
    dataN3preSalesManager = getN3PreSalesManager(DealValues["regional"])

    # Trata a exceção da função "getN3PreSalesManager"
    if not dataN3preSalesManager["status"]:
        
        responde =  handleErrosEnvelopeScheme(False,"notFoundExecutiveManager")

        return responde

    # Tabs do Contrato
    tabsContract = [

            {"tabLabel": "numeroContrato", "value":DealValues["numeroContrato"]},
            {"tabLabel": "anoContrato", "value":datetime.datetime.now().year},
             {"tabLabel": "enderecoContratada", "value": DealValues["dadosEmpresaContratada"]["endereco"]},
            {"tabLabel": "numeroContratada", "value":DealValues["dadosEmpresaContratada"]["numero"]},
            {"tabLabel": "bairroContratada", "value":DealValues["dadosEmpresaContratada"]["bairro"]},
            {"tabLabel": "cidadeContratada", "value":DealValues["dadosEmpresaContratada"]["cidade"]},
            {"tabLabel": "cepContratada", "value":DealValues["dadosEmpresaContratada"]["cep"]},
            {"tabLabel": "cnpjContratada", "value":DealValues["dadosEmpresaContratada"]["cnpj"]},
            {"tabLabel": "empresaContratada", "value":DealValues["dadosEmpresaContratada"]["nome"]},
            {"tabLabel": "nomeEmpresaContrato", "value":DealValues["razaoSocialContratante"]},
            {"tabLabel": "cnpjEmpresaContrato", "value":DealValues["cnpjContratante"]},
            {"tabLabel": "enderecoEmpresaContrato", "value":DealValues["enderecoContratante"]},
            {"tabLabel": "numeroEmpresaContrato", "value":DealValues["numeroContratante"]},
            {"tabLabel": "bairroEmpresaContrato", "value": DealValues["bairroContratante"]},
            {"tabLabel": "cepEmpresaContrato", "value":DealValues["cepContratante"]},
            {"tabLabel": "nomeCliente", "value":DealValues["representanteLegalContratanteN1"]},
            {"tabLabel": "cpfCliente", "value":DealValues["cpfRepresentanteLegalContratanteN1"]},
            {"tabLabel": "emailCliente", "value": DealValues["emailRepresentanteLegalContratanteN1"]},
            {"tabLabel": "nomeTestemunha", "value":DealValues["testemunhaContratanteN1"]},
            {"tabLabel": "cpfTestemunha", "value": DealValues["cpfTestemunhaContratanteN1"]},
            {"tabLabel": "emailTestemunha", "value": DealValues["emailTestemunhaContratanteN1"]},
            {"tabLabel": "nomeExecutivoVendas", "value":DealValues["consultorVendas"]},
            {"tabLabel": "emailExecutivoVendas", "value": DealValues["emailConsultorVendas"]},
            {"tabLabel": "nomeGerenteVendasB2B", "value":dataB2BSalesManager["name"]},
            {"tabLabel": "emailGerenteVendasB2B", "value": dataB2BSalesManager["email"]},
            {"tabLabel": "nomeBackoffice", "value": BACKOFFICE["name"]},
            {"tabLabel": "emailBackoffice", "value": BACKOFFICE["email"]},
            {"tabLabel": "nomeAdvogadoAdmB2B", "value":ADVOGADO_ADM_B2B["name"]},
            {"tabLabel": "emailAdvogadoAdmB2B", "value":ADVOGADO_ADM_B2B["email"]},
            {"tabLabel": "nomeGerenteExecutivoPrevendas", "value":GERENTE_EXECUTIVO_PREVENDAS["name"]},
            {"tabLabel": "emailGerenteExecutivoPrevendas", "value":GERENTE_EXECUTIVO_PREVENDAS["email"]},
            {"tabLabel": "nomeGerenteExecutivoDesenvolvimentoComercial", "value":GERENTE_EXECUTIVO_DESENVOLVIMENTO_COMERCIAL["name"]},
            {"tabLabel": "emailGerenteExecutivoDesenvolvimentoComercial", "value":GERENTE_EXECUTIVO_DESENVOLVIMENTO_COMERCIAL["email"]},
             {"tabLabel": "nomeGerenteExecutivoComercial", "value":dataCommercialExecutiveManager["name"]},
            {"tabLabel": "emailGerenteExecutivoComercial", "value": dataCommercialExecutiveManager["email"]},
            {"tabLabel": "nomeN3PreVendas", "value":dataN3preSalesManager["name"]},
            {"tabLabel": "emailN3PreVendas", "value": dataN3preSalesManager["email"]},
            {"tabLabel": "nomeDiretorComercial", "value":DIRETOR_COMERCIAL["name"]},
            {"tabLabel": "emailDiretorComercial", "value": DIRETOR_COMERCIAL["email"]},
            {"tabLabel": "nomeN1B2B", "value":N1_B2B["name"]},
            {"tabLabel": "emailN1B2B", "value": N1_B2B["email"]},
            {"tabLabel": "nomeN1Financeiro", "value":N1_FINANCEIRO["name"]},
            {"tabLabel": "emailN1Financeiro", "value": N1_FINANCEIRO["email"]},

            
    ]


    # Tabs da Ordem de Serviço
    tabsServiceOrder =  [

            {"tabLabel": "numeroContratoOS", "value": DealValues["numeroContrato"]},
            {"tabLabel": "numeroOS", "value":DealValues["numeroOrdemServico"]},
            {"tabLabel": "anoContrato", "value":datetime.datetime.now().year},
            {"tabLabel": "razaoSocialOS", "value": DealValues["razaoSocialContratante"]},
            {"tabLabel": "inscricaoEstadualOS", "value":DealValues["inscricaoEstadualContratante"]},
            {"tabLabel": "enderecoOS", "value":DealValues["enderecoContratante"]},
            {"tabLabel": "cidadeOS", "value": DealValues["cidadeContratante"]},
            {"tabLabel": "representanteLegalOS", "value":DealValues["representanteLegalContratanteN1"]},
            {"tabLabel": "emailRepresentanteOS", "value":DealValues["emailRepresentanteLegalContratanteN1"]},
            {"tabLabel": "cpfRepresentantePrimarioOS", "value": DealValues["cpfRepresentanteLegalContratanteN1"]},
            {"tabLabel": "nomeExecutivoVendas", "value":DealValues["consultorVendas"]},
            {"tabLabel": "cnpjOS", "value":DealValues["cnpjContratante"]},
            {"tabLabel": "inscricaoMunicipalOS", "value":DealValues["inscricaoMunicipalContratante"]},
            {"tabLabel": "bairroOS", "value":DealValues["bairroContratante"]},
            {"tabLabel": "cepOS", "value":DealValues["cepContratante"]},
            {"tabLabel": "telefoneRepresentanteOS", "value": DealValues["telefoneRepresentanteLegalContratanteN1"]},
            {"tabLabel": "celularRepresentanteOS", "value":DealValues["celularRepresentanteLegalContratanteN1"]},
            {"tabLabel": "servicoContratadoOS", "value":DealValues["servicoContratado"]},
            {"tabLabel": "DisponibilidadeOS", "value": DealValues["disponibilidade"]},
            {"tabLabel": "velocidadeOS", "value": DealValues["velocidade"]},
            {"tabLabel": "numeroProtocoloOS", "value":DealValues["protocoloViabilidadeTecnica"]},
            {"tabLabel": "enderecoPontaA", "value": DealValues["enderecoPontaA"]},
            {"tabLabel": "cidadePontaA", "value":DealValues["cidadePontaA"]},
            {"tabLabel": "cepPontaA", "value": DealValues["cepPontaA"]},
            {"tabLabel": "ufPontaA", "value": DealValues["ufPontaA"]},
            {"tabLabel": "valorMensal", "value": DealValues["valorMensalPorExtenso"]},
            {"tabLabel": "dataContratacao", "value":DealValues["dataContratacao"]},
            {"tabLabel": "dataExtincao", "value":DealValues["dataExtincao"]},
            {"tabLabel": "duracaoMensal", "value":"{} MESES".format(DealValues["duracao"])},
            {"tabLabel": "duracao", "value": DealValues["duracao"]},
            {"tabLabel": "fidelizado", "value":DealValues["fidelizado"]},
            {"tabLabel": "dataVencimentoFatura", "value":DealValues["dataVencimentoFatura"]},
            {"tabLabel": "prazoInstalacao", "value":DealValues["prazoInstalacao"]},
            {"tabLabel": "taxaInstalacao", "value": DealValues["taxaInstalacao"]},
            {"tabLabel": "numeroParcelasInstalacao", "value":DealValues["numeroParcelasInstalacao"]},
            {"tabLabel": "modeloInstalacao", "value": DealValues["modeloInstalacao"]},
            {"tabLabel": "observacoesOS", "value": DealValues["observacoesCondicaoComercial"]},
            {"tabLabel": "servicosAdicionais", "value": DealValues["servicoAdicional"]},
            {"tabLabel": "valorServicosAdicionais", "value": DealValues["valorServicoAdicional"]},
            {"tabLabel": "observacaoServicosAdicionais", "value": DealValues["observacoesServicoAdicional"]},
            {"tabLabel": "nomeTecnicoContratante", "value": DealValues["nomeContatoTecnico"]},
            {"tabLabel": "telefoneContatoTecnico", "value": DealValues["telefoneContatoTecnico"]},
            {"tabLabel": "emailContatoTecnico", "value":DealValues["emailContatoTecnico"]},
             {"tabLabel": "telefoneContratada", "value": DealValues["dadosEmpresaContratada"]["telefone"]},
            {"tabLabel": "emailContratada", "value":DealValues["dadosEmpresaContratada"]["email"]},
            {"tabLabel": "nomeContatoFinanceiro", "value": DealValues["nomeContatoFinanceiro"]},
            {"tabLabel": "telefoneContatoFinanceiro", "value":DealValues["telefoneContatoFinanceiro"]},
            {"tabLabel": "emailContatoFinanceiro", "value": DealValues["emailContatoFinanceiro"]},
             {"tabLabel": "nomeCliente", "value":DealValues["representanteLegalContratanteN1"]},
            {"tabLabel": "cpfCliente", "value":DealValues["cpfRepresentanteLegalContratanteN1"]},
            {"tabLabel": "emailCliente", "value": DealValues["emailRepresentanteLegalContratanteN1"]},
            {"tabLabel": "nomeTestemunha", "value":DealValues["testemunhaContratanteN1"]},
            {"tabLabel": "cpfTestemunha", "value": DealValues["cpfTestemunhaContratanteN1"]},
            {"tabLabel": "emailTestemunha", "value": DealValues["emailTestemunhaContratanteN1"]},
            {"tabLabel": "nomeExecutivoVendas", "value":DealValues["consultorVendas"]},
            {"tabLabel": "emailExecutivoVendas", "value": DealValues["emailConsultorVendas"]},
            {"tabLabel": "nomeGerenteVendasB2B", "value":dataB2BSalesManager["name"]},
            {"tabLabel": "emailGerenteVendasB2B", "value": dataB2BSalesManager["email"]},
            {"tabLabel": "nomeBackoffice", "value": BACKOFFICE["name"]},
            {"tabLabel": "emailBackoffice", "value": BACKOFFICE["email"]},
            {"tabLabel": "nomeAdvogadoAdmB2B", "value":ADVOGADO_ADM_B2B["name"]},
            {"tabLabel": "emailAdvogadoAdmB2B", "value":ADVOGADO_ADM_B2B["email"]},
            {"tabLabel": "nomeGerenteExecutivoPrevendas", "value":GERENTE_EXECUTIVO_PREVENDAS["name"]},
            {"tabLabel": "emailGerenteExecutivoPrevendas", "value":GERENTE_EXECUTIVO_PREVENDAS["email"]},
            {"tabLabel": "nomeGerenteExecutivoDesenvolvimentoComercial", "value":GERENTE_EXECUTIVO_DESENVOLVIMENTO_COMERCIAL["name"]},
            {"tabLabel": "emailGerenteExecutivoDesenvolvimentoComercial", "value":GERENTE_EXECUTIVO_DESENVOLVIMENTO_COMERCIAL["email"]},
             {"tabLabel": "nomeGerenteExecutivoComercial", "value":dataCommercialExecutiveManager["name"]},
            {"tabLabel": "emailGerenteExecutivoComercial", "value": dataCommercialExecutiveManager["email"]},
            {"tabLabel": "nomeN3PreVendas", "value":dataN3preSalesManager["name"]},
            {"tabLabel": "emailN3PreVendas", "value": dataN3preSalesManager["email"]},
            {"tabLabel": "nomeDiretorComercial", "value":DIRETOR_COMERCIAL["name"]},
            {"tabLabel": "emailDiretorComercial", "value":DIRETOR_COMERCIAL["email"]},
            {"tabLabel": "nomeN1B2B", "value":N1_B2B["name"]},
            {"tabLabel": "emailN1B2B", "value": N1_B2B["email"]},
            {"tabLabel": "nomeN1Financeiro", "value":N1_FINANCEIRO["name"]},
            {"tabLabel": "emailN1Financeiro", "value":N1_FINANCEIRO["email"]},
    ]

    
    
    # Define o grupo responsável da alçada de assinaturas
    dataGroupSignature = GroupSignature(

        DealValues["valorTotalContrato"],
        DealValues["duracao"]

        )
  
    # Trata a exceção da função "GroupSignature"
    if not dataGroupSignature["status"]:

        response = handleErrosEnvelopeScheme(False,"NotFoundGroupSignature")

        return response

    
    dataIdTemplate = getIdDocumentTemplate(

        listConstants["DOCUMENTTEMPLATES"],
        DealValues["tipoCliente"],
        dataGroupSignature["groupSigners"]

        )
    
    
    # Trata a exceção da função "getIdDocumentTemplate"
    if not dataIdTemplate["status"]:

        response = handleErrosEnvelopeScheme(False,"notFoundIdTemplate")

        return response

   
    # Seta o ID do Template encontrado no scheme Padrão
    envelopeSchemeDefault["templateId"] = dataIdTemplate["IdTemplate"]

    # Partes qeu variam conforme alguma regra no fluxo de assinatura ou aprovação do contrato
    variableGroupSignatures = [

    {"identificador":"Executivo Vendas","name":DealValues["consultorVendas"], "email":DealValues["emailConsultorVendas"]},
    {"identificador":"Gerente Vendas B2B","name":dataB2BSalesManager["name"], "email":dataB2BSalesManager["email"]},
    {"identificador":"Cliente","name":DealValues["representanteLegalContratanteN1"], "email":DealValues["emailRepresentanteLegalContratanteN1"]},
    {"identificador":"Gerente Executivo Comercial","name":dataCommercialExecutiveManager["name"], "email":dataCommercialExecutiveManager["email"]},
    {"identificador":"N3 Pre Vendas","name":dataN3preSalesManager["name"], "email":dataN3preSalesManager["email"]}

    ] 


    # Formata o scheme padrão para ficar em conformidade com a quantidade de assinaturas do grupo de alçada
    schemeOrdered = fillOrderScheme(

        envelopeSchemeDefault,
        dataGroupSignature["amountSigners"]

        )
    
    # Verificação a existencia da Testemunha do contratante e inserção no scheme do envelope
    dataOptionSignersScheme = addOptionalSigners(

        schemeOrdered,
        DealValues

        )

    
    # Preenche o scheme ordenado com os valores do nome,email e rolename de cada participante do grupo da alçada selecionado
    dataFinalScheme = fillSigners(

        dataOptionSignersScheme["scheme"],
        dataGroupSignature["groupSigners"],
        variableGroupSignatures,
        dataOptionSignersScheme

        ) 

    # Trata a exceção da função "fillSigners"
    if not dataFinalScheme["status"] or dataFinalScheme["finalScheme"] is None:
     
        response = handleErrosEnvelopeScheme(False,"errorFinalScheme")
        
        return response

    #Extrai a lista com os destinatários do grupo da alçada de assinatura
    dataGroupRecipients = dataFinalScheme["dataGroupSigners"]

    
    #Extrai o scheme final do envelope
    envelopeScheme = dataFinalScheme["finalScheme"]
            

    # Valida o tipo de cliente
    if DealValues["tipoCliente"] == "Novo":

        # Combina as duas tabs (tabsContract e tabsServiceOrder)
        combinedTabs = tabsContract + tabsServiceOrder

        # Preenche o scheme do envelope com as tabs da ordem de serviço e contrato
        envelopeSchemeFinal = addTabsToAllSigners(envelopeScheme,combinedTabs)
        
        return {

        "status":True,
        "body":envelopeSchemeFinal,
        "resourcePath":resourcePath,
        "headers":headers,
        "dataRecipients":dataGroupRecipients

        }
    
    # Preenche o scheme do envelope somente com as tabs da ordem de serviço
    envelopeSchemeFinal = addTabsToAllSigners(envelopeScheme,tabsServiceOrder)

    return {

        "status":True,
        "body":envelopeSchemeFinal,
        "resourcePath":resourcePath,
        "headers":headers,
        "dataRecipients":dataGroupRecipients

        }

   