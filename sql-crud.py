from sqlalchemy import(
	create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from our localhost "chinook" db
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class based model for the "Programmer" table
# class Programmer(base):
# 	__tablename__ = "Programmer"
# 	id = Column(Integer, primary_key=True)
# 	first_name = Column(String)
# 	last_name = Column(String)
# 	gender = Column(String)
# 	nationality = Column(String)
# 	famous_for = Column(String)

# create a class based model for the "Guitarist" table
class Guitarist(base):
	__tablename__ = "Guitarist"
	id = Column(Integer, primary_key=True)
	first_name = Column(String)
	last_name = Column(String)
	nationality = Column(String)
	genre = Column(String)
	chosen_axe = Column(String)
	famous_for = Column(String)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)


# creating records on our Programmer table
# ada_lovelace = Programmer(
# 	first_name = "Ada",
# 	last_name = "Lovelace",
# 	gender = "F",
# 	nationality = "British",
# 	famous_for = "First Programmer"
# )

# alan_turing = Programmer(
# 	first_name = "Alan",
# 	last_name = "Turing",
# 	gender = "M",
# 	nationality = "British",
# 	famous_for = "Modern Computing"
# )

# grace_hopper = Programmer(
# 	first_name = "Grace",
# 	last_name = "Hopper",
# 	gender = "F",
# 	nationality = "American",
# 	famous_for = "COBOL language"
# )

# margaret_hamilton = Programmer(
# 	first_name = "Margaret",
# 	last_name = "Hamilton",
# 	gender = "F",
# 	nationality = "American",
# 	famous_for = "Apollo 11"
# )

# bill_gates = Programmer(
# 	first_name = "Bill",
# 	last_name = "Gates",
# 	gender = "M",
# 	nationality = "American",
# 	famous_for = "Microsoft"
# )

# tim_berners_lee = Programmer(
# 	first_name = "Tim",
# 	last_name = "Berners-Lee",
# 	gender = "M",
# 	nationality = "British",
# 	famous_for = "World Wide Web"
# )

# matthew_cleghorn = Programmer(
# 	first_name = "Matthew",
# 	last_name = "Cleghorn",
# 	gender = "M",
# 	nationality = "British",
# 	famous_for = "We shall see"
# )

# creating records on our Programmer table
jerry_reed = Guitarist(
	first_name = "Jerry",
	last_name = "Reed",
	nationality = "American",
	genre = "Country / Fingerstyle",
	chosen_axe = "Baldwin nylon string acoustic",
	famous_for = "Guitar Man"
)

larry_carlton = Guitarist(
	first_name = "Larry",
	last_name = "Carlton",
	nationality = "American",
	genre = "Jazz Rock",
	chosen_axe = "Gibson ES335",
	famous_for = "Steely Dan's Kid Charlemagne"
)

django_reinhardt = Guitarist(
	first_name = "Django",
	last_name = "Reinhardt",
	nationality = "Belgian",
	genre = "Gypsy Jazz",
	chosen_axe = "Selmer #503",
	famous_for = "Minor Swing"
)

tommy_emmanuel = Guitarist(
	first_name = "Tommy",
	last_name = "Emmanuel",
	nationality = "Australian",
	genre = "Fingerstyle",
	chosen_axe = "Maton 808",
	famous_for = "His rendition of Mason Williams' Classical Gas"
)

tony_rice = Guitarist(
	first_name = "Tony",
	last_name = "Rice",
	nationality = "American",
	genre = "Bluegrass",
	chosen_axe = "Martin D-18",
	famous_for = "Church Street Blues"
)

julian_lage = Guitarist(
	first_name = "Julian",
	last_name = "Lage",
	nationality = "American",
	genre = "Jazz",
	chosen_axe = "Fender Telecaster",
	famous_for = "Nocturne"
)

matthew_cleghorn = Guitarist(
	first_name = "Matthew",
	last_name = "Cleghorn",
	nationality = "British",
	genre = "Rock",
	chosen_axe = "Fender Telecaster",
	famous_for = "I Wanna Know More"
)

# add each instance of programmers to our session
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(matthew_cleghorn)

# commit our session to the database
# session.commit()

# add each instance of guitarists to our session
# session.add(jerry_reed)
# session.add(larry_carlton)
# session.add(django_reinhardt)
# session.add(tommy_emmanuel)
# session.add(tony_rice)
# session.add(julian_lage)
# session.add(matthew_cleghorn)




# updating a single record
# programmer = session.query(Programmer).filter_by(id=8).first()
# programmer.famous_for = "World President"

# updating a single record
# guitarist = session.query(Guitarist).filter_by(id=7).first()
# guitarist.famous_for = "Multi-instrumental prowess"

# commit our session to the database
# session.commit()


# updating multiple records
# people = session.query(Programmer)
# for person in people:
# 	if person.gender == "F":
# 		person.gender = "Female"
# 	elif person.gender == "M":
# 		person.gender="Male"
# 	else:
# 		print("Gender not defined")	
# 	session.commit()

# updating multiple records
# people = session.query(Guitarist)
# for person in people:
# 	if person.gender == "F":
# 		person.gender = "Female"
# 	elif person.gender == "M":
# 		person.gender="Male"
# 	else:
# 		print("Gender not defined")	
# 	session.commit()



# deleting a single record
# fname = input("Enter a first name: ")
# lname = input("Enter a last name: ")
# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
# defensive programming
# if programmer is not None:
# 	print("Programmer Found: ", programmer.first_name + " " + programmer.last_name)
# 	confirmation = input("Are you sure you want to delete this record? (y/n) ")
# 	if confirmation.lower() == "y":
# 		session.delete(programmer)
# 		session.commit()
# 		print("Programmer has been deleted")
# 	else:
# 		print("Programmer not deleted")
# else:
# 	print("No records found")

# query the database to find all programmers
# programmers = session.query(Programmer)
# for programmer in programmers:
# 	print(
# 		programmer.id,
# 		programmer.first_name + " " + programmer.last_name,
# 		programmer.gender,
# 		programmer.nationality,
# 		programmer.famous_for,
# 		sep=" | "
# 	)

# query the database to find all guitarists
guitarists = session.query(Guitarist)
for guitarist in guitarists:
	print(
		guitarist.id,
		guitarist.first_name + " " + guitarist.last_name,
		guitarist.nationality,
		guitarist.genre,
		guitarist.chosen_axe,
		guitarist.famous_for,
		sep=" | "
	)