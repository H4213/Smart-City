from model import modele 
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

	return render_template('marker.html', markers=mes_Markers)

def displayUser():

	users = User.query.all()

	return render_template('user.html', users = users)

def authentification(form):
	user = User.query.filter_by(pseudo=form.pseudo, passw=form.passw).first()
	return str(user.id)

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