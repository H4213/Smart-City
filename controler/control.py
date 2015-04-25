from model import modele
from model.modele import User, Marker
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def connectToDatabase():
    """
    Connect to our SQLite database and return a Session object
    """
    session = modele.db
    return session

db = connectToDatabase()

def marker(cathegorie):
	"""
	request for all markers
	"""
	if (cathegorie):
		mes_Markers = Marker.query.filter_by(cathegorie=cathegorie).all()
	else:
		mes_Markers = Marker.query.all()

	if mes_Markers:
		return render_template('marker.html', markers=mes_Markers)
	return "-1"

def displayUser():
	print "displayUser()\n"

	users = User.query.all()

	print "query faite"

	if users :
		print "users non vide\n"
		return render_template('user.html', users = users)

	print "user vide\n"
	return "-1"

	

def authentification(form):
	user = User.query.filter_by(pseudo=form['pseudo'], passw=form['passw']).first()
	if user:
		return str(user.id)
	return "-1"

def addMarker(form):
	if (form['title'] and form['user'] and form['lng'] and form['lat']):
		exist = Marker.query.filter_by(title=form['title'], lng=form['lng'], lat=form['lat']).first()

		if exist:
			return "Already Exist"
		marker = Marker(form['idUser'], form['title'], form['cathegorie'], form['description'], form['lng'], form['lat'])

		db.session.add(marker)
		db.session.commit()

		return marker.id 
		
	return "Invalid Parameters"

def addUser(form):
	print "1"
	if (form['pseudo'] and form['passw']):
		print "2"
		exist = User.query.filter_by(pseudo=form['pseudo']).first()
		print "3"
		if exist:
			print "4"
			return "Already Exist"
		print "5"
		user = User(form['pseudo'], form['passw'])

		print "6"

		db.session.add(user)

		print "6.2"
		db.session.commit()

		print "7"

		return str(user.id) 

	return "Invalid Parameters"



def test(form):
	return form['name']

"""def paiment():"""