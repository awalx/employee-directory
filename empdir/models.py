from datetime import datetime
from empdir import db

class Employees(db.Model):
    EmployeeId = db.Column(db.Integer, primary_key=True)
    LastName = db.Column(nullable=False)
    FirstName = db.Column(nullable=False)
    Title = db.Column()
    ReportsTo = db.Column(db.Integer, db.ForeignKey('Employees.EmployeeID'))
    BirthDate = db.Column(db.DateTime, default=datetime.utcnow)
    HireDate = db.Column(db.DateTime, default=datetime.utcnow)
    Address = db.Column()
    City = db.Column()
    State = db.Column()
    Country = db.Column()
    PostalCode = db.Column()
    Phone = db.Column()
    Fax = db.Column()
    Email = db.Column()

    def __repr__(self):
        return '<Employees> {id}, {lastname}, {firstname}'.format(id=self.EmployeeId, lastname=self.LastName, firstname=self.FirstName)


