from src.amazon_webscrapping import Amazon
import pandas as pd

def main():
    url = 'https://www.amazon.in/HP-i5-1235U-15-6-inch-graphics-speakers/dp/B0CTKHTNWL/ref=sr_1_4?dib=eyJ2IjoiMSJ9.9zhNTtyM6wB18-nU56oobiIA_iHvbszw-zCKLZGEvW5qrNqEtAX6yfYSwYe4H8pURPZVTeXA6cK8xFa_yNDypRetrHBhVEkrSjwfRQe3X7aZsMfe43doKFkIlLO0vvq6ysy9qd398TlGCfEPX8nSqCf7gIJwIqKoANeOSpzL8dNxRvN4wE79-ZoDQ5AIKuiudxTkGJ5p46io1n4x-QUfI9PdYG7qPhQ9o9Rkb-nOW2k.UcuOKL58ddW5gGa4mLWzXUDeUaTIVr9rLtQ3ZgQwEd0&dib_tag=se&keywords=laptop&qid=1720863278&sr=8-4&th=1'
    amazon_scraper = Amazon(url)
    dict = amazon_scraper.get_all_reviews()

    df = pd.DataFrame(dict, columns = dict.keys())
    print(df)
    df.to_csv("Review.csv")

if __name__ == "__main__":
    main()
