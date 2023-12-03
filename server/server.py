from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)

CORS(app)

@app.route('/api/get_maritalk_response', methods=['POST'])
def get_maritalk_response():
   
    request_data = request.json

   
    if 'messages' not in request_data:
        return jsonify({"error": "Mensagens ausentes no corpo da requisição"}), 400

    messages = request_data['messages']

    
    request_data = {
        "messages": messages,
        "do_sample": True,
        'max_tokens': 200,
        "temperature": 0.7,
        "top_p": 0.95,
    }

   
    url_maritalk = 'https://chat.maritaca.ai/api/chat/inference'
    my_key = "107134730569760540352$f8fd7beb203bb30c8322eca7662c791c916a69dcb022a85d12a00c78d839a8d3"
    auth_header = {"authorization": f"Key {my_key}"}

   
    response = requests.post(url_maritalk, json=request_data, headers=auth_header)

  
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)

