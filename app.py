from flask import Flask, render_template

from newsapi import NewsApiClient

app = Flask(__name__)

@app.route('/')
def index():
    
    # Init
    newsapi = NewsApiClient(api_key='1f06391ab2df4b129f263c5fc5ee6f03')
    
    #A function for top headline news
    top_headlines = newsapi.get_top_headlines(sources = 'bbc-news')
    
    t_articles = top_headlines['articles'] #Fetching all articles of top headlines
    
    #A list of contents to store the values on the list 
    news = []
    desc = []
    img = []
    p_date = []
    url = []
    
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    
