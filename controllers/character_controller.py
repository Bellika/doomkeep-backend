from models.Character import Character, db 

def create_character(data):
  class_type = data['class_type']
  stats = {
    "Barbarian": {"strength": 10, "agility": 5, "intelligence": 3, "defence": 8, "health": 130},
    "Wizard": {"strength": 3, "agility": 5, "intelligence": 10, "defence": 4, "health": 80},
    "Archer": {"strength": 6, "agility": 9, "intelligence": 5, "defence": 5, "health": 100},
    "Paladin": {"strength": 8, "agility": 6, "intelligence": 6, "defence": 10, "health": 120}
  }

  if class_type not in stats:
    return None, 'invalid class type'
  
  stats = stats[class_type]
  backstory = 'BACKSTORY'
  image_url = 'IMAGE_URL'

  new_char = Character(
    name=data['name'],
    class_type=class_type,
    health=stats['health'],
    strength=stats['strength'],
    agility=stats['agility'],
    intelligence=stats['intelligence'],
    backstory=backstory,
    image_url=image_url
  )

  db.session.add(new_char)
  db.session.commit()

  return new_char, None

