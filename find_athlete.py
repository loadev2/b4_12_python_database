import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from users import User
from datetime import date

DB_PATH="sqlite:///sochi_athletes.sqlite3"
Base=declarative_base()

class Athelete(Base):

	__tablename__="athelete"
	id=sa.Column(sa.Integer, primary_key=True)
	name=sa.Column(sa.TEXT)
	height=sa.Column(sa.TEXT)
	birthdate=sa.Column(sa.TEXT)

def find_ath():
	idus=input("Enter user id: ")
	session=connect_db()
	user=session.query(User).filter(User.id==int(idus)).first()
	if user is None:
		print("There is no user with id "+idus)
		return
	ath_height_right=session.query(Athelete).order_by(Athelete.height).filter(Athelete.height>=user.height).first()
	ath_height_left=session.query(Athelete).order_by(Athelete.height.desc()).filter(Athelete.height<user.height).first()

	ath_height=None
	if ath_height_right is None:
		ath_height=ath_height_left
	elif ath_height_left is None:
		ath_height=ath_height_right
	elif (ath_height_right.height-user.height)<(user.height-ath_height_left.height):
		ath_height=ath_height_right
	else:
		ath_height=ath_height_left

	print("The closest to user's height athelete is {}. Height is {}.".format(ath_height.name,ath_height.height))

	ath_date_right=session.query(Athelete).order_by(Athelete.birthdate).filter(Athelete.birthdate>=user.birthdate).first()
	ath_date_left=session.query(Athelete).order_by(Athelete.birthdate.desc()).filter(Athelete.birthdate<user.birthdate).first()

	ath_date=None
	
	if ath_date_right is None:
		ath_date=ath_date_left
	elif ath_date_left is None:
		ath_date=ath_date_right
	elif (date.fromisoformat(ath_date_right.birthdate)-date.fromisoformat(user.birthdate))<(date.fromisoformat(user.birthdate)-date.fromisoformat(ath_date_left.birthdate)):
		ath_date=ath_date_right
	else:
		ath_date=ath_date_left

	print("The closest to user's date of birth athelete is {}. Date is {}.".format(ath_date.name,ath_date.birthdate))
	


def connect_db():
	engine=sa.create_engine(DB_PATH)
	Base.metadata.create_all(engine)
	Session=sessionmaker(engine)
	return Session()

if __name__ == "__main__":
	find_ath()