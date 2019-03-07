import urllib3
from bs4 import BeautifulSoup


def read_file(path):
    text_file = open(path)
    content = text_file.read()
    print('Content from text file: ' + content)
    text_file.close()
    return content


def check_for_profanity(content):
    http = urllib3.PoolManager()
    content_without_spaces = content.replace(' ', '%20').replace('\n', '%20')
    url = 'http://www.wdylike.appspot.com/?q='+content_without_spaces
    response = http.request('GET', url)
    soup = BeautifulSoup(response.data, features="html.parser")
    print('Response from HTTP request: ' + soup.contents[0])

    response_after_check = "There's profanity in this text file" if 'true' in soup.contents \
        else "No Profanity... This file is clean." if 'false' in soup.contents \
        else "Something happened, maybe a bad request?"
    return response_after_check


# Should say that there's profanity in the text file
print(check_for_profanity(read_file('profanity_checker/files/bad.txt')))

print("----------------------------------------------------------")

# Should say that there's no profanity in the text file
print(check_for_profanity(read_file('profanity_checker/files/good.txt')))
