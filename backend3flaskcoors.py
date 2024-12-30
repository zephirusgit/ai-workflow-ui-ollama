from flask import Flask, request, Response
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app)  # Habilitar CORS en la aplicación

OLLAMA_URL = 'http://localhost:11434/api/generate'

@app.route('/api/query', methods=['POST'])
def query_ollama():
    data = request.json
    payload = {
        "model": data.get("model", "llama3"),
        "prompt": data.get("prompt", "")
    }

    def stream_response():
        try:
            with requests.post(OLLAMA_URL, json=payload, stream=True) as response:
                for line in response.iter_lines():
                    if line:
                        try:
                            json_data = json.loads(line.decode('utf-8'))
                            yield json_data["response"]
                        except json.JSONDecodeError:
                            yield "Error al decodificar parte de la respuesta JSON."
        except Exception as e:
            yield f"Error en la solicitud: {str(e)}"

    return Response(stream_response(), content_type='text/plain')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
