from flask import Blueprint, request, jsonify
from controllers.character_controller import create_character

character_routes = Blueprint('character_routes', __name__)

@character_routes.route('/create-character', methods=['POST'])
def create_character_route():

  data = request.get_json()

  new_char, error = create_character(data)
  if error:
      return jsonify({"error": error}), 400
  return jsonify({
      "message": "Character created!",
      "character_id": new_char.id,
      "name": new_char.name,
      "health": new_char.health,
      "class_type": new_char.class_type,
      "strength": new_char.strength,
      "agility": new_char.agility,
      "intelligence": new_char.intelligence,
      "backstory": new_char.backstory,
      "image_url": new_char.image_url
  })