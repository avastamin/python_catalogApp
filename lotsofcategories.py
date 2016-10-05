from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Catalog, Base, Item

engine = create_engine('sqlite:///catalogitem.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Menu for UrbanBurger
restaurant1 = Catalog(name="Urban Burger", slug="urbanburger")

session.add(restaurant1)
session.commit()

# Menu for UrbanBurger
restaurant1 = Catalog(name="Soccer", slug="soccer")

session.add(restaurant1)
session.commit()
# Menu for UrbanBurger
restaurant2 = Catalog(name="Table Tenis", slug="tabletenis")

session.add(restaurant2)
session.commit()
# Menu for UrbanBurger
restaurant3 = Catalog(name="Valley Ball",slug="valleyball")

session.add(restaurant3)
session.commit()

#menuItem1 = Item(name="New items", description="with garlic and parmesan",catalog=restaurant1)

#session.add(menuItem1)
#session.commit()

print "added menu items!"
