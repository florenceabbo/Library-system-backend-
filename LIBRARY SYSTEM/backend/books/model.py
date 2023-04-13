
from backend.db import db
class Book(db.Model):
    __tablename__='books'
    id = db.Column('book_id', db.Integer, primary_key=True)
    title= db.Column(db.String(50), unique =True)
    image = db.Column(db.String(50), nullable=True)
    price = db.Column(db.String(10), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    publish_date =db.Column(db.String(50))
    publish_year =db.Column(db.String(50))
   


    def __init__(self, id, title, image,price,description, publish_date,publish_year,user_id,publishing_company_id ):
        self.id =id
        self.title =title
        self.image =image
        self.price =price
        self.description = description
        self.publish_date = publish_date
        self.publish_year = publish_year
         

        def __repr__(self):
         return f"<Book {self.title} >"
  

        
   #save a new instance
        def save(self):
         db.session.add(self)
         db.session.commit()

   #delete the item
        def delete(self):
         db.session.delete(self)
         db.session.commit()

