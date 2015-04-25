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
	user = User.query.filter_by(pseudo=form.pseudo, passw=form.passw).first()
	if user:
		return str(user.id)
	return "-1"

def addMarker(form):
	if (form.title and form.user and form.lng and form.lat):
		exist = Marker.query.filter_by(title=form.title, lng=form.lng, lat=form.lat).first()

		if exist:
			return "Already Exist"
		marker = Marker(form.idUser, form.title, form.cathegorie, form.description, form.lng, form.lat)

		db.session.add(marker)
		db.commit()

		return marker.id 
		
	return "Invalid Parameters"

def addUser(form):
	if (form.pseudo and form.password):
		exist = User.query.filter_by(pseudo=form.pseudo).first()

		if exist:
			return "Already Exist"
		user = User(form.pseudo, form.password)

		db.session.add(user)
		db.commit()

		return user.id 

	return "Invalid Parameters"



def test(form):
	return form['name']

"""def paiment():"""