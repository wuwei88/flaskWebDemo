from application import app, db, manager
from flask_script import Server, Command
from jobs.launcher import runJob
from www import *
import traceback
import sys

# web server
manager.add_command('runserver', Server(use_debugger=True, use_reloader=True))

manager.add_command("runjob", runJob)


# create_table
@Command
def create_all():
    from application import db
    from common.models.user import User
    db.create_all()


manager.add_command("create_all", create_all)


def main():
    manager.run()


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as e:
        traceback.print_exc()
