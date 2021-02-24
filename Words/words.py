import sys
from urllib.request import urlopen # to open url

def fetch_words(url):
    story = urlopen(url)  # all content from the page encoded in utf-8
    story_words = [] # empty list for words of page
    for line in story:
        line_words = line.decode('utf8').split() 
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words

def print_items(items):
    for item in items:
        print(item)

def main(url):
    words = fetch_words(url)
    print_items(words)

if __name__ == '__main__':
    main(sys.argv[1])
