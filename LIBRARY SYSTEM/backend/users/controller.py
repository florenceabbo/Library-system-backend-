# Register a new user
from flask import jsonify, request, Blueprint

from werkzeug.security import check_password_hash,generate_password_hash
from backend.users.model import User
from backend.db import db


# Creating a blue print for users, where users is the resource
users = Blueprint('users',__name__,url_prefix='/users')

#Getting all Users
@users.route("/")
def all_users():
    users = User.query.all()
    results =[
        {
        "id":user.id,
        "username":user.username,
        "user_type":user.user_type,
        "gender":user.gender,
        "email":user.email,
        "contact":user.contact,
        "address":user.address
        
        } 
        for user in users
    ]
    return{"count": len(results), "users": results}

#creating a new user using request.json
@users.route('/create',methods=['POST','GET'])
def create_user():
    user_name= request.json['name']
    gender=request.json['gender']
    user_email= request.json['email']
    user_contact= request.json['contact']
    user_address= request.json['address']
    user_type= 'author'
    user_password= request.json['password']
    hashed_password = generate_password_hash

    #validations
    if not user_name:
        return jsonify({'Message':'Username is required'}),400
    
    if not user_email:
        return jsonify({'Message':'Useremail is required'}),400
    
    if not user_contact:
        return jsonify({'Message':'Usercontact is required'}),400
    
    if not user_address:
        return jsonify({'Message':'Useraddress is required'}),400
    if not gender:
        return jsonify({'Message':'gender is required'}),400
    
    
    if not user_password:
        return jsonify({'Message':'User password is required'}),400
    if len (user_password )<6:
        return jsonify({'Message':'Password must be atleast 6 charaters'}),400
    
    #adding a validation on email that exsists to avoid depulications
    if User.query.filter_by(email=user_email).first():
        return jsonify({'Message':"Useremail already exsists"})
    
    exsisting_user_contact = User.query.filter_by(contact =user_contact).first()
    if exsisting_user_contact:
        return jsonify({'Message':'This contact is already in use'}),400
    
    #storing new user
    new_user= User(username=user_name, email=user_email, contact=user_contact,user_type=user_type, address=user_address,gender=gender,password=hashed_password )
    
    #adding the stored user to the database
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'Success':True, 'Message':'You have successfully created an account','data':new_user}),201
   