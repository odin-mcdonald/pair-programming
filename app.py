from flask import Flask, request, render_template, redirect, url_for, flash

app = Flask(__name__)

# Handling error 404 and displaying relevant web page
@app.errorhandler(404)
def not_found_error(error):
    return render_template("404.html"), 404

# Handling error 500 and displaying relevant web page
@app.errorhandler(500)
def internal_error(error):
    return render_template("500.html"), 500

books_dict = [
{"title": "The Hobbit", "author": "J.R.R. Tolkien", "pages": 295, "genre": "Fiction", "details": "read,recommend", "source": "library"}
]


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template(
        "index.html", pageTitle="Homepage", books=books_dict
    )


@app.route("/add", methods=["POST"])
def add():
    print("inside add function")
    if request.method == "POST":

        form = request.form

        title = form["title"]
        author = form["author"]
        pages = form["pages"]
        genre = form["genre"]
        details = form.getlist("details")
        source = form["source"]
        #activities = form.getlist("activities")  # this is a PYthon list

        print(title)
        print(author)
        print(pages)
        print(genre)
        print(details)
        print(source)

        details_string = ", ".join(details)  # make the Python list into a string

        book_dict = {
            "title": title,
            "author": author,
            "pages": pages,
            "genre": genre,
            "details": details_string,
            "source": source,
        }

        print(book_dict)
        books_dict.append(
            book_dict
        )  # append this dictionary entry to the larger books dictionary
        print(books_dict)
        return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))
    
@app.route("/about")
def about():
    return rexder_template ("about.html")


if __name__ == "__main__":
    app.run(debug=False)
    #Before publishing, debug=FALSE


