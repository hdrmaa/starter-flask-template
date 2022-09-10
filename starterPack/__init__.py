from flask import Flask

def create_app():
    app = Flask(__name__)

    # Main routes
    from starterPack.main_routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
