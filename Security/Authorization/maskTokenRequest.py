# Função para mascarar o token da requisição
def maskTokenRequest(url):

    token_key = 'token='

    if token_key in url:

        start = url.find(token_key) + len(token_key)
        end = url.find('&', start) if '&' in url[start:] else len(url)
        token = url[start:end]
        masked_url = url.replace(token, 'token=****')

        return masked_url
    
    return url