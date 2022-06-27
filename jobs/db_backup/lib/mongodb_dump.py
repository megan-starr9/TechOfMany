#!/usr/bin/env python
import os, argparse, subprocess, configparser

parser = argparse.ArgumentParser(description='Export mongo database to dump file')
parser.add_argument('-d', '--database',
        type=str,
        required=True,
        help='Mongo DB database')

def mongodb_dump(database=None):
    if database is None:
        args = parser.parse_args()
        database = args.database

    config_path = os.path.expanduser('~')+'/.mongo.cnf';
    if not os.path.exists(config_path):
        username = os.environ.get('MONGODB_USERNAME') or 'root'
        password = os.environ.get('MONGODB_PASSWORD') or ''
        hostname = os.environ.get('MONGODB_HOST') or 'mongo'
        port = os.environ.get('MONGODB_PORT') or 27017
        config_object = configparser.ConfigParser()
        config_object['mongodump'] = {
            'password': password,
            'uri': 'mongodb://%s:%s@%s:%s/%s' % (username, password, host, port, database),
        }

        with open(config_path, 'x') as conf:
            config_object.write(conf)

    filename = database + '_dump.gz'

    p = subprocess.Popen(
        'mongodump --config=%s --archive=%s --gzip' % (config_path, filename),
        stdout=subprocess.PIPE,
        shell=True
    )
    print('Dumping mongo database:', database, '>', filename)
    (output, err) = p.communicate()

    print('File created.')

    return filename
