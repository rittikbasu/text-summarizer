from flask import Flask, request,  render_template
from threading import Thread
from summarise import geturl, process

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('landing_page.html')

@app.route('/', methods=['POST'])
def my_form_post():
    select = request.form['select']
    num = request.form['number']
    if select=='URL':
      url = request.form['url']
      value = geturl(url,int(num))
      return render_template("summary_page.html", text=value)
    else:
      text = request.form['text']
      value = process(text,int(num))
      return render_template("summary_page.html", text=value)

def run():
    app.run(host='0.0.0.0', port=9000)


def keep_alive():
    t = Thread(target=run)
    t.start()
    
