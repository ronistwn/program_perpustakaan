from flask import Flask, jsonify, request

app = Flask(__name__)
buku_list = []
counter = 1

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(buku_list)

@app.route('/books', methods=['POST'])
def add_book():
    global counter
    data = request.json
    data["id"] = counter
    buku_list.append(data)
    counter += 1
    return jsonify(data), 201

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    data = request.json
    for buku in buku_list:
        if buku["id"] == id:
            buku["judul"] = data["judul"]
            buku["penulis"] = data["penulis"]
            return jsonify(buku)
    return jsonify({"error": "Not found"}), 404

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    global buku_list
    buku_list = [buku for buku in buku_list if buku["id"] != id]
    return jsonify({"message": "Buku dihapus"})

if __name__ == '__main__':
    app.run(debug=True)
