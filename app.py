from flask import Flask, request, make_response, jsonify

app = Flask(__name__)

# 1. Declaring API routes
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/data')
def get_data():
    data = {"key": "value"}
    return jsonify(data)

# 2. Getting and Setting Cookies
@app.route('/set_cookie')
def set_cookie():
    resp = make_response("Cookie set!")
    resp.set_cookie('user_id', '12345')
    return resp

@app.route('/get_cookie')
def get_cookie():
    user_id = request.cookies.get('user_id')
    return f"User ID: {user_id}"

# 3. Retrieving Request Form Data
@app.route('/submit', methods=['POST'])
def submit_form():
    username = request.form.get('username')
    password = request.form.get('password')
    return f"Received username: {username} and password: {password}"

# 4. Returning Various HTTP Status Codes
@app.route('/not_found')
def not_found():
    return make_response("Resource not found", 404)

@app.route('/forbidden')
def forbidden():
    return make_response("Access forbidden", 403)

if __name__ == '__main__':
    app.run()
