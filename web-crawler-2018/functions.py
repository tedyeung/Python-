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
