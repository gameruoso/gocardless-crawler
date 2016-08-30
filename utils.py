from urllib.parse import urlparse
import json


# Get domanin from URL
def get_url_domain(url):
    try:
        domain = get_url_subdomain(url).split('.')
        return domain[-2] + '.' + domain[-1]
    except:
        return ''


# Get subdomain from URL
def get_url_subdomain(url):
    try:
        return urlparse(url).netloc
    except:
        return ''


# Strip last URL slash if exists
def strip_last_slash_from_url(url):
    if url[-1] != '/':
        return url
    return url[: -1]


# Consider url as static content if it contains '.'
def is_a_static_content(url):
    try:
        url_path = urlparse(url)[2]
        if '.' in url_path.split('/')[-1]:
           return True
        return False
    except:
        return False


# Check if the url belongs to the original domain
def is_url_in_original_domain(url, base_url):
    try:
        url_token = urlparse(url)[1].split('.')
        url_domain = url_token[-2] + '.' + url_token[-1]
        base_url_token = urlparse(base_url)[1].split('.')
        base_url_domain = base_url_token[-2] + '.' + base_url_token[-1]
        if base_url_domain == url_domain:
            return True
        return False
    except:
        return False


# Sort crawled links and save into file
def sitemap_to_file(pages):
    with open('sitemap.json', "w") as f:
        for page in pages:
            f.write(json.dumps(page) + '\n')