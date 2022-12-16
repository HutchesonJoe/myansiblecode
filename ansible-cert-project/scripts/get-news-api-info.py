#!/usr/bin/python3
# cleans up data from news API

import requests
import argparse

def main(): 
    news = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={args.api_key}")
    total_results = news.json()['totalResults']
    article_index = args.articlenumber  #input(f"You have {total_results} articles. Pick a number between 1 and {total_results}: ")
    article = news.json()['articles'][int(article_index)]
    print(article)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('articlenumber')
    parser.add_argument('api_key')
    args = parser.parse_args()
    #print(args.articlenumber)
    main()
