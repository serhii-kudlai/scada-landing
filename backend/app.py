"""
Entry point for the landing contact-form backend (Flask).
"""
import logging
from flask import Flask
from urls import bp

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

app = Flask(__name__)

app.register_blueprint(bp)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
