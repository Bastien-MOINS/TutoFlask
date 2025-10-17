from .app import db
class Auteur(db.Model):
    idA = db.Column(db.Integer, primary_key=True)
    Nom = db.Column(db.String(100))

    def __repr__ (self):
        return "<Auteur (%d) %s>" % (self.idA , self.Nom)

def __init__(self, Nom):
    self.Nom = Nom

class Livre(db.Model):
    IdL = db.Column(db.Integer, primary_key=True)
    Prix = db.Column(db.Float())
    Titre = db.Column(db.String(255))
    Url = db.Column(db.String(255))
    Img = db.Column(db.String(255))

    auteur_id = db.Column (db.Integer , db.ForeignKey ("auteur.idA") )
    auteur = db.relationship ("Auteur", backref =db.backref ("livres", lazy="dynamic") )

    def __repr__ (self):
        return "<Livre (%d) %s>" % (self.IdL , self.Titre)

def __init__(self, id, prix, titre, url, img, auteur_id):
    self.IdL = id
    self.Prix = prix
    self.Titre = titre
    self.Url = url
    self.Img = img
    self.auteur_id = auteur_id

from flask_login import UserMixin

class User(db.Model, UserMixin):
    Login = db.Column (db.String(50), primary_key=True)
    Password = db.Column (db.String(64))

    def get_id(self):
        return self.Login