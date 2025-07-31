# app.py
from flask import Flask, render_template, request
from scraper import scrape_basic_info

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    data = []
    if request.method == 'POST':
        urls = request.form['urls'].splitlines()
        for url in urls:
            data.append(scrape_basic_info(url.strip()))
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
