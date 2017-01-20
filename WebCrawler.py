##def get_page(url):
##    try:
##        import urllib
##        return urllib.urlopen(url).read()
##    except:
##        return ""


def get_page(url):
    try:
        if url == "http://www.udacity.com/cs101x/index.html":
            return ('<html> <body> This is a test page for learning to crawl! '
            '<p> It is a good idea to '
            '<a href="http://www.udacity.com/cs101x/crawling.html">learn to '
            'crawl</a> before you try to  '
            '<a href="http://www.udacity.com/cs101x/walking.html">walk</a> '
            'or  <a href="http://www.udacity.com/cs101x/flying.html">fly</a>. '
            '</p> </body> </html> ')
        elif url == "http://www.udacity.com/cs101x/crawling.html":
            return ('<html> <body> I have not learned to crawl yet, but I '
            'am quite good at '
            '<a href="http://www.udacity.com/cs101x/kicking.html">kicking</a>.'
            '</body> </html>')
        elif url == "http://www.udacity.com/cs101x/walking.html":
            return ('<html> <body> I cant get enough '
            '<a href="http://www.udacity.com/cs101x/index.html">crawling</a>! '
            '</body> </html>')
        elif url == "http://www.udacity.com/cs101x/flying.html":
            return ('<html> <body> The magic words are Squeamish Ossifrage! '
            '</body> </html>')
    except:
        return ""
    return ""

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        url = None
        end_quote = 0
    else:
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1:end_quote]

    return url, end_quote

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)


def get_all_links(page):
    link_list = []
    while (get_next_target(page) != None,0):
        url, endpos = get_next_target(page)
        if url:
            link_list.append(url)
            page=page[endpos:]
        else:
            break
    return link_list

index = []

##def record_user_click(index, keyword, url):
##    urls = lookup(index, keyword)
##    if urls:
##        for entry in urls:
##            if entry[0] == url:
##                entry[1] = entry[1]+1
##
##def add_to_index(index, keyword, url):
##    # format of index: [[keyword, [[url, count], [url, count],..]],...]
##    index = {}
##    for entry in index:
##        if entry[0] == keyword:
##            for urls in entry[1]:
##                if urls[0] == url:
##                    return
##            entry[1].append([url,0])
##            return
##    # not found, add new keyword to index
##    index.append([keyword, [[url,0]]])

def add_to_index(index, keyword, url):
    if keyword in index:
        index[keyword].append(url)
    index[keyword] = [url]
    

def add_page_to_index(index,url,content):
    content_split = content.split()
    for keywords in content_split:
        add_to_index(index,keywords,url)

def lookup(index,keyword):
    if keyword in index:
        return index[keyword]
    return []

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index =  {}
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index,page,content)
            union(tocrawl, get_all_links(content))
            crawled.append(page)
    return crawled

## ___________Crawl with page maximum____________
##def crawl_web(seed, max_pages):
##    tocrawl = [seed]
##    crawled = []
##    while tocrawl and len(crawled) < max_pages:
##        page = tocrawl.pop()
##        if page not in crawled:
##            union(tocrawl, get_all_links(get_page(page)))
##            crawled.append(page)
##    return crawled

## ___________Crawl with depth maximum____________
##def crawl_web(seed,max_depth):    
##    tocrawl = [seed]
##    crawled = []
##    next_depth = []
##    depth = 0
##    while tocrawl and depth <= max_depth:
##        page = tocrawl.pop()
##        if page not in crawled:
##            union(next_depth, get_all_links(get_page(page)))
##            crawled.append(page)
##        if not tocrawl:
##            tocrawl, next_depth = next_depth, []
##            depth = depth + 1
##    return crawled

url = "http://www.udacity.com/cs101x/index.html"

print crawl_web(url, 3)
