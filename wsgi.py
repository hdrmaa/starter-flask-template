from starterPack import create_app
import sys

if __name__ == "__main__":
    path = "/var/www/webroot/ROOT"
    if path not in sys.path:
        sys.path.append(path)
    app = create_app()
    app.run()
