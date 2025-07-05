from flask import Flask, render_template

app: Flask = Flask(__name__)

@app.route("/")
def hello():
	return "<p>Hello!</p>"

@app.route("/hello")
def hello_all():
	name: str = "Varrahan"
	return render_template("hello.html", content=name)
if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
