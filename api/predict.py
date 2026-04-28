from http.server import BaseHTTPRequestHandler
import json
import numpy as np
from sklearn.linear_model import LinearRegression

ages = np.array([5, 8, 10, 12, 15, 18]).reshape(-1, 1)
heights = np.array([110, 128, 138, 150, 168, 175])
weights = np.array([18, 26, 32, 42, 58, 70])

height_model = LinearRegression().fit(ages, heights)
weight_model = LinearRegression().fit(ages, weights)

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length))
        age = [[body.get("age", 10)]]

        result = {
            "height": round(height_model.predict(age)[0], 1),
            "weight": round(weight_model.predict(age)[0], 1),
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
