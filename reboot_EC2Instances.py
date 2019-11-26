import boto3

def lambda_handler(event, context):

    ec2 = boto3.resource('ec2')
    print('list of ec2 instance', ec2)