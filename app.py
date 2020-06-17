from flask import Flask

app = Flask(__name__)

# routes
@app.route('/')
def home():
    return "Hello World"

# run app
if __name__ == "__main__":
    app.run(host='10.0.0.4', debug=True)