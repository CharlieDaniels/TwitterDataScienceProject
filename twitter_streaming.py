#Import the necessary methods from tweepy library
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = #enter your access_token credentials here
access_token_secret = #enter your access_token_secret credentials here
consumer_key = #enter your consumer_key credentials here
consumer_secret = #enter your consumer_secret credentials here


#Basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #Handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #Filter Twitter Streams to capture data by keywords
    stream.filter(track=['microbiome'])

    #Run the file to save tweets to a text file: python twitter_streaming.py > twitterdata.txt