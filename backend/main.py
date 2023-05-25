from flask import Flask, jsonify, request
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
@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object ={'status':'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'title': post_data.get('title'),
            'genre': post_data.get('genre'),
            'read': post_data.get('read')  })
                  
        response_object['message'] = 'New Book is added Successfully!'
    else:
        response_object['books'] =BOOKS
    return jsonify(response_object)


@app.route('/shark', methods=['GET'])
def shark():
    return("Shark!")

if __name__ == '__main__':
    app.run(debug=True)