from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the programmer table
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


class FavouriteCountry(base):
    __tablename__ = "Favourite Countries"
    id = Column(Integer, primary_key=True)
    country_name = Column(String)
    country_capital_city = Column(String)
    country_currency = Column(String)
    country_food = Column(String)
    famous_for = Column(String)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# creating record on our programmer table
ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender="F",
    nationality="British",
    famous_for="First Programmer"
)

alan_turing = Programmer(
    first_name="Alan",
    last_name="Turing",
    gender="M",
    nationality="British",
    famous_for="Modern Computing"
)

grace_hopper = Programmer(
    first_name="Grace",
    last_name="Hopper",
    gender="F",
    nationality="American",
    famous_for="COBOL language"
)

margaret_hamilton = Programmer(
    first_name="Margaret",
    last_name="Hamilton",
    gender="F",
    nationality="American",
    famous_for="Apollo 11"
)

bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="American",
    famous_for="Microsoft"
)

tim_berners_lee = Programmer(
    first_name="Tim",
    last_name="Berners-Lee",
    gender="M",
    nationality="British",
    famous_for="World Wide Web"
)

gemma_sayers = Programmer(
    first_name="Gemma",
    last_name="Sayers",
    gender="F",
    nationality="British",
    famous_for="Enjoying the small things!"
)

italy = FavouriteCountry(
    country_name="Italy",
    country_capital_city="Rome",
    country_currency="Euro",
    country_food="Pizza",
    famous_for="Food, architechture and cars"
)

greece = FavouriteCountry(
    country_name="Greece",
    country_capital_city="Athens",
    country_currency="Euro",
    country_food="Calamari, Lamb, fish, salad",
    famous_for="Food, hospitality, beautiful islands, historical architecture"
)

fakey = FavouriteCountry(
    country_name="Not a real country",
    country_capital_city="Anywhere",
    country_currency="Monopoly",
    country_food="flower burgers",
    famous_for="Not existing"
)

# add each instance of our countries to our session
# session.add(italy)
# session.add(greece)
session.add(fakey)

# add each instance of our programmers to our session
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(gemma_sayers)
# add each of the programmers to our session



# updating a single record - using .first() means avoiding having to yse a for -loop for the iteration
# programmer = session.query(Programmer).filter_by(id=7).first()
# programmer.famous_for = "Budget cooking!"

# commit session to the db
# session.commit()

# updating multiple records
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
#     session.commit()


# deleting a single record
# fname = input("Enter a first name: ")
# lname = input("Enter a last name: ")
# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
# # defensive programming
# if programmer is not None:
#     print("Programmer found: ", programmer.first_name + " " + programmer.last_name)
#     confirmation = input("Are you sure you want to delete this record? (y/n) ")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer has been deleted")
#     else:
#         print("Programmer not deleted")
# else:
#     print("No records found")


# # query the db to find all the programmers
# programmers = session.query(Programmer)
# for programmer in programmers:
#     print(
#         programmer.id,
#         programmer.first_name + " " + programmer.last_name,
#         programmer.gender,
#         programmer.nationality,
#         programmer.famous_for,
#         sep=" | "
#     )

# country = session.query(FavouriteCountry).filter_by(id=1).first()
# country.famous_for = "Roman History, food, cars, wine, la dolce vita"

# commit session to the db
# session.commit()

# # query the db to find all the countries
countries = session.query(FavouriteCountry)
for country in countries:
    print(
        country.id,
        country.country_name,
        country.country_capital_city,
        country.country_currency,
        country.country_food,
        country.famous_for,
        sep=" | "
    )


