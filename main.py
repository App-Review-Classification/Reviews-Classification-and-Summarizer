from src.amazon_webscrapping import Amazon

def main():
    url = 'https://www.amazon.in/Acer-Premium-Windows-AL15-41-Display/dp/B0CB7S1RTX/ref=sr_1_1_sspa?crid=2OHPBTHGHJLMA&dib=eyJ2IjoiMSJ9.9zhNTtyM6wB18-nU56oobiIA_iHvbszw-zCKLZGEvW5qrNqEtAX6yfYSwYe4H8pURPZVTeXA6cK8xFa_yNDypRetrHBhVEkrSjwfRQe3X7aZsMfe43doKFkIlLO0vvq6ysy9qd398TlGCfEPX8nSqPFlHxk1zOR3nP5GDXl9bugq2iF0g1CJ0OXqqbsmTRHiHrpO0rUXiGEJKmgsywEWPJvtXmEIcXJWG0pkbiugb7w.GYAHtLH-Z4N4CW0abKaAxAdVii5DxsHG1N5y5iXTiag&dib_tag=se&keywords=laptop&qid=1720851014&sprefix=laptop%2Caps%2C254&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1'
    amazon_scraper = Amazon(url)
    amazon_scraper.get_reviewpage()

if __name__ == "__main__":
    main()
