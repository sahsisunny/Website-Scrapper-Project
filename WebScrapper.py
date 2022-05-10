# Imports Modules
import os
import webbrowser

import pandas as pd
import requests
import snscrape.modules.twitter as sntwitter
from bs4 import BeautifulSoup


# Advance Search Twitter Tutorial Function
def tutForAdvSer():
    print("----Twitter Advance Search Tutorial----")
    print("---------------------------------------")
    print("\t\t1. In Hindi")
    print("\t\t2. In English")
    print("\t\t3. Exit")
    choice = int(input("Enter the Choice:"))

    if choice == 1:
        webbrowser.open("https://www.youtube.com/watch?v=8sDXM06jhr0")
    elif choice == 2:
        webbrowser.open("https://www.youtube.com/watch?v=eT0tmgQ18Oo")
    elif choice == 3:
        twitterMenu()
    else:
        print("Oops! Incorrect Choice.")


# Scrap Tweets from Query Function
def scrapTweetsFromAdvSearch():
    query = '<| QUERY |>'
    InputQuery = input("Enter the Query : ")
    query = query.replace("<| QUERY |>", InputQuery)
    limit = int(input("Enter the Number of Tweets : "))
    tweets = []
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        if len(tweets) == limit:
            break
        else:
            tweets.append(
                [tweet.user.username, tweet.date, tweet.content, tweet.likeCount, tweet.replyCount,
                 tweet.retweetCount])
    # Save Data in .CSV File
    df = pd.DataFrame(tweets, columns=['Username', 'Date', 'Tweets', 'Like Count', 'Reply Count', 'Retweet Count'])
    df.to_csv('TwitterData.csv', index=True, encoding='utf-8')
    print("Tweets Scrapping Done...............")


# Scrap Tweets From Username
def scrapTweetsUsername():
    query = "(from:<|USERNAME|>) -filter:replies"
    uName = input("Enter the Username : ")
    query = query.replace("<|USERNAME|>", uName)
    limit = int(input("Enter the Number of Tweets : "))
    tweets = []
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        if len(tweets) == limit:
            break
        else:
            tweets.append(
                [tweet.user.username, tweet.date, tweet.content, tweet.likeCount, tweet.replyCount,
                 tweet.retweetCount])
    # Save Data in .CSV File
    df = pd.DataFrame(tweets, columns=['Username', 'Date', 'Tweets', 'Like Count', 'Reply Count', 'Retweet Count'])
    df.to_csv('TwitterData.csv', index=True, encoding='utf-8')
    print("Tweets Scrapping Done...............")


# Main Twitter Menu Function
def twitterMenu():
    print("--------T W I T T E R  S C R A P-------")
    print("---------------------------------------")
    print("\t\t1. Go to Twitter Advance Search")
    print("\t\t2. Go to Tutorial Menu")
    print("\t\t3. Scrap Tweets(Advance Search)")
    print("\t\t4. Scrap Tweets(Username)")
    print("\t\t5. Exit")
    choice = int(input("Enter the Choice:"))
    if choice == 1:
        webbrowser.open("https://twitter.com/search-advanced?f=top")
        twitterMenu()
    elif choice == 2:
        tutForAdvSer()
    elif choice == 3:
        scrapTweetsFromAdvSearch()
    elif choice == 4:
        scrapTweetsUsername()
    elif choice == 5:
        exit(0)
    else:
        print("Oops! Incorrect Choice.")


def FlipDataScrap():
    Start_Price = input("\nEnter Starting Price : ")
    End_Price = input("Enter Ending Price : ")
    Page_Number = int(input("Enter Page Number: "))

    for i in range(1, Page_Number + 1):
        pageNum = str(i)
        url = '''https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=categorytree&p%5B%5D=facets.price_range.from%3D<|START|>&p%5B%5D=facets.price_range.to%3D<|END|>&page=<| PAGE |> '''
        url = url.replace("<|START|>", Start_Price)
        url = url.replace("<|END|>", End_Price)
        url = url.replace("<| PAGE |>", pageNum)
        response = requests.get(url)
        htmlContent = response.content
        soup = BeautifulSoup(htmlContent, 'html.parser')
        titles = []
        prices = []
        images = []
        ratings = []
        for d in soup.find_all('div', attrs={'class': '_2kHMtA'}):
            title = d.find('div', attrs={'class': '_4rR01T'})
            price = d.find('div', attrs={'class': '_30jeq3 _1_WHN1'})
            image = d.find('img', attrs={'class': '_396cs4 _3exPp9'})
            rating = d.find('div', attrs={'class': '_3LWZlK'})
            titles.append(title.string)
            prices.append(price.string)
            images.append(image.get('src'))
            ratings.append(rating.text)
        df = pd.DataFrame({'Model Name': titles, 'Price': prices, 'Images': images, 'Ratings': ratings})
        df.to_csv('Flipkart Mobile Data_' + pageNum + '.csv', encoding='utf-8')


# creating options for MAIN MENU
while True:
    os.system('cls')
    print('''
     __        __   _       ____                             _             
     \ \      / /__| |__   / ___|  ___ _ __ __ _ _ __  _ __ (_)_ __   __ _ 
      \ \ /\ / / _ \ '_ \  \___ \ / __| '__/ _` | '_ \| '_ \| | '_ \ / _` |
       \ V  V /  __/ |_) |  ___) | (__| | | (_| | |_) | |_) | | | | | (_| |
        \_/\_/ \___|_.__/  |____/ \___|_|  \__,_| .__/| .__/|_|_| |_|\__, | v1.0
                                                |_|   |_|            |___/  By -  Sunny Sahsi''')
    print("\t----------M A I N   M E N U---------")
    print("\t------------------------------------")
    print("\t\t1. Twitter")
    print("\t\t2. Flipkart Mobile Data")
    print("\t\t3. Exit")
    choice = int(input("Enter the Choice:"))
    if choice == 1:
        twitterMenu()
    elif choice == 2:
        FlipDataScrap()
    elif choice == 3:
        break
    else:
        print("Oops! Incorrect Choice.")
