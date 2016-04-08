import feedparser

FEEDS_LIST=[]

class MyFeed(object):
    is_read = False
    is_follow_on = False
    def __init__(self,title):
        self.title = title.encode('ascii','ignore')
    def set_url(self,url):
        self.url = url.encode('ascii','ignore')
    def set_tags(self,tags):
        self.tags = tags
    def set_description(self,description):
        self.description = description.encode('ascii','ignore')
    def __str__(self):
        return 'title:'+self.title+'\nurl:'+self.url+'\ntags:'+str(self.tags)+'\ndescription:'+self.description

def get_feeds():
    geeks_for_geeks_feeds = get_geeks_for_geeks_feeds()
    career_cup_feeds = get_career_cup_feeds()
    FEEDS_LIST.extend(geeks_for_geeks_feeds)
    FEEDS_LIST.extend(career_cup_feeds)
    return FEEDS_LIST

def get_geeks_for_geeks_feeds():
    # Parse geeksforgeeks url
    GEEKSFORGEEKS_FEED_URL = 'http://www.geeksforgeeks.org/feed'
    gfeed = feedparser.parse(GEEKSFORGEEKS_FEED_URL)
    gfeed_entries = gfeed['entries']
    GEEKSFORGEEKS_FEEDS = []
    for entry in gfeed_entries:
        title = entry['title']
        entry_url = entry['id']
        tags = []
        for tag in entry['tags']:
            tags.append(tag['term'])
        description = entry['summary']
        myFeed = MyFeed(title)
        myFeed.set_url(entry_url)
        myFeed.set_tags(tags)
        myFeed.set_description(description)
        GEEKSFORGEEKS_FEEDS.append(myFeed)
    return GEEKSFORGEEKS_FEEDS

def get_career_cup_feeds():
    CAREERCUP_FEED_URL = ''
    CAREERCUP_FEEDS = []
    return CAREERCUP_FEEDS

