import zmq
import requests

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

def lookup_meal_by_id(meal_id):
    url = "https://www.themealdb.com/api/json/v1/1/lookup.php?i=" + meal_id
    response = requests.get(url)

    if response.status_code == 200:
        
        data = response.json()
        ingredients_list = []
        count = 1
        while True:
            key = 'strIngredient' + str(count)
            ingredient = data['meals'][0].get(key)
            if ingredient and ingredient.strip() != "":
                ingredients_list.append(ingredient)
                count += 1
            else:
                break
    else:
        print("Failed to retrieve data from the API")
    
    return ingredients_list

while True:
    # Wait for request from Flask app
    request_data = socket.recv_json()

    # Extract meal_id and ingredients from the request data
    meal_id = request_data.get('meal_id')
    available_ingredients = request_data.get('ingredients', [])

    # Lookup meal details by ID
    shopping_list = lookup_meal_by_id(meal_id)

    # Iterate through ingredients and remove duplicates from meal_details
    for ingredient in available_ingredients:
        if ingredient in shopping_list:
            shopping_list.remove(ingredient)

    # Send the processed data back to Flask app
    socket.send_json({'shopping_list': shopping_list})
