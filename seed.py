from models import db, Pet
from app import app

# Create all tables
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Add pet
whiskey = Pet(name='Whiskey', species='dog', photo_url='', age='5', notes='I eat popcorn!', available=True)
fluffy = Pet(name='Fluffy', species='cat', photo_url='', age='10', notes='meoww', available=False )

db.session.add(whiskey)
db.session.add(fluffy)
# db.session.add(post1)
# db.session.add(post2)
# db.session.add(tag1)
# db.session.add(tag2)
# db.session.add(pt1)
# db.session.add(pt2)
# db.session.add(pt3)

# Commit--otherwise, this never gets saved!
db.session.commit()
