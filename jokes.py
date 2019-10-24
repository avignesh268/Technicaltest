from flask import Flask, render_template
import requests
import json

app = Flask(__name__, template_folder='.')

@app.route('/getJokes')
def homepage():
  r = requests.get(
      'http://api.icndb.com/jokes/random/')
  return render_template('jokes.html', movies=json.loads(r.text)['jokes'])

if __name__ == '__main__':
  app.run(debug=True)
