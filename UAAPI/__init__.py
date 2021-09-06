from pip._internal import main as pip

try:
    from requests_html import HTMLSession
except:
    pip(["install","requests-html"])
    from requests_html import HTMLSession

def getInfo(url):
    s = HTMLSession()
    r = s.get(url)
    r.html.render()

    product = {
        "title": r.html.xpath("//*[@id='productTitle']", first=True).text,
        "price": r.html.xpath("//*[@id='priceblock_ourprice']", first=True).text,
        "url": url
    }

    return product
