import threading
from queue import Queue
from crawler import Crawler
from utils import *

HOMEPAGE = 'https://gocardless.com/'

NUMBER_OF_THREADS = 16
thread_queue = Queue()
Crawler(HOMEPAGE)


# Create worker threads
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


# Do the next job in the queue
def work():
    while True:
        url = thread_queue.get()
        Crawler.crawl_page(url)
        thread_queue.task_done()


# Each queued link is a new job
def create_jobs():
    for link in Crawler.queue:
        thread_queue.put(link)
    thread_queue.join()
    crawl()


# Check if there are items in the queue, if so crawl them, if not output result to file
def crawl():
    queued_links = Crawler.queue
    if len(queued_links) > 0:
        create_jobs()
    else:
        sitemap_to_file(Crawler.crawled_links)


create_workers()
crawl()
sitemap_to_file(Crawler.result)
