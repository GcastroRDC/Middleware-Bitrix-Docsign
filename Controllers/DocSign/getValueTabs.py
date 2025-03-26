def getValueTabs(jsonEvent):
    try:
        # Verificando se a chave 'data' existe
        if "data" not in jsonEvent:
            return {"status": False, "idDeal": None}

        # Acessando 'envelopeSummary' dentro de 'data'
        envelopeData = jsonEvent["data"]

        # Verificando se 'envelopeSummary' existe dentro de 'data'
        if "envelopeSummary" not in envelopeData:
            return {"status": False, "idDeal": None}

        # Acessando os dados dentro de 'envelopeSummary'
        envelopeSummary = envelopeData["envelopeSummary"]

        # Verificando se a chave 'recipients' existe dentro de 'envelopeSummary'
        if "recipients" not in envelopeSummary:
            return {"status": False, "idDeal": None}

        recipients = envelopeSummary["recipients"]

        # Verificando se a chave 'signers' existe dentro de 'recipients'
        if "signers" not in recipients:
            return {"status": False, "idDeal": None}

        signers = recipients["signers"]

        # Iterando sobre os signatários
        for signer in signers:
            tabs = signer.get("tabs", {})
            textTabs = tabs.get("textTabs", [])

            # Buscando o tabLabel
            for tab in textTabs:
                tabLabel = tab.get("tabLabel")

                # o campo "numeroProtocoloOS" contém o ID do Negócio Bitrix.
                if tabLabel == "numeroProtocoloOS":
                    valueTabIdDeal = tab.get("value")
                    

                    # Verificando se 'envelopeDocuments' está presente na resposta
                    if "envelopeDocuments" in envelopeSummary:
                        # Armazenando os bytes de todos os documentos em uma lista
                        allPdfBytes = []
                        for document in envelopeSummary["envelopeDocuments"]:
                            # Adiciona os bytes de cada documento na lista
                            pdfBytes = document.get("PDFBytes")
                            if pdfBytes:
                                allPdfBytes.append(pdfBytes)

                        # Retorna o ID do negócio e os PDFs em base64
                        return {
                            "status": True,
                            "idDeal": valueTabIdDeal,
                            "allFiles": allPdfBytes  # Lista com os PDFs
                        }

    except:
      
        return {
            "status": False,
            "idDeal": None
        }

    return {
        "status": False,
        "idDeal": None
    }
