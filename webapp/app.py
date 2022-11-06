from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/pgp.txt')
def pgp():
	return render_template("pgp.html")
	
@app.route('/blog/<title>')
def blog(title):
    return render_template('blog.html', title=title)

if __name__ == "__main__":
	app.run(debug=True, host = "0.0.0.0")
