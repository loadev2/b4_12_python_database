import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import uuid

DB_PATH="sqlite:///sochi_athletes.sqlite3"
Base=declarative_base()

class User(Base):
	__tablename__ = "user"
	id=sa.Column(sa.INTEGER, primary_key=True)
	first_name=sa.Column(sa.TEXT)
	last_name=sa.Column(sa.TEXT)
	gender=sa.Column(sa.TEXT)
	email=sa.Column(sa.TEXT)
	birthdate=sa.Column(sa.TEXT)
	height=sa.Column(sa.REAL)


def add_new_user():
	user=User();
	#user.id=uuid.uuid4().int
	user.first_name=input("Enter first name: ")
	user.last_name=input("Enter last name: ")
	user.gender=checkGender(input("Enter gender (Male or Female): "))
	user.email=input("Enter email: ")
	user.birthdate=input("Enter date of birth (format yyyy-mm-dd): ")
	user.height=checkHeight(input("Enter height (format is x.xx): "))

	save_to_db(user)
	

def checkGender(gender):
	if gender.lower() in ['male', 'female']:
		return gender.lower().capitalize()
	else:
		return 'Unknown'

def checkHeight(value):
	try:
		newval=float(value)
		return newval
	except ValueError:
		return 0

def save_to_db(user):
	engine=sa.create_engine(DB_PATH)
	Sessions=sessionmaker(engine)
	session=Sessions()
	session.add(user)
	session.commit()

if __name__ == '__main__':
	add_new_user()