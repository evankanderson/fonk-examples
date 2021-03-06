# Copyright (c) Alex Ellis 2017. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

from flask import Flask, request
from function import handler

app = Flask(__name__)

@app.route("/", defaults={"path": ""}, methods=["POST", "GET", "OPTIONS"])
@app.route("/<path:path>", methods=["POST", "GET", "OPTIONS"])
def main_route(path):
    ret = handler.handle(request.get_data())
    return ret

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
