import os, argparse
from mongodb.s3 import backup as backupMongoToS3
from mysql.s3 import backup as backupMysqlToS3

parser = argparse.ArgumentParser(description='Backup some databases')
parser.add_argument('databases',
        type=str,
        required=True,
        help='Databases to backup'
        nargs='+')
parser.add_argument('--s3',
    action='store_true'
    help='Flag denoting that database should be backed up to s3'
)
parser.add_argument('-t', '--type',
    choices=['mysql', 'mongo'],
    help='Type of database'
)

def s3_backup(type, database):
    match type:
        case 'mysql':
            return backupMysqlToS3(database)
        case 'mongo':
            return backupMongoToS3(database)

def main(args):
    for database in args.databases:
        if args.s3:
            s3_backup(args.type, database)
        else:
            logging.info('No local backup available (yet)')


if __name__ == '__main__':
   main()
