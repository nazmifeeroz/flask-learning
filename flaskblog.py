from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Nazmi Feeroz',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Nov 25 2021'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'First post content',
        'date_posted': 'Nov 21 2021'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)

