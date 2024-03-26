from flask import Flask, request, jsonify

app = Flask(__name__)

# Route to return student number
@app.route('/')
def student_number():
    return jsonify({'student_number': 'YourStudentNumber'})

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    fulfillmentText = ''
    
    if req:
        query_result = req.get('queryResult')
        if query_result and query_result.get('action') == 'get.address':
            fulfillmentText = 'Hi'

    return jsonify({
        "fulfillmentText": fulfillmentText,
        "source": "webhookdata"
    })


if __name__ == '__main__':
    app.run(debug=True)  
