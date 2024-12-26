from flask import Flask, render_template

app =  Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/')
def about():
  return 'this is about this page'

if __name__ == '__main__':
  app.run(host = '0.0.0.0', debug = True)

    