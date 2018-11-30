from flask import Flask

app = Flask(__name__)

from app import routes  # bottom import is a workaround to circular imports
