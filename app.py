from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

books_dict = [
{"title": "The Hobbit", "author": "J.R.R. Tolkien", "pages": 295, "classification": "Fiction", "details": "read,recommend", "acquisition": "library"}
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
        classification = form["classification"]
        details = form.getlist("details")  # this is a PYthon list
        acquisition = form["acquisition"]
        #activities = form.getlist("activities")  # this is a PYthon list

        print(title)
        print(author)
        print(pages)
        print(classification)
        print(details)
        print(acquisition)

        details_string = ", ".join(details)  # make the Python list into a string

        book_dict = {
            "title": title,
            "author": author,
            "pages": pages,
            "classification": classification,
            "details": details_string,
            "acqusition": acquisition,
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
    return render_template ("about.html")


if __name__ == "__main__":
    app.run(debug=True)
