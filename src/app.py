from flask import Flask, jsonify
from flask import request
app = Flask(__name__)


todos = [ { "label": "My first task", "done": False } ]


@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json  
    print("Incoming request with the following body", request_body)
    
    todos.append(request_body)  
    
    return jsonify(todos)  

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    # Verificar que la posición es válida
    if position < 0 or position >= len(todos):
        return jsonify({"error": "Posición inválida"}), 400

  # Eliminar la tarea de la lista
    todos.pop(position)
    
    # Retornar la lista actualizada
    return jsonify(todos)
    

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)