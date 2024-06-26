from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, welcome to Barkuni Corp!'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
