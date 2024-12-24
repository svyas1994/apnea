import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json  # Get JSON data from the request
    selected_date = data.get('selected_date')

    if not selected_date:
        return jsonify({"success": False, "message": "No date provided"}), 400

    # Save to a JSON file
    json_file_path = "submitted_data.json"
    try:
        # Append to JSON file
        with open(json_file_path, 'r') as json_file:
            existing_data = json.load(json_file)
    except FileNotFoundError:
        existing_data = []

    existing_data.append({"selected_date": selected_date})

    with open(json_file_path, 'w') as json_file:
        json.dump(existing_data, json_file, indent=4)

    return jsonify({"success": True, "message": f"Date {selected_date} saved successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
