from flask import Flask, request, jsonify
from flask_cors import CORS

import os, sys

import requests
from invokes import invoke_http

import json
from types import SimpleNamespace



if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) + " for placing an offer...")
    app.run(host="0.0.0.0", port=5100, debug=True) 