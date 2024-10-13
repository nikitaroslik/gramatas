import json
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def read_books_from_file():
    with open('books.json', 'r') as f:
        return json.load(f)

def write_books_to_file(books):
    with open('books.json', 'w') as f:
        json.dump(books, f, indent=4)

@app.route('/books', methods=['GET'])
def get_books():
    books = read_books_from_file()
    return jsonify(books)

@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    books = read_books_from_file()
    book = next((book for book in books if book['id'] == id), None)
    return jsonify(book)

@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.json
    books = read_books_from_file()
    new_book['id'] = len(books) + 1
    books.append(new_book)
    write_books_to_file(books)
    return jsonify(new_book), 201

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    books = read_books_from_file()
    book = next((book for book in books if book['id'] == id), None)
    if book:
        book.update(request.json)
        write_books_to_file(books)
        return jsonify(book)
    return jsonify({'error': 'Book not found'}), 404

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    books = read_books_from_file()
    books = [book for book in books if book['id'] != id]
    write_books_to_file(books)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
