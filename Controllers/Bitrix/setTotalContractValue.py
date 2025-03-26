def setTotalContractValue(monthlyAmount, duration, installationRate):
    
    # Verifica se installationRate é válida (não nula e diferente de "0,00")
    if installationRate and installationRate != "0,00":
        
        total = (float(monthlyAmount) * int(duration)) + float(installationRate)
        
    else:
        
        total = float(monthlyAmount) * int(duration)

    return total