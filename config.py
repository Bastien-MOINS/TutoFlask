#>>>import random, string, os
#>>>"".join([random.choice(string.printable) for _ in os.urandom(24) ] )
SECRET_KEY = "2lzUl{$*D6#`8uXqlU."
ABOUT = "Bienvenue sur la page à propos de Flask !"
CONTACT = "Vous pouvez me retrouver sur \n" \
            "Facebook: https://www.facebook.com/groups/1209157305791416/ \n" \
            "Flask's documentation: https://flask.palletsprojects.com/en/stable/"

import os
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'monApp.db')

BOOTSTRAP_SERVE_LOCAL = True