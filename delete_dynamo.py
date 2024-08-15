import sys
import boto3
import json
   
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

def delete_item(dynamodb_client, table_name, pk_value, sk_value):
    try:
        response = dynamodb_client.delete_item(
            TableName=table_name,
            Key={
                'pk': {'S': pk_value},
                'sk': {'S': sk_value}
            }
        )        
        return True
    except Exception as e:
        print(f"Erro ao excluir o item com PK={pk_value} e SK={sk_value} da tabela {table_name}: {e}")
        return False
        
def main():
    
    # Perfil do AWS CLI
    aws_profile = '123456-Perfil_1'  
    region_name = 'sa-east-1'
    
    dynamodb_client = connect_to_dynamodb(aws_profile, region_name)               
    delete_item(dynamodb_client, "tabela","conta#1234","1392198447")    
         
if __name__ == '__main__':
    main()
    
