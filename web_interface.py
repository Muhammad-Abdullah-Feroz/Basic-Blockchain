from blockchain import Blockchain
from flask import Flask, jsonify, request

app = Flask(__name__)
blockchain = Blockchain()

@app.route("/blocks", methods=["GET"])
def get_blocks():
    blocks = []
    for block in blockchain.get_chain():
        blocks.append({
            "index": block.index,
            "timestamp": block.timestamp,
            "data": block.data,
            "hash": block.hash,
            "previous_hash": block.previous_hash
        })
    return jsonify(blocks)

@app.route("/add_block", methods=["POST"])
def add_block():
    data= request.json["data"]
    blockchain.add_block(data)
    return jsonify({"message": "Block added successfully!"}), 200

if __name__ == '__main__':
    app.run(debug=True)