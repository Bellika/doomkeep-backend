from models.Character import Character, db 
import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_image(backstory):
  response = openai.images.generate(
    model="dall-e-3",
    prompt=f"Make an image of the character told about in this story, the setting is dark-fantasy: {backstory}. The image should only be of the character holding some type of weapon. Make it in the style of a 90s videogame. There should be no text in the image",
    size="1024x1024",
    quality="standard",
    n=1
  )
  return response.data[0].url

def generate_backstory(name, class_type):
  prompt = f"""
    Create a dark fantasy backstory for a character named {name},
    who is a {class_type}. The setting of the game is a cursed, dark fortress
    that has appeared in a forest. The player must enter this fortress to
    defeat the evil within. The story should have a grim dark, 90s Souls-like fantasy tone.
    The backstory should explain the character's past and motivations, how they
    came to face this dark fortress, and what they seek inside. It should 
    build tension and describe the foreboding atmosphere of the fortress. 
    The story should end with the character standing at the entrance of the 
    fortress, preparing for the final challenge ahead. Also write a visual description
    of the character. Write in plain text and dont use any special characters.
  """

  response = openai.chat.completions.create(
    model='gpt-4o',
    messages=[
      {'role': 'system', 'content': 'You are a skilled fantasy storyteller'},
      {'role': 'user', 'content': prompt}
    ],
    temperature=0.8,
  )
  return response.choices[0].message.content.strip()

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
  backstory = generate_backstory(data['name'], class_type)
  image_url = generate_image(backstory)

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

