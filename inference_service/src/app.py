from flask import Flask, jsonify, render_template, request
import socket

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7001)