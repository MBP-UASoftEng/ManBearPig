from app import db
import datetime

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    employee_id = db.Column(db.Integer, unique = True)
    active = db.Column(db.Boolean)
    classification = db.Column(db.String)
    password = db.Column(db.String)
    timestamp = db.Column(db.String)
    manager_id = db.Column(db.Integer, db.ForeignKey("employee.employee_id"), index = True, nullable = True)

    manager = db.relationship(lambda: Employee, remote_side=[employee_id], backref='underlings')
    transactions = db.relationship(lambda: Transaction, remote_side=[employee_id], backref='cashier')

    def __repr__ (self):
        return '<First Name %r>' % self.first_name

class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String)
    item_id = (db.Integer)
    item_lookup_code = db.Column(db.String, unique = True)
    price = db.Column(db.Float(precision=2, asdecimal=False, decimal_return_scale=None))
    item_type = db.Column(db.Integer)
    cost = db.Column(db.Float(precision=2, asdecimal=False, decimal_return_scale=None))
    quantity = db.Column(db.Float(precision=2, asdecimal=False, decimal_return_scale=None))
    reorder_point = db.Column(db.Float(precision=2, asdecimal=False, decimal_return_scale=None))
    restock_level = db.Column(db.Integer)
    parent_id = db.Column(db.Integer)
    extended_description = db.Column(db.String)
    inactive = db.Column(db.String)
    msrp = db.Column(db.Float(precision=2, asdecimal=False, decimal_return_scale=None))
    date_created = db.Column(db.String)

class TenderEntry(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    transaction_id = db.Column(db.Integer, db.ForeignKey('transaction.id'))
    tender_type = db.Column(db.String)
    amount= db.Column(db.Float(precision=2, asdecimal=False, decimal_return_scale=None), nullable=False)
    timestamp = db.Column(db.String)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    cashier_id = db.Column(db.Integer, db.ForeignKey('employee.employee_id'))
    amount = db.Column(db.Float(precision=2, asdecimal=False, decimal_return_scale=None), nullable=False)
    transaction_type = db.Column(db.String)
    parent_id = db.Column(db.Integer, db.ForeignKey('transaction.id'), nullable = True)
    timestamp = db.Column(db.String)

    parent_transaction = db.relationship(lambda: Transaction, remote_side=[id], backref='sub_transactions')
    tender_entries = db.relationship(lambda: TenderEntry, remote_side=[id], backref='tender_transaction')
    transaction_entries = db.relationship(lambda: TransactionEntry, remote_side=[id], backref='entry_transaction')

    def __repr__ (self):
        return '<Transaction ID %r>' % self.id

class TransactionEntry(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    transaction_id = db.Column(db.Integer, db.ForeignKey('transaction.id'))
    #product_id = db.Column(db.Integer, db.ForeignKey('product.item_id'))
    price = db.Column(db.Float(precision=2, asdecimal=False, decimal_return_scale=None))
    quantity = db.Column(db.Float(precision=2, asdecimal=False, decimal_return_scale=None))
