from flask import Flask 



def create_app():
    app = Flask(__name__)

    from . import pet
    app.register_blueprint(pet.bp)

    from . import facts
    app.register_blueprint(facts.bp)

    return app




