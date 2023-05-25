from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*":{'origins':"*"}})

BOOKS = [
 {
"title" : "The Shadow of the Wind",
"genre" : "Historical Fiction",
"read" : False,
},
{
"title" : "The Martian",
"genre" : "Science Fiction",
"read" : True,
},
{
"title" : "To Kill a Mockingbird",
"genre" : "Classic Literature",
"read" : True,
},
{
"title" : "Gone Girl",
"genre" : "Thriller",
"read" : False,
},
{
"title" : "The Hunger Games",
"genre" : "Young Adult, Dystopian",
"read" : True,
},
{
"title" : "Pride and Prejudice",
"genre" : "Romance, Classic Literature",
"read" : True,
},
{
"title" : "1984",
"genre" : "Dystopian, Science Fiction",
"read" : False,
},
{
"title" : "The Great Gatsby",
"genre" : "Classic Literature",
"read" : True,
},
{
"title" : "The Girl on the Train",
"genre" : "Thriller",
"read" : False,
},
{
"title" : "Harry Potter and the Sorcerer's Stone",
"genre" : "Fantasy, Young Adult",
"read" : True,
}
]

#books route handler
@app.route('/books', methods=['GET'])
def all_books():
    return jsonify(
        {'books': BOOKS, 'status': 'success'}
    )

@app.route('/shark', methods=['GET'])
def shark():
    return("Shark!")

if __name__ == '__main__':
    app.run(debug=True)