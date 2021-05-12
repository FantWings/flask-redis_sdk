from flask import Flask
from routes.index import index
from settings import FlaskConfig

app = Flask(__name__)
app.config.from_object(FlaskConfig)

app.register_blueprint(blueprint=index, url_prefix='/')

if __name__ == "__main__":
    app.run()
