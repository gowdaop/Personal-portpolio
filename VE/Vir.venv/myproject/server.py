from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route('/contact', methods=['POST'])
def contact():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    # Format the message
    entry = (
        f"\n--- New Message ---\n"
        f"Time: {datetime.now()}\n"
        f"Name: {name}\n"
        f"Email: {email}\n"
        f"Message:\n{message}\n"
    )

    # Save to messages.txt
    with open('messages.txt', 'a', encoding='utf-8') as f:
        f.write(entry)

    return jsonify({'status': 'success', 'message': 'Message received and saved.'})

if __name__ == '__main__':
    app.run(debug=True)
