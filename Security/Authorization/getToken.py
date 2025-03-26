
def getToken(clientRequest):

    # Obtem o token do cabeçalho 'Authorization'
    authHeader = clientRequest.headers.get('Authorization')
    
    if authHeader:

        parts = authHeader.split()

        if len(parts) == 2 and parts[0].lower() == 'bearer':
            
            return parts[1]  # Retorna o token com a origem 'header'
    
    # Obtem o token dos parâmetros da query string
    tokenQuery = clientRequest.args.get('token')

    if tokenQuery:

        return tokenQuery # Retorna o token com a origem 'query'
    
    # Obtem o token do corpo da requisição (em formato JSON)
    try:

        data = clientRequest.get_json()

        if data and 'token' in data:
            return data['token']  # Retorna o token com a origem 'body'
        
    except:

        return None
    
    # Se não encontrar o token em nenhuma das fontes, retorna None
    return None

