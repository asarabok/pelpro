from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import app, db
from app.management.load_fixture import LoadFixture

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('load_fixture', LoadFixture())
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()