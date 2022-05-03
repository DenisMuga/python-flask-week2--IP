from flask import Flask, render_template

from newsapi import NewsApiClient

app = Flask(__name__)

@app.route('/')
def index():
    
    # Init
    newsapi = NewsApiClient(api_key='1f06391ab2df4b129f263c5fc5ee6f03')
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    
