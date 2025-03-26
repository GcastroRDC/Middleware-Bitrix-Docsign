import requests
from Controllers.Bitrix.getDataContractedCompany import getDataContractedCompany
from Controllers.Bitrix.valueWordsNumber import valueWordsNumber
from Controllers.Bitrix.setTotalContractValue import setTotalContractValue

def crmDealGetAll(tokenBitrix,idDeal):

    endpointCrmDealGet = f"https://dominio.bitrix24.com.br/rest/crm.deal.get?auth={tokenBitrix}"
   
    params = {

        'ID': idDeal 
    }

    # Enviando a requisição GET para a API
    response = requests.get(endpointCrmDealGet, params=params)

    # Verificando o status da resposta
    if response.status_code == 200:

        dealData = response.json()
        
         # Verifica se a chave "result" existe e contém dados
        if 'result' in dealData:

            dealInfo = dealData['result']
            
            # Campos obrigatórios do contrato e O.S
            tipoCliente = dealInfo.get('UF_CRM_1732228475718',None)
            segmento = dealInfo.get('UF_CRM_1639506890', None)
            subRegional = dealInfo.get('UF_CRM_1712768063', None)
            regional = dealInfo.get('UF_CRM_1724250996610', None)
            numeroContrato = dealInfo.get('UF_CRM_1732040318914', None)
            numeroOrdemServico = dealInfo.get('UF_CRM_1732041415258', None)
            empresaContratada = dealInfo.get('UF_CRM_1732913299214',None)
            razaoSocialContratante = dealInfo.get('UF_CRM_1732041490494', None)
            enderecoContratante = dealInfo.get('UF_CRM_1732043569984', None)
            cidadeContratante = dealInfo.get('UF_CRM_1732043625478', None)
            representanteLegalContratanteN1 = dealInfo.get('UF_CRM_1732043744912', None)
            emailRepresentanteLegalContratanteN1 = dealInfo.get('UF_CRM_1732043800421', None)
            consultorVendas = dealInfo.get('UF_CRM_1732045778781', None)
            emailConsultorVendas = dealInfo.get('UF_CRM_1732135820295', None)
            cnpjContratante = dealInfo.get('UF_CRM_1732045915475', None)
            bairroContratante = dealInfo.get('UF_CRM_1732046069653', None)
            cepContratante = dealInfo.get('UF_CRM_1732046121786', None)
            servicoContratado = dealInfo.get('UF_CRM_1732046955024', None)
            disponibilidade = dealInfo.get('UF_CRM_1732047019369', None)
            velocidade = dealInfo.get('UF_CRM_1732047092969', None)
            protocoloViabilidadeTecnica = dealInfo.get('UF_CRM_1732047162105', None)
            enderecoPontaA = dealInfo.get('UF_CRM_1732047253224', None)
            cidadePontaA = dealInfo.get('UF_CRM_1732047314540', None)
            cepPontaA = dealInfo.get('UF_CRM_1732047457216', None)
            ufPontaA = dealInfo.get('UF_CRM_1732047730587', None)
            valorMenalContrato = dealInfo.get('UF_CRM_1732047873050', None)
            dataContratacao = dealInfo.get('UF_CRM_1732047920462', None)
            dataExtincao = dealInfo.get('UF_CRM_1732048003279', None)
            duracao = dealInfo.get('UF_CRM_1732048054014', None)
            fidelizado = dealInfo.get('UF_CRM_1732048114302', None)
            dataVencimentoFatura = dealInfo.get('UF_CRM_1732048173863', None)
            
            # Campos opcionais do contrato e O.S
            servicoAdicional = dealInfo.get('UF_CRM_1732048534821', None)
            valorServicoAdicional = dealInfo.get('UF_CRM_1732048586470', None) or "0,00"
            observacoesServicoAdicional = dealInfo.get('UF_CRM_1732048657319', None)
            observacoesCondicaoComercial = dealInfo.get('UF_CRM_1732048720674', None)
            testemunhaContratanteN1 = dealInfo.get('UF_CRM_1732052887251', None)
            emailTestemunhaContratanteN1 = dealInfo.get('UF_CRM_1732133839817', None)
            cpfTestemunhaContratanteN1 = dealInfo.get('UF_CRM_1732133882315', None)
            prazoInstalacao = dealInfo.get('UF_CRM_1732048221439', None)
            taxaInstalacao = dealInfo.get('UF_CRM_1732048272999', None) or "0,00"
            numeroParcelasInstalacao = dealInfo.get('UF_CRM_1732048358166', None) 
            modeloInstalacao = dealInfo.get('UF_CRM_1732048406631', None)
            nomeContatoTecnico = dealInfo.get('UF_CRM_1732048842658', None)
            telefoneContatoTecnico = dealInfo.get('UF_CRM_1732048907979', None)
            emailContatoTecnico = dealInfo.get('UF_CRM_1732049003487', None)
            nomeContatoFinanceiro = dealInfo.get('UF_CRM_1732049097291', None)
            telefoneContatoFinanceiro = dealInfo.get('UF_CRM_1732049156940', None)
            emailContatoFinanceiro = dealInfo.get('UF_CRM_1732049252748', None)
            inscricaoMunicipalContratante = dealInfo.get('UF_CRM_1732045988479', None)
            cpfRepresentanteLegalContratanteN1 = dealInfo.get('UF_CRM_1732199943264', None)
            telefoneRepresentanteLegalContratanteN1 = dealInfo.get('UF_CRM_1732046347058', None)
            celularRepresentanteLegalContratanteN1 = dealInfo.get('UF_CRM_1732046867369', None)
            inscricaoEstadualContratante = dealInfo.get('UF_CRM_1732043117746', None)
            numeroContratante = dealInfo.get('UF_CRM_1732049389638', None)
            
        
            
            # Valor Mensal por Extenso
            valorMensalPorExtenso = valueWordsNumber(valorMenalContrato)

            #  Retorna os dados da empresa contratada
            dadosEmpresaContratada = getDataContractedCompany(empresaContratada)

            # Calcula o valor total do contrato (Valor mensal x duração + Taxa de Instalação)
            ValorTotalContrato = setTotalContractValue(
                valorMenalContrato,
                duracao,
                taxaInstalacao
                )

        
            # Construção de um dicionário com os valores dos campos da integração obrigatórios, com exceção dos campos opcionais.
            fieldsDeal ={
                
                "tipoCliente":tipoCliente,
                "segmento":segmento,
                "subRegional":subRegional,
                "regional":regional,
                "numeroContrato":numeroContrato,
                "empresaContratada":empresaContratada,
                "dadosEmpresaContratada":dadosEmpresaContratada,
                "numeroOrdemServico":numeroOrdemServico,
                "razaoSocialContratante":razaoSocialContratante,
                "enderecoContratante":enderecoContratante,
                "cidadeContratante":cidadeContratante,
                "representanteLegalContratanteN1":representanteLegalContratanteN1,
                "emailRepresentanteLegalContratanteN1":emailRepresentanteLegalContratanteN1,
                "testemunhaContratanteN1":testemunhaContratanteN1,
                "emailTestemunhaContratanteN1":emailTestemunhaContratanteN1,
                "consultorVendas":consultorVendas,
                "emailConsultorVendas":emailConsultorVendas,
                "cnpjContratante":cnpjContratante,
                "bairroContratante":bairroContratante,
                "cepContratante":cepContratante,
                "servicoContratado":servicoContratado,
                "disponibilidade":disponibilidade,
                "velocidade":"{}MB".format(velocidade),
                "protocoloViabilidadeTecnica":protocoloViabilidadeTecnica,
                "enderecoPontaA":enderecoPontaA,
                "cidadePontaA":cidadePontaA,
                "cepPontaA":cepPontaA,
                "ufPontaA":ufPontaA,
                "valorMenalContrato":valorMenalContrato,
                "valorMensalPorExtenso":valorMensalPorExtenso,
                "valorTotalContrato":ValorTotalContrato,
                "dataContratacao":dataContratacao,
                "dataExtincao":dataExtincao,
                "duracao":duracao,
                "fidelizado":fidelizado,
                "dataVencimentoFatura":dataVencimentoFatura,
                "nomeContatoTecnico": nomeContatoTecnico,
                "telefoneContatoTecnico": telefoneContatoTecnico,
                "emailContatoTecnico": emailContatoTecnico,
                "nomeContatoFinanceiro": nomeContatoFinanceiro,
                "telefoneContatoFinanceiro": telefoneContatoFinanceiro,
                "emailContatoFinanceiro": emailContatoFinanceiro
                
               
            }

             # array para armazenar as chaves com erros
            fieldsDealError = []
            
            # Percorre todos os campos do dicionario "fieldsDeal"
            for chave, valor in fieldsDeal.items():

                # Verifica se o valor está vazio ou é None
                if not valor or not str(valor).strip():

                    fieldsDealError.append(chave)  # Adiciona a chave a lista "fieldsDealError" 
            
             # Valida se o array "fieldsDealError" está vazia, caso sim significa que não temos campos obrigatórios vazios ou nulos
            if not fieldsDealError:

                #Adiciona os campos opcionais após a validação
                fieldsDeal["servicoAdicional"] = servicoAdicional
                fieldsDeal["valorServicoAdicional"] = valorServicoAdicional
                fieldsDeal["observacoesServicoAdicional"] = observacoesServicoAdicional
                fieldsDeal["observacoesCondicaoComercial"] = observacoesCondicaoComercial
                fieldsDeal["cpfTestemunhaContratanteN1"] = cpfTestemunhaContratanteN1
                fieldsDeal["inscricaoEstadualContratante"] = inscricaoEstadualContratante
                fieldsDeal["inscricaoMunicipalContratante"] = inscricaoMunicipalContratante
                fieldsDeal["numeroContratante"] = numeroContratante
                fieldsDeal["cpfRepresentanteLegalContratanteN1"] = cpfRepresentanteLegalContratanteN1
                fieldsDeal["taxaInstalacao"] = taxaInstalacao
                fieldsDeal["prazoInstalacao"] = prazoInstalacao
                fieldsDeal["numeroParcelasInstalacao"] = numeroParcelasInstalacao
                fieldsDeal["modeloInstalacao"] = modeloInstalacao
                fieldsDeal["telefoneRepresentanteLegalContratanteN1"] = telefoneRepresentanteLegalContratanteN1
                fieldsDeal["celularRepresentanteLegalContratanteN1"] = celularRepresentanteLegalContratanteN1
                
               
                return {

                    "status":True,
                    "values":fieldsDeal

                    }
            
            # Caso existam campos obrigatórios vazios ou nulos, é gerada uma notificação ao usuário na timeline do negócio para correção dos dados.
            else:

                return {

                    "status":False,
                    "values":None,
                    "type":"emptyFields",
                    "fieldsError":fieldsDealError
                    
                    }

        return {

            "status":False,
            "values":None,
            "type":"notFoundDealValues"
            }
    
    else:

        return {

            "status":False,
            "values":None,
            "type":"error"

            }