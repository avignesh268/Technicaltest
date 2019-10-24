from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/getJokes')
def homepage():
    my_list =[]
    for x in range(10):
        r = requests.get('http://api.icndb.com/jokes/random/')
        my_list.append(json.loads(r.text)['value'])

    return render_template('the.html', my_list1=my_list)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
