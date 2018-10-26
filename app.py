from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Tomas Vesely',
        'title': 'Blog Post 1',
        'content': 'First post Content',
        'date_posted': '10262018'
    },
]


@app.route('/')
def home():
    return render_template('home_page.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/login')
def login():
    return render_template('login_page.html')

@app.route('/index')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
