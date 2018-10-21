from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author': 'Akshay Kulkarni',
        'title': 'OnePlus 6T launch rescheduled on October 29th',
        'content': 'OnePlus is moving up the launch of its OnePlus 6T by a day in order to avoid colliding with Apple’s iPad Pro and Mac event on October 30th, which was just announced yesterday. The change was revealed in a post by CEO Pete Lau on the OnePlus community forum, who explained the difficult decision. Both events were scheduled to take place in New York on the same day, but OnePlus has announced that it will now hold its event on October 29th at the same location and 11AM ET time.',
        'date_posted': 'October 21, 2018'
    },
	{
        'author': 'John Doe',
        'title': 'Flask is Fun!',
        'content': 'Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions. And before you ask: It\'s BSD licensed!',
        'date_posted': 'October 22, 2018'
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
