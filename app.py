#! /usr/bin/python
# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os
from flask import Flask, flash, render_template, request, session, jsonify
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
  print "user\n"
  return control.displayUser()

#renvoie l'id après l'authentification de l'utilisateur
@app.route('/auth', methods=('GET', 'POST'))
def auth():
  if request.method == 'POST':
    return control.authentificaton(request.form)
  return "false"

#ajout d'un marqueur
@app.route('/add/marker', methods=('GET', 'POST'))
def addMarker():
  if request.method == 'POST':
    return control.addMarker(request.form)
  return "false"

#inscription d'un utilisateur
@app.route('/add/user', methods=('GET', 'POST'))
def addUser():
  if request.method == 'POST':
    return control.addUser(request.form)
  return "false"



#test
@app.route('/test', methods=('GET', 'POST'))
def test():
  if request.method == 'POST':
    return control.test(request.form)
  return "false"

@app.route('/useer')
def displaye():
  users = Marker.query.all()
  return jsonify(users=[user.serialize() for user in users])

"""@app.route('/test2', methods=('GET', 'POST'))
def test2():
  marker = Marker()
  marker.title = "le titre"

  db.session.add(marker)
  db.session.commit()

  return str(marker.id)"""


"""@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404"""

if __name__ == '__main__':
  app.run(debug=True)
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port)