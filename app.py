from distutils.log import debug
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__) 
app.config['SECRET_KEY'] = "ABC-key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'

database = SQLAlchemy(app)


from routes import * 


if __name__ == '__main__':
    app.run(debug=True)