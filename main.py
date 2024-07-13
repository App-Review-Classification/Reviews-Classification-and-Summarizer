from src.amazon_webscrapping import Amazon
from src.flipkart_webscrapping import Flipkart
import pandas as pd

def main():
    url = 'https://www.flipkart.com/apple-iphone-15-pink-128-gb/p/itm7579ed94ca647?pid=MOBGTAGPNMZA5PU5&lid=LSTMOBGTAGPNMZA5PU51YWTGZ&marketplace=FLIPKART&q=mobile+iphone&store=tyy%2F4io&srno=s_1_4&otracker=search&otracker1=search&fm=Search&iid=e73c2247-b211-47e1-b39f-ec078d92f2b9.MOBGTAGPNMZA5PU5.SEARCH&ppt=pp&ppn=pp&ssid=p2illcz7800000001720872195500&qH=0747fed614fc520e'
    # amazon_scraper = Amazon(url)
    # dict = amazon_scraper.get_all_reviews()

    flipkart_scrapper = Flipkart(url)
    dict = flipkart_scrapper.get_all_reviews()

    df = pd.DataFrame(dict, columns = dict.keys())
    print(df)
    df.to_csv("Review.csv")

if __name__ == "__main__":
    main()
