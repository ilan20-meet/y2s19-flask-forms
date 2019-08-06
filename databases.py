from model import Base, Comment

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///comments.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_comment(name, email, comment):
	"""
	Add a comment to the database, given
	their name, email, and the comment.
	"""
	comment_object = Comment(
		name=name,
		email=email,
		comment=comment)
	session.add(comment_object)
	session.commit()

def query_by_name(name):
	"""
	Find the first comment in the database,
	by their name
	"""
	comment = session.query(Comment).filter_by(
		name=name).first()
	return comment

def query_all():
	"""
	Print all the comments in the database.
	"""
	comments = session.query(Comment).all()
	return comments

def delete_comment_id(id_number):
	"""
	Delete comment with cetain id from the database.
	"""
	session.query(Comment).filter_by(
		id_num=id_number).delete()
	session.commit()

def delete_comment_name(name):
	"""
	Delete all commments with a certain name
	from the database.
	"""
	session.query(Comment).filter_by(
		name=name).delete()
	session.commit()

def query_by_id(id_num):
	"""
	find comment with certain id
	"""
	comment = session.query(Comment).filter_by(
        id_num=id_num).first()
	return comment
