# Tweeter Deleter

This script deletes tweets based on specified keywords that the user determines in a file. Unfortunately due to Twitter's REST API you can only make a certain amount of API calls per hour. To deal with this, this script pulls the maximum allowed tweets per call (200), checks them for the keyword, deletes if necessary (not counted as an API call) then sleeps for 5 minutes.

It'll take 8.5 hours to go through 20,000 tweets, so it's probably best to let this script run over night.

![screenshot of Tweeter-Deleter](http://i.imgur.com/XjYNqIZ.png)
