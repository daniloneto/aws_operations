import sys
import boto3
   
def connect_to_dynamodb(profile_name, region_name):
    """
    Conecta ao DynamoDB usando as credenciais do perfil fornecido e retorna o cliente DynamoDB.

    Args:
        profile_name (str): Nome do perfil do AWS CLI.
        region_name (str): Nome da região do DynamoDB.

    Returns:
        boto3.client: Cliente DynamoDB conectado.
    """
    session = boto3.Session(profile_name=profile_name)
    dynamodb = session.client('dynamodb', region_name=region_name)
    return dynamodb    

def main():
    
    # Perfil do AWS CLI
    aws_profile = '123456_Perfil_1'  
    region_name = 'sa-east-1'
    
    dynamodb_client = connect_to_dynamodb(aws_profile, region_name)               
    
    
if __name__ == '__main__':
    main()
    
