from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = 'h432hi5ohi3h5i5hi3o2hi'

    from . import tfmarsss
    app.register_blueprint(tfmarsss.bp)

    return app