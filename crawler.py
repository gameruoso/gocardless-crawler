import requests
from utils import *
from bs4 import BeautifulSoup
from urllib.parse import urljoin



class Crawler:
    base_url = ''
    domain = ''
    queue = set()
    crawled_links = set()
    result = []

    def __init__(self, base_url):
        Crawler.base_url = strip_last_slash_from_url(base_url)
        Crawler.domain = get_url_domain(base_url)
        # Add the first URL to the queue
        Crawler.queue.add(Crawler.base_url)
        self.crawl_page(Crawler.base_url)

    # Crawl page
    @staticmethod
    def crawl_page(page_url):
        if page_url not in Crawler.crawled_links:
            url_list, static_content_list = Crawler.get_urls(Crawler.base_url, page_url)
            Crawler.add_links_to_queue(url_list)
            Crawler.queue.remove(page_url)
            Crawler.crawled_links.add(page_url)
            Crawler.result.append({"page": page_url, "static_content": list(static_content_list)})
            print('page: : ' + str(page_url) + ', static_content: ' + str(list(static_content_list)))


    # Fetch links and static links of a given URL
    @staticmethod
    def get_urls(base_url, url_to_parse):
        links = set()
        static_content = set()
        try:
            page_source_code = requests.get(url_to_parse)
            html_string = page_source_code.text
            soup = BeautifulSoup(html_string, 'html.parser')
            all_links = soup.find_all('a')

            for link in all_links:
                href = link.get('href')
                url = urljoin(base_url, href)
                url = strip_last_slash_from_url(url)
                if is_url_in_original_domain(base_url, url):
                    links.add(url)
                    if is_a_static_content(url):
                        static_content.add(url)

        except Exception as e:
            print(str(e))
            return set(), set()

        return links, static_content

    # Add new urls to queue ONLY IF they are not already in queue/crawled
    @staticmethod
    def add_links_to_queue(urls):
        for url in urls:
            if (url in Crawler.queue) or (url in Crawler.crawled_links):
                continue
            Crawler.queue.add(url)
