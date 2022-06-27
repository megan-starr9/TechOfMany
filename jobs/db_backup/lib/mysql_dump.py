#!/usr/bin/env python
import os, argparse, subprocess, configparser

parser = argparse.ArgumentParser(description='Export mysql database to dump file')
parser.add_argument('-d', '--database',
        type=str,
        required=True,
        help='MySQL database')

def mysql_dump(database=None):
    if database is None:
        args = parser.parse_args()
        database = args.database

    config_path = os.path.expanduser('~')+'/.my.cnf';
    if not os.path.exists(config_path):
        username = os.environ.get('MYSQL_USERNAME') or 'root'
        password = os.environ.get('MYSQL_PASSWORD') or ''
        config_object = configparser.ConfigParser()
        config_object['mysqldump'] = {
            'user': username,
            'password': password,
        }

        with open(config_path, 'x') as conf:
            config_object.write(conf)

    hostname = os.environ.get('MYSQL_HOST') or 'localhost'
    port = os.environ.get('MYSQL_PORT') or 3306
    filename = database + '_dump.sql.gz'

    p = subprocess.Popen(
        'mysqldump -h %s -P %s --no-tablespaces %s | gzip > %s' % (hostname, port, database, filename),
        stdout=subprocess.PIPE,
        shell=True
    )
    print('Dumping sql database:', database, '>', filename)
    (output, err) = p.communicate()

    print('File created.')

    return filename;
