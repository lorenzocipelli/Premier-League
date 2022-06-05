# Football News with MQTT
This little project has been created to show the MQTT protocol working, there are two main ![Python](https://img.shields.io/badge/-Python-333333?style=flat&logo=python) scripts, [subscriber.py](https://github.com/lorenzocipelli/telematica/blob/main/subscriber.py) which allows to subscribe to different topics (we use the football_news main topic with all team names as subtopics, for example, premier_league_news/manchester_city), and the other main script is [publisher.py](https://github.com/lorenzocipelli/telematica/blob/main/publisher.py) that allows to publish the news inside the database (used to simulate a news system), one for every team's topic.

⭐️ From [lorenzocipelli](https://github.com/lorenzocipelli) & [nicholas9813](https://github.com/nicholas9813)

## Modules to install
Use the terminal to install the following modules (make sure that the search path for modules is correctly configured):
```js
pip install pandas
pip install paho-mqtt
```
Run [subscriber.py](https://github.com/lorenzocipelli/telematica/blob/main/subscriber.py) to simulate a subscriber;
Run [publisher.py](https://github.com/lorenzocipelli/telematica/blob/main/publisher.py) to simulate a publisher;
