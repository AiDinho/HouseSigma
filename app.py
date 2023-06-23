from flask import Flask, jsonify, request
import time

app = Flask(__name__)

@app.route('/timestamp', methods=['GET'])
def get_timestamp():
    return jsonify({'timestamp': int(time.time())})

@app.route('/readdata', methods=['POST'])
def read_data():
    data = request.get_json(force=True)
    return jsonify(data)

@app.route('/<path:path>')
def catch_all(path):
    return jsonify(error='404 Not Found'), 404

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
