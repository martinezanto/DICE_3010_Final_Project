
#This bot searches for people that use the term "#teamapple", likes their post, follows person, and sends them a tweet saying "Apple Rules!" with a link to the Apple products on Amazon.
 

import urllib
import simplejson
import twitter
import tweepy

consumer_key = 'wJpwLUODs2Js95GJJxP42q3Dl'
consumer_secret = 'eEBrQclSxqmx68N1sO3AaXntfogVIgKey5m9G9KxPvnCTYPC46'
access_token_key = '1204933477214220289-S18ZiHLnRlq4Pj3YO6PwrOqZWNs96m'
access_token_secret = 'hst2UOqdbV7hQdOr3p6VfToVCBET7di8Y2SLazOntMYnA'

def searchTweets(query):
	search = urllib.urlopen("http://search.twitter.com/search.json?q="+query)
	dict = simplejson.loads(search.read())
	return dict

api = twitter.Api(consumer_key = consumer_key, consumer_secret = consumer_secret, access_token_key = access_token_key, access_token_secret = access_token_secret)
tweets = searchTweets("#teamapple&rpp=100&result_type=recent")
msg = 'Check out these apples! Him: https://www.google.com/search?biw=1280&bih=529&tbm=isch&sxsrf=ACYBGNQiMY9V65RXNw8dEOlWP8dQb4CqPA%3A1576115622918&sa=1&ei=pp3xXerVN83B0PEPqvSH8A0&q=apples&oq=apples&gs_l=img.3..0l10.35857.36727..36961...2.0..0.284.1938.0j6j4......0....1..gws-wiz-img.......35i39j0i67j0i131i67.brhQjRr0IOI&ved=0ahUKEwjqwNCegK_mAhXNIDQIHSr6Ad4Q4dUDCAc&uact=5 Her: https://www.apple.com/'

for i in range(len(tweets["results"])):
	tweeter = tweets["results"][i]["from_user"]
	status = twitter.Api.GetStatus(api, tweets["results"][i]["id"])
	api.CreateFavorite(status)
	api.CreateFriendship(tweeter)
	api.PostUpdate('@' + tweeter + ' ' + msg)
