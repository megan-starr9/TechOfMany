import os, argparse, logging
from lib.mongodb_dump import mongodb_dump
from lib.mysql_dump import mysql_dump
from lib.s3_upload import s3_upload

parser = argparse.ArgumentParser(description='Backup some databases')
parser.add_argument('databases',
    type=str,
    help='Databases to backup',
    nargs='+'
)
parser.add_argument('--s3',
    action='store_true',
    help='Flag denoting that database should be backed up to s3'
)
parser.add_argument('-t', '--type',
    choices=['mysql', 'mongo'],
    help='Type of database'
)

def create_dump_file(type, database):
    match type:
        case 'mysql':
            return mysql_dump(database)
        case 'mongo':
            return mongodb_dump(database)

def main():
    args = parser.parse_args()
    for database in args.databases:
        filename = create_dump_file(args.type, database)
        if args.s3:
            s3_upload(filename)
        else:
            logging.info('No local backup available (yet)')


if __name__ == '__main__':
   main()
