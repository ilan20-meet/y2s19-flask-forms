from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Comment(Base):
	"""
	Create a commentss table. This table has
	4 columns.

	The first column, id_num is
	the primary key for the table. The second
	column is a string, representing the name of
	the user. The third column is a string representing the email of the user.
	The last column is a string representing the comment of the user.
	"""
	__tablename__ = 'comment'
	id_num = Column(Integer, primary_key=True)
	name = Column(String)
	email = Column(String)
	comment = Column(String)

	def __repr__(self):
		return ("User Name: {}\n"
				"User Email: {} \n"
				"Comment: {}").format(
					self.name,
					self.email,
					self.comment)


