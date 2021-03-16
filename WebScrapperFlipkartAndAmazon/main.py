import time

import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
import pandas as pd
from AmazonReview import ScrapAmazonReview
from Flipkartreview import ScrapFlipkart
from Sentiments import getSentiments


if __name__=="__main__":
    flipkar_reviews_text=[]
    flipkar_reviews_person=[]
    flipkar_review_date=[]
    flipkar_all_url=[]
    flipkart_url=['https://www.flipkart.com/XX/p/XXX?pid=PSAEUD8KADJ67RMY&marketplace=GROCERY','https://www.flipkart.com/XX/p/XXX?pid=CKBEUC5CFC6CAZR7&marketplace=GROCERY']
    print('-' * 50)
    print('Starting Flipkart scraping ')
    print('-' * 50)
    for val in flipkart_url:
        name,review,date,url=ScrapFlipkart(val)
        for name in name:
            flipkar_reviews_person.append(name)
        for review in review:
            flipkar_reviews_text.append(review)
        for date in date:
            flipkar_review_date.append(date)
        for url in url:
            flipkar_all_url.append(url)
    print('-'*50)
    print('Total Data Extracted ='+str(len(flipkar_reviews_text)))
    print('Generating Sentiments for Flipkart Reviews')
    sentiments=[]
    for val in flipkar_reviews_text:
        sentiments.append(getSentiments(val))
    print('Creating Excel for Flipkart Data ')
    df=pd.DataFrame()
    df['Users']=flipkar_reviews_person
    df['Date']=flipkar_review_date
    df['Reviews']=flipkar_reviews_text
    df['Url']=flipkar_all_url
    df['Sentiments']=sentiments
    df.to_excel('Flipkart.xlsx', index = False)


    # Amazon Reviews
    amzn_reviews_text = []
    amzn_reviews_person = []
    amzn_review_date = []
    all_url_val=[]
    amzn_url = ['https://www.amazon.in/dp/B07MLRYM4G','https://www.amazon.in/dp/B07M78D1JD','https://www.amazon.in/dp/B07MLRWR36']
    print('-' * 50)
    print('Starting Amazon scraping ')
    print('-' * 50)
    for val in amzn_url:
        ScrapAmazonReview(val)
        name, review, date ,url= ScrapAmazonReview(val)
        for name in name:
            amzn_reviews_person.append(name)
        for review in review:
            amzn_reviews_text.append(review)
        for date in date:
            amzn_review_date.append(date)
        for url in url:
            all_url_val.append(url)

    print('-' * 50)
    print('Total Data Extracted =' + str(len(amzn_reviews_text)))
    print('Generating Sentiments for Amazon Reviews')
    sentiments_amaz = []
    for val in amzn_reviews_text:
        sentiments_amaz.append(getSentiments(val))
    print('Creating Excel for Amazon Data ')
    df = pd.DataFrame()
    df['Users'] = amzn_reviews_person
    df['Date'] = amzn_review_date
    df['Reviews'] = amzn_reviews_text
    df['Url'] = all_url_val
    df['Sentiments'] = sentiments_amaz
    df.to_excel('Amazon.xlsx', index=False)


