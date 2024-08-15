import boto3

def main():

    aws_profile = '987654321_x'  
    aws_region = 'sa-east-1'

    session = boto3.Session(profile_name=aws_profile)
    batch_client = session.client('batch', region_name=aws_region)    

    # Job Params
    job_definition = 'batch-xyz'
    job_name = 'TestRunJob'
    job_queue = 'batch-queue'
    container_overrides = {
        'environment': [
            {
                'name': 'id_list_env_example',
                'value': '1,2,3,4',
            }
        ]
    }
    
    response = batch_client.submit_job(
        jobDefinition=job_definition,
        jobName=job_name,
        jobQueue=job_queue,
        containerOverrides=container_overrides
    )

    print(response)

if __name__ == '__main__':
    main()
