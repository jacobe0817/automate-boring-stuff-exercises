from urllib.error import HTTPError
import requests
import os
import datetime
import bs4
import threading

def main():
    root_directory = 'comics'

    chicken_string_list = []
    chicken_thread = threading.Thread(target=savage_chickens, args=[root_directory, chicken_string_list])
    chicken_thread.start()

    moonbeard_string_list = []
    moonbeard_thread = threading.Thread(target=moonbeard, args=[root_directory, moonbeard_string_list])
    moonbeard_thread.start()

    threads = []
    threads.append(chicken_thread)
    threads.append(moonbeard_thread)

    for thread in threads:
        thread.join()

    all_strings = chicken_string_list + ['\n'] + moonbeard_string_list + ['\n']
    for string in all_strings:
        print(string, end='')

def savage_chickens(root_directory, string_list):
    url = 'https://www.savagechickens.com/'
    extension = '.jpg'
    comic_directory = os.path.join(root_directory, 'savage chickens')
    os.makedirs(comic_directory, exist_ok=True)

    successful_download, soup, download_message = download_page(url)
    string_list.append(download_message)
    if not successful_download:
        return

    try:
        dt = soup.select_one('span.date.time.published').getText()
        dt = datetime.datetime.strptime(dt, '%B %d, %Y')
    except AttributeError:
        string_list.append('\nDate could not be found in html, may need to tweak scraper')

    file_is_new, filename, file_message = get_new_file_path(dt, comic_directory, extension)
    string_list.append(file_message)
    if not file_is_new:
        return

    try:
        img_link = soup.select_one('div.entry_content').select_one('img').get('src')
    except AttributeError:
        string_list.append('\nComic could not be found in html, may need to tweak scraper')
        return

    string_list.append(download_image(img_link, comic_directory, filename))

def moonbeard(root_directory, string_list):
    url = 'https://moonbeard.com/'
    extension = '.png'
    comic_directory = os.path.join(root_directory, 'moonbeard')
    os.makedirs(comic_directory, exist_ok=True)

    successfuL_download, soup, download_message = download_page(url)
    string_list.append(download_message)
    if not successfuL_download:
        return

    try:
        dt = soup.select_one('span.post-date').get_text()
        dt = datetime.datetime.strptime(dt, '%B %d, %Y')
    except AttributeError:
        string_list.append('\nDate could not be found in html, may need to tweak scraper')

    file_is_new, filename, file_message = get_new_file_path(dt, comic_directory, extension)
    string_list.append(file_message)
    if not file_is_new:
        return
    
    try:
        image_link = soup.select_one('div.comicpane').select_one('img').get('src')
    except AttributeError:
        string_list.append('\nComic could not be found in html, may need to tweak scraper')
        return

    string_list.append(download_image(image_link, comic_directory, filename))

# attempts to download the passed page
# returns a tuple (download was successful, soup object, message)
def download_page(url):
    try:
        res = requests.get(url, headers={"User-Agent": "XY"})
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        return (True, soup, f'\nOpened {url}')
    except HTTPError:
        return (False, None, f'\nCould not establish connection to {url}')

#returns a tuple (file is new, file path, message)
def get_new_file_path(dt, comic_directory, extension):
    new_filename = dt.strftime('%Y-%m-%d') + extension

    if new_filename in os.listdir(comic_directory):
        return (False, new_filename, f'\n{new_filename} already downloaded')
    return (True, new_filename, '')

def download_image(image_link, comic_directory, filename):
    try:
        img = requests.get(image_link, headers={"User-Agent": "XY"})
        img.raise_for_status()
    except HTTPError:
        return'\nImage could not be downloaded'

    download_path = os.path.join(comic_directory, filename)
    with open(download_path, 'wb') as image_file:
        for chunk in img.iter_content(10000):
            image_file.write(chunk)
        return f'\nDownloaded comic to {download_path}'

if __name__ == '__main__':
    main()