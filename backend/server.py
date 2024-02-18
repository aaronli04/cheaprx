from flask import Flask, jsonify, request
from flask_cors import CORS
from utils import search_costplusdrugs, search_blink_health

app = Flask(__name__)
CORS(app)

@app.route('/api/medication', methods=['POST'])
def get_data():

    if request.method == 'POST':
        try:
            medications = []
            request_data = request.get_json()
            medication_name = request_data.get('name')

            costplusdrugs = search_costplusdrugs('./costplusdrugs/prescription_data.csv', medication_name)
            medications = medications + costplusdrugs

            blink_health = search_blink_health(medication_name)
            if blink_health:
                medications.append(blink_health)

            medications = sorted(medications, key=lambda x: float(x.get(('price'), float('inf'))))
            result = {'medications': medications}

            return jsonify(result)
        except Exception as e:
            return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run()