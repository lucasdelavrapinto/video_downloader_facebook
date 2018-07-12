from flask import Flask, request, render_template, redirect, url_for
import requests as r
import re
import sys

app = Flask(__name__)

@app.route('/')
def index():
	
	return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():

	url = request.form['url']
	html = r.get(url)
	video_url = re.search('hd_src:"(.+?)"', html.text).group(1)
	
	return render_template('result.html', video_url=video_url,
		url=url)

if __name__ == '__main__':
	app.run(debug=True)