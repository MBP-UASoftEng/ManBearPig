from app import db, models

manager = models.Employee(first_name = "test", last_name = "test")

#Add the created entry to the table
db.session.add(manager)
db.session.commit()

test = models.Employee(first_name = "test1", last_name = "test1", manager_id= manager.id)

#Add the created entry to the table
db.session.add(test)
db.session.commit()
