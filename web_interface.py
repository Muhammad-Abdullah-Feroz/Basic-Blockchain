from blockchain import Blockchain
from flask import Flask, jsonify, request

app = Flask(__name__)
blockchain = Blockchain()
