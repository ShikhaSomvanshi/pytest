from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def send_get_request():
    url = 'https://gorest.co.in/public/v2/users'
    response = requests.get(url)
    return response.json()

if __name__ == '__main__':
    app.run(debug=True)
