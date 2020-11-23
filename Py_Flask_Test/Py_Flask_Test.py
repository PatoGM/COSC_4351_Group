from flask import Flask, render_template, url_for, request

app = Flask(__name__)   # __name__ is the name of the module, flask knows where to look for templates/static files


posts = [
    {
        'author': 'Site/Post Author',
        'title': 'Basic Site Info',
        'content': 'Instructions and other info regarding this site',
        'date_posted': 'November 23, 2020'
    }
]


@app.route("/")
@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/home")
def home():
    admin_type = request.args.get('type')
    return render_template('home.html', posts=posts, type=admin_type)


# @app.route("/about")
# def about():
#     return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)

# cd COSC_4351
# set FLASK_APP=Py_Flask_Test.py
# set FLASK_ENV=development
# flask run
