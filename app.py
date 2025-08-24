from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def home():
  return render_template('index.html')


@app.route('/hello')
def hello():
  return 'hello this is the intro section after the welcome, I want to say hello to you. Glad you entered this page.'


@app.route('/hello/<name>')
def name(name):
  return f"Hello, {name.capitalize()}"


@app.route('/greet')
def greet():
  name = request.args.get('name', 'Stranger')
  return f"Hello, {name.capitalize()} hope you are doing well."


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
