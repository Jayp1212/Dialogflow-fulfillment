from flask import Flask, request, jsonify

app = Flask(__name__)

# Route to return student number
@app.route('/')
def student_number():
    return jsonify({'student_number': 'YourStudentNumber'})

# Route to handle webhook requests from Dialogflow
@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    # Process the request from Dialogflow
    # Extract intent and parameters, perform any necessary logic
    # Generate response text
    # Return response to Dialogflow
    response = {
        'fulfillmentText': 'This is the response from your webhook.'
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app
