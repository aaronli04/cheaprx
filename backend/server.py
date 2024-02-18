from flask import Flask, jsonify, request
from flask_cors import CORS
from utils import search_costplusdrugs

app = Flask(__name__)
CORS(app)

@app.route('/api/medication', methods=['POST'])
def get_data():
    if request.method == 'POST':
        try:
            request_data = request.get_json()
            medication_name = request_data.get('name')

            rows = search_costplusdrugs('./costplusdrugs/prescription_data.csv', medication_name)

            print(rows)
            result = {'message': 'Data received successfully', 'medication_name': medication_name}

            return jsonify(result)
        except Exception as e:
            return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run()