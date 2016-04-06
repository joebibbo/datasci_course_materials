import sys
import json

notext = 0
textlns = 0
def hw(sent_file, tweet_file):
    global notext
    global textlns
    scores = {} # initialize an empty dictionary
    for line in sent_file:
	term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
	scores[term] = int(score)  # Convert the score to an integer.

    tweetCnt = 1;
    totallns = 0;

    for line in tweet_file:
        score = 0
	tweet = json.loads(line)
	lang  = 'undef'
	if 'lang' in tweet.keys():
		lang = tweet['lang']
	
	# filter out all non-English tweets for this assignment
	if ( lang != 'en' ):
		continue;

	if 'text' in tweet.keys():
		text = tweet['text']
   		words = text.split(" ");
		for term in words:
			#print term
			if term in scores.keys():
				score = score + scores[term]
		print str(tweetCnt) + ': ' + str(score)  
		tweetCnt = tweetCnt + 1;
 		textlns = textlns + 1;
	else:
		notext = notext + 1;

	totallns = totallns + 1

    print 'total # English tweets: ' + str(totallns) + ' text: ' + str(textlns) + ' # of English tweets that had no text: ' + str(notext)

def lines(fp):
    print str(len(fp.readlines()))

def main():
    afinnfile = open("AFINN-111.txt")
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
	term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
	scores[term] = int(score)  # Convert the score to an integer.

    #print scores.items() # Print every (term, score) pair in the dictionary

    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)

    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    lines(sent_file)
    lines(tweet_file)

    print 'Lines in the tweet file that have no text ' + str(notext)

if __name__ == '__main__':
    main()
