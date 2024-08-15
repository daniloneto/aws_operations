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

def query_items_by_pk_and_sk_prefix(dynamodb_client, table_name, pk_value, sk):
    try:
        response = dynamodb_client.query(
            TableName=table_name,
            KeyConditionExpression='pk = :pk and begins_with(sk, :sk)',
            ExpressionAttributeValues={
                ':pk': {'S': pk_value},
                ':sk': {'S': str(sk)}
            }
        )
        if 'Items' in response:
            return response['Items']
        else:
            print(f"Nenhum item encontrado com PK={pk_value} e SK começando com {sk}")
            return []
    except Exception as e:
        print(f"Erro ao buscar itens com PK={pk_value} e SK começando com {sk}: {e}")
        return []
        
def main():
    
    # Perfil do AWS CLI
    aws_profile = '123456_Perfil_1'  
    region_name = 'sa-east-1'
    
    dynamodb_client = connect_to_dynamodb(aws_profile, region_name)               
    items = query_items_by_pk_and_sk_prefix(dynamodb_client, "tabela","conta#1234","98765")
    for item in items:                
        print(json.dumps(item))
         
if __name__ == '__main__':
    main()
    
