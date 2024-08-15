import boto3

# Inicialize o cliente do CodeCommit
aws_profile = '123456_Perfil_1'  
aws_region = 'sa-east-1'

session = boto3.Session(profile_name=aws_profile)
client = session.client('codecommit', region_name=aws_region)    
    
# Palavra para filtrar os nomes dos repositórios
palavra_filtro = 'xyz'

# Lista todos os repositórios do CodeCommit
response = client.list_repositories()

# Filtra os repositórios que contêm a palavra no nome
repositorios_filtrados = [repo for repo in response['repositories'] if palavra_filtro in repo['repositoryName']]

# Imprime os nomes dos repositórios filtrados
for repo in repositorios_filtrados:
    print(repo['repositoryName'])
