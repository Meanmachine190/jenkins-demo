from flask import Flask
from prometheus_client import start_http_server, Summary, Counter, generate_latest

app = Flask(__name__)

REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests')

@app.route('/')
def hello():
    REQUEST_COUNT.inc()
    return "Hello from Jenkins with metrics!"

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain; charset=utf-8'}

if __name__ == "__main__":
    # Start Prometheus client on default port 8000
    start_http_server(8000)
    app.run(host='0.0.0.0', port=5000)

