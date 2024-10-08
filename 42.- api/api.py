from flask import Flask, request

app = Flask(__name__)

@app.route('/saludo', methods=['GET'])
def saludo():
    nombre = request.args.get('nombre')
    if nombre:
        return f'Hola desde api, {nombre}!'
    else:
        return 'Hola, desconocido!'

if __name__ == '__main__':
    app.run(debug=True)

#http://localhost:5000/saludo?nombre=Juan
