from config.db import db 

class Character(db.Model):
  __tablename__ = 'characters'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), nullable=False)
  class_type = db.Column(db.String(20), nullable=False)
  strength = db.Column(db.Integer, default=5)
  agility = db.Column(db.Integer, default=5)
  intelligence = db.Column(db.Integer, default=5)
  defence = db.Column(db.Integer, default=5)
  items = db.Column(db.Text, default="")
  health = db.Column(db.Integer, default=100)
  backstory = db.Column(db.Text, default="")
  image_url = db.Column(db.Text, default="")

  def __repr__(self):
    return f"<Character {self.name}>"


