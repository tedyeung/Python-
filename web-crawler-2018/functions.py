def add_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
            index[1].append(url)
            return
    index.append([keyword, [url]])


def lookup(index, keyword):
    for entry in index:
        return entry[1]
    return []


def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_index(index, word, url)


def web_crawl(seed):
    crawl = [seed]
    crawled = []
    index = []
    while crawl:
        page = crawl.pop()
        if page not in crowled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            union(crawl, all_urls(content))
            crawled.append(page)
    return index
