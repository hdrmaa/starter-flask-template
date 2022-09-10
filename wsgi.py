import sys
path = "/var/www/webroot/ROOT"
if path not in sys.path:
    sys.path.append(path)

from starterPack import create_app
application = create_app()
