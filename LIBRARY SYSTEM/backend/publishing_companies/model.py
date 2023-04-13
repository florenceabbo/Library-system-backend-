from backend.db import db

class PublishingCompany(db.Model):
    __tablename__='publishing_companies'
    id = db.Column('publishing_company_id', db.Integer, primary_key=True)
    name= db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(50), nullable=False)
    contact = db.Column(db.String(10), nullable=False)
    # books = db.relationship("Book",backref="publishing_company")
    
    def __init__(self, id, name, address,contact,user_id):
        self.id =id
        self.name =name
        self.address =address
        self.contact =contact
        # self.user_id = user_id

    def __repr__(self):
       return f"<PublishingCompany {self.name} >"
        