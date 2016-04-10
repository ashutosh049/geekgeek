import feedparser
import pickle
import os

FEEDS_DICT={}
HOME_FOLDER = os.path.expanduser('~')
FEEDPARESER_DB_PATH = HOME_FOLDER + "/.feedparserdb"

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
    FEEDS_DICT.update(geeks_for_geeks_feeds)
    FEEDS_DICT.update(career_cup_feeds)
    return FEEDS_DICT

def get_feeds_from_db():
    dbReadFileHandler = open(FEEDPARESER_DB_PATH, "r")
    dbGeeks = pickle.load(dbReadFileHandler)
    dbReadFileHandler.close()
    return dbGeeks

def get_geeks_for_geeks_feeds():
    # Parse geeksforgeeks url
    GEEKSFORGEEKS_FEED_URL = 'http://www.geeksforgeeks.org/feed'
    gfeed = feedparser.parse(GEEKSFORGEEKS_FEED_URL)
    gfeed_entries = gfeed['entries']
    GEEKSFORGEEKS_FEEDS_DICT = {}
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
        GEEKSFORGEEKS_FEEDS_DICT[entry_url]=myFeed
    return GEEKSFORGEEKS_FEEDS_DICT

def get_career_cup_feeds():
    from bs4 import BeautifulSoup
    import urllib

    HOME_URL = "https://careercup.com"
    CAREERCUP_FEED_URL = 'https://careercup.com/page'
    r = urllib.urlopen(CAREERCUP_FEED_URL).read()
    soup = BeautifulSoup(r)
    questions = soup.find_all("li",{"class":"question"})
    CAREERCUP_FEEDS_DICT = {}
    for question in questions:
        title = question.find("span",{"class":"tags"}).get_text().replace("\n"," ")
        uri = question.find("span",{"class":"entry"}).find("a").get("href")
        url = HOME_URL + uri
        description = question.find("span",{"class":"entry"}).find("p").prettify()
        tags = question.find("span",{"class":"tags"}).get_text().split("\n")
        myFeed = MyFeed(title)
        myFeed.set_url(url)
        myFeed.set_tags(tags)
        myFeed.set_description(description)
        CAREERCUP_FEEDS_DICT[url]=myFeed
    return CAREERCUP_FEEDS_DICT

def read_feeds_from_db():
    dbReadFileHandler = open(FEEDPARESER_DB_PATH, "r")
    dbGeeks = pickle.load(dbReadFileHandler)
    dbReadFileHandler.close()
    return dbGeeks

def write_feeds_to_db(feeds_dict):
    dbFileHandler = open(FEEDPARESER_DB_PATH, "w")
    pickle.dump(feeds_dict, dbFileHandler)
    dbFileHandler.close()
    return
if __name__=="__main__":
    dbGeeks = {}
    if os.path.isfile(FEEDPARESER_DB_PATH):
        dbGeeks = read_feeds_from_db()
    # Get feeds by parsing websites
    feeds_dict=get_feeds()
    # Update feeds dictionary with the feeds status from database
    feeds_dict.update(dbGeeks)
    # Write feeds to db
    write_feeds_to_db()