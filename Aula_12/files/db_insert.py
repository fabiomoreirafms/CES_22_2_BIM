from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from . import dbdeclarative

engine = create_engine('sqlite:///dbfile.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
dbdeclarative.Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Insert a Person in the person table
new_file = dbdeclarative.File(name='new file')
session.add(new_file)
session.commit()
