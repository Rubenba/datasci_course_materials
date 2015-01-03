import oauth2 as oauth
import urllib2 as urllib

#Tambien podria funcionar import urllib2.urlopen as urllib

# See assignment1.html instructions or README for how to get these credentials

api_key = "IQWsv7hlrfsutKWNP9oc6bV3u"
api_secret = "h26ACXQa3Fds0tvNPLaIUc48L3BP3h6e1dFvxMEj1fDcDurXQv"
access_token_key = "793973412-EaWk4pg9BPsRK2FmMFwosN1I2iEk0ZK0RQI5fPQM"
access_token_secret = "ZinGLKFR2aMLP6n4fPBtuPNWE9MhrQNkTg9SolnBHKnqg"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=api_key, secret=api_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

def fetchsamples():
  url = "https://stream.twitter.com/1.1/statuses/sample.json"
  parameters = []
  response = twitterreq(url, "GET", parameters)
  f = open('outputtwitter.txt', 'w')

  for line in response:
    print >>f, line.strip()


if __name__ == '__main__':
  fetchsamples()



f = open('C:\\Users\\Ruben\\PycharmProjects\\datasci_course_materials\\assignment1\\outputtwitter.txt', 'r')
outfile = open("C:\\Users\\Ruben\\PycharmProjects\\datasci_course_materials\\assignment1\\assign1prob1.txt","a") # open file for appending

for i in range(21):
  line = f.readline()
  outfile.write(line)
  print(line)

f.close()
outfile.close()


def fetchmicrosoft():
  url = "https://stream.twitter.com/1.1/statuses/sample.json?q=microsoft"
  parameters = []
  response = twitterreq(url, "GET", parameters)
  f = open('output2.txt', 'w')

  for line in response:
    print >>f, line.strip()


if __name__ == '__main__':
  fetchmicrosoft()


fmicrosoft = open('C:\\Users\\Ruben\\PycharmProjects\\datasci_course_materials\\assignment1\\output2.txt', 'r')
outfilemicro = open("C:\\Users\\Ruben\\PycharmProjects\\datasci_course_materials\\assignment1\\assign1prob1micro.txt","a") # open file for appending

for i in range(21):
  line = fmicrosoft.readline()
  outfilemicro.write(line)
  print(line)

fmicrosoft.close()
outfilemicro.close()

