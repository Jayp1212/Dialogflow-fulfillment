from flask import Flask, request, jsonify, render_template
import requests
import time

api_key = "c163c7181ca543d5b0f786987cc4cfe0"

app = Flask(__name__)

# Route to return student number
@app.route('/')
def student_number():
    student_number = '200543276'
    # Render the HTML template with the student number
    return render_template('index.html', student_number=student_number)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(force=True)
    intent_name = req.get('queryResult').get('intent').get('displayName')

    if intent_name == 'GetStockPrice':
       
        params = req.get('queryResult').get('parameters')
        stock_symbol = params.get('stock_symbol')
        url = f"https://api.twelvedata.com/price?symbol={stock_symbol}&apikey={api_key}"
       
        response = requests.get(url).json()
        price = response['price']

        fulfillment_text = f"The latest price of {stock_symbol} is {price}."

        response = {'fulfillmentText': fulfillment_text}
    else:
        response = {'fulfillmentText': 'Unknown intent'}

    return jsonify(response)
    


if __name__ == '__main__':
    app.run(debug=True)  
