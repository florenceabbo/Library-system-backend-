from flask import jsonify, request, Blueprint

from werkzeug.security import check_password_hash,generate_password_hash
from backend.publishing_companies.model import PublishingCompany
from backend.db import db


# Creating a blue print for users, where users is the resource
publishing_companies = Blueprint('users',__name__,url_prefix='/publishing_companies')

#Getting all Users
@publishing_companies.route("/")
def all_publishing_companies():
    publishing_companies = publishing_companies.querry.all()
    results =[
        {
        "id":company.id,
        "name":company.name,
        "addres":company. addres,
        "contact":company.contact,
        "user_id":company.user_id
        
        } for company in publishing_companies
    ]
    return{"count": len(results), "publishing_companies": results}

