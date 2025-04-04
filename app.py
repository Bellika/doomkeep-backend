from flask import Flask 
from config.db import db, get_database_uri

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = get_database_uri()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/ping')
def ping():
  return 'Server is running'

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)