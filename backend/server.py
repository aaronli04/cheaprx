from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/find', methods=['POST'])
def get_data():
    print('hello')
    data = {'key': 'value'}
    return jsonify(data)

if __name__ == '__main__':
    app.run()