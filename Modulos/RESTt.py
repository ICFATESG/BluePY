from flask import Flask, jsonify
from bluePy import json_list
app = Flask(__name__)

macs=json_list()


@app.route('/macs', methods=['GET'])
def get_tasks():
    return macs

if __name__ == '__main__':
    app.run()