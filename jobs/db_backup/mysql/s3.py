#!/usr/bin/env python
import os, argparse
import boto3
from botocore.exceptions import ClientError

parser = argparse.ArgumentParser(description='Backup mysql database to s3')
parser.add_argument('-d', '--database',
        type=str,
        required=True,
        help='MySQL database')

def backup(args):
    db = args.database

    aws_id = os.environ.get('AWS_ACCESS_KEY_ID')
    aws_key = os.environ.get('AWS_SECRET_ACCESS_KEY')

    if aws_id is None or aws_key is None:
        raise Exception('AWS credentials must be provided in the ENV')

    username = os.environ.get('MYSQL_USERNAME') or 'root'
    password = os.environ.get('MYSQL_PASSWORD') or ''
    hostname = os.environ.get('MYSQL_HOST') or 'localhost'
    port = os.environ.get('MYSQL_PORT') or 3306
    filename = db + '_dump.sql.gz'

    backup_output = subprocess.check_output([
        'mysqldump',
        '-h', '%s' % hostname,
        '-P', '%s' % port,
        '-u', '%s' % username,
        '-p', '%s' % password,
        '%s | gzip > %s' % (db, filename),
    ])

    logging.info('File created:', backup_output)

    aws_region = os.environ.get('AWS_DEFAULT_REGION') or 'us-east-2'
    aws_bucket = os.environ.get('AWS_BUCKET') or 'techofmany-db-backups'

    try:
        s3_client = boto3.client(
            service_name='s3',
            region_name=aws_region,
            aws_access_key_id=aws_id,
            aws_secret_access_key=aws_secret,
        )
        response = s3_client.upload_file(filename, aws_bucket)

        print('Uploaded to s3:', response)
    except ClientError as e:
        print(e)
