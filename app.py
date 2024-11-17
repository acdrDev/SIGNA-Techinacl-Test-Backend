import os
from flask import Flask
from dotenv import load_dotenv
from routes.BrandRoutes import brands_bp
from flask_cors import CORS


if os.getenv('ENVIRONMENT') != 'docker':
  load_dotenv()

app = Flask(__name__)
CORS(app)

app.register_blueprint(brands_bp)

if __name__ == '__main__':
  app.run(host='0.0.0.0' ,port=5000, debug=True)