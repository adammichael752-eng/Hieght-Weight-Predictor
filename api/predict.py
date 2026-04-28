from http.server import BaseHTTPRequestHandler
import json
import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[5, 110], [8, 128], [10, 138], [12, 150], [15, 168], [18, 175]])
weights = np.array([18, 26, 32, 42, 58, 70])

weight_model = LinearRegression().fit(X, weights)

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length))
        age = int(body.get("age", 10))
        height = int(body.get("height", 138))

        result = {
            "weight": round(float(weight_model.predict([[age, height]])[0]), 1),
        }

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(result).encode())

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
