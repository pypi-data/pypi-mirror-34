import logging
import os
from _mysql import OperationalError

from tornado.options import options

import middleware
import config
from model import MiddlewareModel

config.initialize()

def create_db_structure():
    path = os.path.dirname(middleware.__file__)
    sqlFile = open(path + "/db/db_scheme.sql", "r")
    sql = sqlFile.read()
    sqlFile.close()
    # all SQL commands (split on ';')
    sqlCommands = sql.split(';')
    with MiddlewareModel.transaction() as cursor:
        for command in sqlCommands:
            # This will skip and report errors
            # For example, if the tables do not yet exist, this will skip over
            # the DROP TABLE commands
            try:
                cursor.execute(command)
            except OperationalError, msg:
                logging.warning("Command skipped: ", msg)