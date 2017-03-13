# Tweeter Deleter

THis script deletes tweets based on specified keywords that the user determines.Unfortunately due to Twitter's REST API you can only make a certain amount of API calls per hour. TO deal with this, this script pulls the maximum allowed tweets per call (200), checks them for the keyword, deletes if nesecarry (not counted as an API call) then sleeps for 5 minutes.
