from backend.db import db

#Creating a model denoted by the class word and they should start with a capital letter
class User(db.Model):
    __tablename__ ='users'
    id = db.Column( 'user_id', db.Integer, primary_key=True)
    username = db.Column(db.String(50),unique=True, nullable=False)
    user_type=db.Column(db.String(50), nullable=False)
    gender=db.Column(db.String(10), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    contact = db.Column(db.String(12), unique=True, nullable=False)
    address = db.Column(db.String(50), nullable=False)
    password= db.Column(db.String(50))

    def __init__(self, username, user_type,gender, email, contact, address,password):
    
        self.username =username
        self.user_type =user_type
    
        self.gender =gender
        self.email =email
        self.contact =contact
        self.address =address
        self.password =password



    def __repr__(self):
        return f"<User{self.email}>" 
    
    #save a new instance
    def save(self):
        db.session.add(self)
        db.session.commit()


    def delete(self):
        db.session.delete(self)
        db.session.commit()