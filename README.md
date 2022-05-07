# News_App

## Author

[Denis-Muga](https://github.com/DenisMuga)

# Description

People who want to consume realtime news without watching TV can use this application. The app fetches news articles from different sources and users can click to read more concerning such news. News-App consumes news from NewsAPI (https://newsapi.org/)

## Live Demo

Click [Link](https://news-app.herokuapp.com/) to visit the site

## User Story

1. A user would view different news sources on the News-app homepage.
2. A user would click a news source and view all news articles from the clicked source.
3. A user would view the image and time the article was published.
4. A  user would select an article and read all the contents using the application.


## Development Installation
To get the code..

1. Cloning the repository:
  ```bash
  git clone https://github.com/DenisMuga/python-flask-week2--IP.git
  ```
2. Move to the folder and install requirements
  ```bash
  cd News_App
  pip install -r requirements.txt
  ```
3. Exporting Configurations
  ```bash
  export API_KEY='{Enter your News Api Key}'
  ```
4. Running the application
  ```bash
  python3.8 manage.py server
  ```
5. Testing the application
  ```bash
  python3.8 manage.py test
  ```
Open the application on your browser `127.0.0.1:5000`.


## Technology used

* [Python3.6](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Heroku](https://heroku.com)


## Known Bugs
* There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact Information 

If you have any question or contributions, please email me at [denismugah5@gmail.com]

## License
* *MIT License:*
* Copyright (c) 2022 **Denis Muga**