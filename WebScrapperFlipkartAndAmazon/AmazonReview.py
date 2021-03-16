import requests
from bs4 import BeautifulSoup as bs

def ScrapAmazonReview(url):
    '''

    Provide the url for Scaraping The reviews for 20 pages
    :param Url:
    :return:  person name,reviews,date of Post
    '''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', }
    # hit the url using request Obejct

    url=requests.get(url,headers=headers)
    # Change the request object in Beautiful soup object

    amzn_html=bs(url.text, "html.parser")

    # extract the see all reviews page

    bigboxes = amzn_html.findAll("div", {
        "id": "reviews-medley-footer"})

    new_url = 'https://www.amazon.in/'+bigboxes[0].a['href']
    # Goto All Reviews pages and Extatrct the url for pages
    all_review=requests.get(new_url,headers=headers)
    all_review_page=bs(all_review.text,"html.parser")
    review_boxes=all_review_page.findAll("div", {
        "id": "cm_cr-review_list"})
    # get the url for pages
    url_pages=review_boxes[0].findAll("div",{"class":"a-form-actions a-spacing-top-extra-large"})
    url_pagesval='https://www.amazon.in/'+url_pages[0].a['href']
    review=[]
    reviewer_name = []
    review_text = []
    review_date = []
    my_url=[]
    for i in range(1,21):
        page_no='pageNumber='+str(i)
        url_val=url_pagesval.replace('pageNumber=2',page_no)
        review_page=requests.get(url_val,headers=headers)
        review_page_html=bs(review_page.text,"html.parser")
        review_box_for_page=review_page_html.findAll("div", {
        "id": "cm_cr-review_list"})
        commentboxes=review_box_for_page[0].findAll("div",{"data-hook":"review"})

        for val in commentboxes:
            reviewer=val.div.findAll('div')[0].a.findAll('span',{'class':'a-profile-name'})[0]
            date_review = val.div.findAll('div')[0].findAll('span', {"data-hook":"review-date"})
            review_body=val.div.findAll('div')[0].findAll('span', {"data-hook":"review-body"})
            # print(review_body[0].text)
            reviewer_name.append(reviewer.text)
            review_date.append(date_review[0].text)
            review_text.append(review_body[0].text)
            my_url.append(url_val)
            #print(val.div.findAll('div')[0].a.findAll('span',{'class':'a-profile-name'}))
    # print(reviewer_name)
    # print(review_date)
    # print(review_text)

    return reviewer_name,review_text,review_date,my_url
    #print(len(my_url))
    # print(my_url)


