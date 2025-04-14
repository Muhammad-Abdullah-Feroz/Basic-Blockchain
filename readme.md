# Basic Blockchain Application

This is a basic implementation of a blockchain built in Python. The application allows you to store data in blocks, where each block contains a list of transactions, a timestamp, a hash of the current block, and a reference to the previous block in the chain.

## Features

- Create a basic blockchain with the ability to store data.
- Each block contains:
  - Index: Position of the block in the blockchain.
  - Timestamp: When the block was created.
  - Data: The actual data stored in the block.
  - Previous Hash: The hash of the previous block.
  - Hash: The hash of the current block.
- A simple web interface to interact with the blockchain using Flask (optional).

## Requirements

- Python 3.x
- Flask (for the web interface, optional)
- `hashlib` (for hashing)

### Install Dependencies
1. Install the required libraries using pip:
   ```bash
   pip install flask
# How to Run the Application

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/blockchain-app.git
   cd blockchain-app
   ```

2. Run the application:

   ```bash
   python app.py
   ```

3. The Flask app will start, and you can access it at:

   ```bash
   http://127.0.0.1:5000/
   ```

4. You can interact with the blockchain through the following endpoints:

   - **GET /blocks**: Retrieve the entire blockchain in JSON format.
   - **POST /add_block**: Add a new block to the blockchain. Send a JSON request with the `data` field.

## API Endpoints

### Get All Blocks
**GET /blocks**

Returns the entire blockchain as a JSON array. Example response:

```json
[
  {
    "index": 0,
    "timestamp": 1630972800.0,
    "data": "Genesis Block",
    "hash": "abcdef1234567890",
    "previous_hash": "0"
  },
  {
    "index": 1,
    "timestamp": 1630972900.0,
    "data": "First piece of data",
    "hash": "abcdef1234567891",
    "previous_hash": "abcdef1234567890"
  }
]
```

### Add a New Block
**POST /add_block**

Request body (JSON):

```json
{
  "data": "Second piece of data"
}
```

Response:

```json
{
  "message": "Block added successfully!"
}
```

## How the Blockchain Works

### Block Structure
Each block in the blockchain contains:
- **Index**: A unique number representing the block's position in the chain.
- **Timestamp**: The time the block was created.
- **Data**: The data being stored in the block.
- **Previous Hash**: The hash of the previous block in the chain.
- **Hash**: A unique hash generated for this block using the block's content.

### Blockchain Structure
The blockchain is a series of blocks where each block is linked to the previous block by its hash. The genesis block (the first block) has no previous hash, and each subsequent block points to the previous block's hash.

## Future Improvements

- Implement consensus algorithms (e.g., Proof of Work).
- Add user authentication for interacting with the blockchain.
- Explore integrating with a frontend interface (React, Vue, etc.).
- Implement smart contracts or more complex transaction handling.

## License
This project is open-source and available under the MIT License. See the LICENSE file for more information.

## Acknowledgements

- Python documentation
- Flask documentation
