#!/usr/bin/env python
import os, argparse
import boto3
from botocore.exceptions import ClientError

parser = argparse.ArgumentParser(description='Upload file to s3')
parser.add_argument('-f', '--filename',
        type=str,
        required=True,
        help='File to upload')
parser.add_argument('-p', '--path',
        type=str,
        default='.',
        help='Path to file')

def s3_upload(filename=None, path='.'):
    if filename is None:
        args = parser.parse_args()
        filename = args.filename

    aws_id = os.environ.get('AWS_ACCESS_KEY_ID')
    aws_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
    aws_region = os.environ.get('AWS_DEFAULT_REGION') or 'us-east-2'
    aws_bucket = os.environ.get('AWS_BUCKET') or 'techofmany-db-backups'

    try:
        s3_client = boto3.client(
            service_name='s3',
            region_name=aws_region,
            aws_access_key_id=aws_id,
            aws_secret_access_key=aws_key,
        )
        response = s3_client.upload_file('%s/%s' % (path, filename), aws_bucket, filename)

        print('Uploaded to s3:', response)
    except ClientError as e:
        print(e)
