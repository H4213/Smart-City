#! /usr/bin/python
# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os
from flask import Flask, flash, render_template, request, session
from flask.ext.sqlalchemy import SQLAlchemy

from controler import control

from model.modele import User, Marker

app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def index():
  record = Marker.query.first()
  if record:
    print "test1"
  else:
    print "sdqg"
  return "Hi Bitches"

#Affichage des différents marqueurs enregistrés
@app.route('/marker')
@app.route('/marker/<cathegorie>')
def marker(cathegorie = None):
  return control.marker(cathegorie)

@app.route('/user')
def user():
  return control.displayUser()

#renvoie l'id après l'authentification de l'utilisateur
@app.route('/auth', methods=('GET', 'POST'))
def auth():
  return control.authentificaton(request.form)

#ajout d'un marqueur
@app.route('/add/marker', methods=('GET', 'POST'))
def addMarker():
  return control.addMarker(request.form)

#inscription d'un utilisateur
@app.route('/add/user', methods=('GET', 'POST'))
def addUser():
  return control.addUser(request.form)



#test
@app.route('/test', methods=('GET', 'POST'))
def test():
  if request.method == 'POST':
    return control.test(request.form)
  return "false"

"""@app.route('/test2', methods=('GET', 'POST'))
def test2():
  marker = Marker()
  marker.title = "le titre"

  db.session.add(marker)
  db.session.commit()

  return str(marker.id)"""


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
  app.run(debug=True)