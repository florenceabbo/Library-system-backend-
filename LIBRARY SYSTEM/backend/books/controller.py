from flask import jsonify, request, Blueprint

from werkzeug.security import check_password_hash,generate_password_hash
from backend.books.model import Book
from backend.db import db


# Creating a blue print for users, where users is the resource
books = Blueprint('books',__name__,url_prefix='/books')

#Getting all Users
@books.route("/books")
def all_users():
    books = Book.querry.all()
    results =[
        {
        "id":book.id,
        "title":book.title,
        "image":book.image,
        "price":book.price,
        "description":book.description,
        "publish_date":book.publish_date,
        " publish_year":book. publish_years,
       
        
        } for book in books
    ]
    return{"count": len(results), "books": results}

#creating a new book using request.json
@books.route('/create',methods=['POST','GET'])
def create_book():
    book_title= request.json['title']
    book_image= request.json['image']
    book_price= '50000'
    book_description= request.json['description']
    book_publish_date = ['publish_date']
    book_publish_year= request.json['publish_year']
    


    #validations
    if not  book_title:
        return jsonify({'Message':'Book title is required'}),400
    
    if not book_image:
        return jsonify({'Message':'Book image is not so necessary'}),400
    
    if not book_price:
        return jsonify({'Message':'Usercontact is required'}),400
    
    if not book_description:
        return jsonify({'Message':'book description is required'}),400
    
    
    if not book_publish_date:
        return jsonify({'Message':'book publish date is required'}),400
    if not book_publish_year:
        return jsonify({'Message':'book publish year is required'}),400
 
    
    #adding a validation on email that exsists to avoid depulications
    if Book.query.filter_by(title=book_title).first():
        return jsonify({'Message':"That book already exsists"})
    
    #storing new user
    new_book= Book(id=id,title=book_title, image=book_image, price=book_price,description= book_description,publish_date=book_publish_date,publish_year=book_publish_year)
    
    #adding the stored user to the database
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'Success':True, 'Message':'You have successfully added a new book','data':new_book}),201
   