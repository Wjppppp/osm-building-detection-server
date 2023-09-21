from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
import socket
from inference_post import inference
import time

app = Flask(__name__)
CORS(app)


# Function to fetch hostname and ip
def fetchDetails():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return str(hostname), str(ip) 

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/health")
def health():
    return jsonify(
        status = "UP"
    )

@app.route("/details/<tag>")
def details(tag):
    hostname, ip = fetchDetails()
    method = request.method
    return render_template('index.html', HOSTNAME=hostname, IP =ip, TAG=tag, METHOD=method)

@app.post("/inference")
def respond_inference():
    start = time.time()

    header = request.headers    
    body = request.get_json()

    print("header", header)
    print("request", request)
    print(f'body: {body}')

    extend = body['bbox']
    model = body['model']

    length, geojson, num = inference(extend, model)

    end = time.time()

    return jsonify(
        status = 200,
        length = length,
        time = end-start,
        geojson = geojson,
        num = num
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7001)