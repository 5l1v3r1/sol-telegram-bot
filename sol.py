from flask import Flask
app = Flask(__name__)
import lxml.html
from lxml.cssselect import CSSSelector
import mechanize
import credentials

browser = mechanize.Browser()
cookies = mechanize.CookieJar()

username = credentials.secret_dict['sol_customer_no']
password = credentials.secret_dict['sol_password']

@app.route('/')
#Get the AKK (Fair Usage Quota) information for the ISP - Superonline
def get_akk():
    akk = ""
    browser.set_handle_robots(False)
    browser.addheaders = [('User-agent',
                           'Mozilla/5.0 (X11; U; Linux i686; en-US)     AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
    try:
        browser.open("http://www.superonline.net")
        browser.select_form(nr=0)
        browser.form['customerNo'] = username
        browser.form['password'] = password
        response = browser.submit()
    except:
        pass
    kaynak = browser.open("http://superonline.net").read()
    tree = lxml.html.fromstring(kaynak)
    sel = CSSSelector('strong')
    results = sel(tree)
    match = results[0]
    lxml.html.tostring(match)
    akk = match.text

    return akk

if __name__ == '__main__':
    #Please, set to False in deployment.
    app.debug = True
    app.run()


