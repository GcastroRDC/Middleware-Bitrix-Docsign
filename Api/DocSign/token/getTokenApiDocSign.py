from docusign_esign import ApiClient
from SdkDocSign.jwt_helpers.jwt_helper import get_jwt_token, get_private_key
from SdkDocSign.jwt_config import DS_JWT

SCOPES = [

    "signature", "impersonation"
]


def getTokenApiDocSign():

    api_client = ApiClient()

    api_client.set_base_path(DS_JWT["authorization_server"])
    api_client.set_oauth_host_name(DS_JWT["authorization_server"])
    
    private_key = get_private_key(DS_JWT["private_key_file"]).encode("ascii").decode("utf-8")

    token_response = get_jwt_token(private_key, SCOPES, DS_JWT["authorization_server"], DS_JWT["ds_client_id"],
                                   DS_JWT["ds_impersonated_user_id"])
    
    access_token = token_response.access_token

    if not access_token:

        return {
            "status":False,
            "token":None
            } 
    
    return {
        "status":True,
        "token":access_token
        }



