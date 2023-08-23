import boto3
#select your own region
region ='us-east-1'
#replace <name of instance with the name of your own instance
instances = ['<name of instance>']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event_context):
  ec2.start_instances(InstanceIds=instances)
  print('start your instances:' + str(instances))
