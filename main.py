import time
import requests

def extract_urls(html_content):
    urls = []
    start_tag = '<a class="navPages" href="'
    end_quote = '"'

    start_index = 0
    while start_index != -1:
        start_index = html_content.find(start_tag, start_index)

        if start_index != -1:
            start_index += len(start_tag)
            end_index = html_content.find(end_quote, start_index)
            if end_index != -1:
                url = html_content[start_index:end_index]
                urls.append(url)
                start_index = end_index

    return urls

target = "The topic or board you are looking for appears to be either missing or off limits to you."

for i in range(541, 5020):
    print(f"#{i}")
    url_main = f"https://modarchive.org/forums/index.php?topic={i}.0"
    #url = "https://modarchive.org/forums/index.php?topic=869.0"
    try:
        response = requests.get(url_main)
        if response.status_code != 200:
            print(response.status_code)
            pass
        html = response.text
        if target in html:
            pass
        else:
            urls = extract_urls(html)
            urls.append(url_main)
            #print("\n".join(urls))
            for url in set(urls):
                requests.get(f"https://web.archive.org/save/{url}")
                print(url)
                time.sleep(1)


    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    time.sleep(1)
