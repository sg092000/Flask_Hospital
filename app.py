from flask import Flask
from flask_restful import Api
from flask import Flask, redirect, request
from views import HelloWorld
import models
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
#app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql+psycopg2://postgres:admin1234@localhost:5432/HospitalDB'
api = Api(app)

db = SQLAlchemy(app)


api.add_resource(HelloWorld,"/")

if __name__ == "__main__":
    app.run()
    
    


