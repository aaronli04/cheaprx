from flask import Flask, jsonify, request
from flask_cors import CORS
from utils import search_costplusdrugs, search_blink_health

app = Flask(__name__)
CORS(app)

@app.route('/api/medication', methods=['POST'])
def get_data():
    medications = []

    if request.method == 'POST':
        try:
            request_data = request.get_json()
            medication_name = request_data.get('name')

            costplusdrugs = search_costplusdrugs('./costplusdrugs/prescription_data.csv', medication_name)
            medications = medications + costplusdrugs

            blink_health = search_blink_health(medication_name)
            medications.append(blink_health)

            result = {'medications': medications}

            return jsonify(result), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run()