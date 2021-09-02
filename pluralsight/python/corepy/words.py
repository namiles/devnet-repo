
import sys # Required to take arguments into the script
from urllib.request import urlopen

def fetch_words(url):
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()
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


# Dunder name, Dunder main
# If they are not equal, python knows it is being imported as a module into another module -
# and will not run the function automatically.
if __name__ == "__main__":
    main(sys.argv[1]) # The 0th arg is the module filename.

