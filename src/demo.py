# Original URL
url = 'https://www.flipkart.com/apple-2022-macbook-air-m2-8-gb-256-gb-ssd-mac-os-monterey-mly13hn-a/product-reviews/itm2e7b5e998f058?pid=COMGFB2GBKDVYBDD&lid=LSTCOMGFB2GBKDVYBDDM2PGFI&marketplace=FLIPKART&page=2'

# Find the position of the 'page=' parameter
page_index = url.find('page=')
print(page_index)

# If 'page=' is found, replace the last character with '3'
if page_index != -1:
    new_url = url[:page_index + len('page=')] + '3'
    print("Updated URL:", type(new_url))
else:
    print("Page parameter not found in the URL")
