from flask import Flask, render_template, request
#started 9:06pm - 9:35pm
#10am-10:40am

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    # return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    return render_template("index.html")

@app.route("/application-form")
def application_form():
    
    return render_template("application-form.html")

@app.route("/application", methods=['POST'])
def application():
    firstname = request.form.get("first-name")
    lastname = request.form.get("last-name")
    salary = request.form.get("salary")
    job = request.form.get("job")

    return render_template("application-response.html", firstname=firstname, 
                            lastname=lastname,
                            job=job,
                            salary=salary)


if __name__ == "__main__":
    app.run(debug=True)
