This microservice is a Python-based server that generates a shopping list based on the ingredients needed for the meal and the available ingredients provided by the user. It utilizes ZeroMQ (ZMQ) for communication between the server and the client and interacts with TheMealDB API to fetch meal details as JSON data.

# Features:
* The application can retrieve meal details from TheMealDB API by providing the meal_ID.
* Generates a shopping list by comparing the required ingredients for the meal with the available ingredients provided by the user.
* Ensures that the shopping list does not contain duplicate ingredients.

# Requirements:
* Python 3.x
* ZeroMQ (ZMQ) library (pip install pyzmq)
* Requests library (pip install requests)

# Install requirements:
```
pip install -r requirements.txt
```

# Usage:
* Start the server by running the server.py script:

```
python server.py
```

* The server will start listening for requests on tcp://*:5555.
* To request a shopping list for a meal, send a JSON request containing the meal ID and available ingredients to the server using a client application.
* Upon receiving the request, the server will fetch the meal details from TheMealDB API and generate a shopping list based on the available ingredients provided.
* The server will then send the shopping list back to the client.

# Example Client Implementation:
Below is an example implementation of a client application in Python using ZeroMQ to communicate with the server:

```
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# Example request data
request_data = {'meal_id': '52772', 'ingredients': ['Rice', 'Chicken', 'Onion']}

# Send request to server
socket.send_json(request_data)

# Receive response from server
response = socket.recv_json()

# Print shopping list
# Check if response contains an error message
if 'error' in response:
    print("Error:", response['error'])
else:
    print("Shopping List:")
    for item in response['shopping_list']:
        print(item)

# Close socket
socket.close()
```

![UML diagram](uml-diagram.png)

# Disclaimer:
This application is for educational purposes only and should not be used in production environments without proper testing and validation. TheMealDB API usage is subject to their terms and conditions.
