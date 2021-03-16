import requests
from bs4 import BeautifulSoup as bs


def ScrapFlipkart(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', }
    # hit the url using request Obejct

    url = requests.get(url, headers=headers)
    flipkrt_html = bs(url.text, "html.parser")
    bigboxes = flipkrt_html.findAll("div", {
        "class": "_3UAT2v _16PBlm"})
    review_page_url = requests.get('https://www.flipkart.com' + bigboxes[0].parent['href'])
    reviews_html = bs(review_page_url.text, "html.parser")
    review_box = reviews_html.findAll("div", {
        "class": "_1YokD2 _3Mn1Gg col-9-12"})
    review=review_box[0].findAll('div',{'class':'_1AtVbE col-12-12'})
    page_div=review[-1]
    del review[-1]
    page_url='https://www.flipkart.com'+page_div.div.div.a['href']
    #print(page_url)
    reviewer_name = []
    review_text = []
    review_date = []
    url_val=[]
    for i in range(1, 21):
        page_no = 'page=' + str(i)
        page_url_val=page_url.replace('page=1',page_no)
        review_page_url = requests.get(page_url_val)
        reviews_html = bs(review_page_url.text, "html.parser")
        review_box = reviews_html.findAll("div", {
            "class": "_1YokD2 _3Mn1Gg col-9-12"})
        if len(review_box)!=0:
            review = review_box[0].findAll('div', {'class': '_1AtVbE col-12-12'})
        #print(review)
        commentboxes=review
        for val in commentboxes:
            try:
                reviewer=val.findAll('div',{'class':'col _2wzgFH K0kLPL'})
                if len(reviewer)!=0:
                    reviewer_name.append(reviewer[0].findAll("p",{"class":"_2sc7ZR _2V5EHH"})[0].text)
                    review_text.append(reviewer[0].findAll("div",{"class":"t-ZTKy"})[0].text.replace('READ MORE',''))
                    review_date.append(reviewer[0].findAll("div",{"class":"row _3n8db9"})[0].findAll('p',{'class':'_2sc7ZR'})[1].text)
                    url_val.append(page_url_val)
            except:
                pass
    return reviewer_name,review_text,review_date,url_val
    #print(url_val)