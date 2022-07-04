# Football News with MQTT
This little project has been created to show the MQTT protocol working, there are two main ![Python](https://img.shields.io/badge/-Python-333333?style=flat&logo=python) scripts, [subscriber.py](https://github.com/lorenzocipelli/telematica/blob/main/subscriber.py) which allows to subscribe to different topics (we use the football_news main topic with all team names as subtopics, for example, premier_league_news/manchester_city), and the other main script is [publisher.py](https://github.com/lorenzocipelli/telematica/blob/main/publisher.py) that allows to publish the news inside the database (used to simulate a news system), one for every team's topic.

⭐️ From [lorenzocipelli](https://github.com/lorenzocipelli) & [nicholas9813](https://github.com/nicholas9813)

## Modules to install
Use the terminal to install the following modules (make sure that the search path for modules is correctly configured):
```js
pip install pandas
pip install paho-mqtt
pip install beautifulsoup4 (run this code just in case you want to execute
	the [news_collector.py](https://github.com/lorenzocipelli/telematica/blob/main/news_collector.py) file, that allows you to download the latests
	news from every Premier League club)
```
Run [subscriber.py](https://github.com/lorenzocipelli/telematica/blob/main/subscriber.py) to simulate a subscriber and being able to follow your favourite/es club and receive relatives news;
Run [publisher.py](https://github.com/lorenzocipelli/telematica/blob/main/publisher.py) to simulate a publisherand and being able to publish about a specific topic;

You can freely look inside the code and play with the subscriptions and publications, the code is commented so that functions are easly understandable
