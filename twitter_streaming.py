#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "204478988-LePQErpHejWdwcg1NStO7oUccKWc7wpHRHRcWBlP"
access_token_secret = "FvemJ4cBCjOd05ARSfbLf46JrgiFatEdC3YR7FLeynxIC"
consumer_key = "CpxWVyRYrmpKbcZ2VOOmCqMqh"
consumer_secret = "95k4BJav8Wc4oKtJg2VXteQS88eOBYMbXVMu4zjQKs3Ow94n50"

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):    
    
    def on_data(self, data):
        print(data)
        return True
    
    def on_error(self, status):
        print(status)
        
if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['lovetwitter'])