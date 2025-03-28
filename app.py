from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_cloud():
    return 'SUCCESS! Final update via Github and CloudBuild!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
