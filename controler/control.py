from model import modele
from model.modele import User, Marker
from flask import Flask, flash, render_template, request, session
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

	if not(mes_Markers):
		print "Markers vides"

	return render_template('marker.html', markers=mes_Markers)

def displayUser():
	print "displayUser()"

	users = User.query.all()

	for user in users:
		print user.pseudo

	print "query faite"

	if users :
		print "users non vide"
		return render_template('user.html', users = users)

	print "user vide"
	return "-1"

	

def authentification(form):
	user = User.query.filter_by(pseudo=form['pseudo'], passw=form['passw']).first()
	if user:
		return str(user.id)
	return "-1"

def addMarker(form):
	print "addMarker"
	if (form['title'] and form['user'] and form['lng'] and form['lat']):
		exist = Marker.query.filter_by(title=form['title'], lng=form['lng'], lat=form['lat']).first()
		
		if exist:
			return "Already Exist"

		user = User.query.get(form['user'])

		if not(user):
			return "User doesn't exist"
		
		marker = Marker(form['title'], float(form['lng']), float(form['lat']), form['user'], form['cathegorie'], form['description'])
		
		db.session.add(marker)
		db.session.commit()
		

		return str(marker.id) 
		
	return "Invalid Parameters"

def addUser(form):
	if (form['pseudo'] and form['passw']):

		exist = User.query.filter_by(pseudo=form['pseudo']).first()

		if exist:
	
			return "Already Exist"

		user = User(form['pseudo'], form['passw'])

		db.session.add(user)
		db.session.commit()

		return str(user.id) 

	return "Invalid Parameters"



def test(form):
	return form['name']

"""def paiment():"""