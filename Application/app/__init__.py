from flask import Flask

app = Flask(__name__)

from Application.app import routes