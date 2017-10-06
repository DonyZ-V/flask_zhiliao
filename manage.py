# -*- coding: utf-8 -*-

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_zhiliao import app
from exts import db
from models import User

manage = Manager(app)

# 使用Migrate绑定app和db
migrate = Migrate(app, db)

# 添加迁移脚本的命令到manager中
manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manage.run()