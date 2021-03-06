import logging
from flask import Flask, send_from_directory
from main.views import main_blueprint
from loader.views import loader_blueprint

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

logging.basicConfig(filename="log.txt",level=logging.INFO)

@app.route("/uploads/<path:path>")
def uploads_dir(path):
    return send_from_directory("uploads", path)

app.run()
