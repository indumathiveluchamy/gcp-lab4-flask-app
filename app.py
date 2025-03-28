from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_cloud():
    return 'Hello Cloud! Deployed via Terraform and Cloud Build.'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
