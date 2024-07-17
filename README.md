# Reviews-Classification-and-Summarizer
Give link to get product summary

---

## Overview

This project involves the development of a Bi-LSTM model for performing advanced sentiment analysis on user reviews. In addition to this, a multithreaded web scraping solution has been implemented using Selenium to automatically retrieve, categorize, and summarize product reviews from provided links, significantly speeding up the data collection process. The Transformer-based BART model is used for summarizing the product reviews.

## Features

- **Bi-LSTM Model:** A Bidirectional Long Short-Term Memory (Bi-LSTM) model is used to perform sentiment analysis on user reviews, providing highly accurate results by considering the context from both directions in the text.
- **Multithreaded Web Scraping:** Utilizes multithreading and Selenium to efficiently scrape product reviews from the web, reducing the time required for data collection.
- **Automatic Categorization:** Automatically categorizes the scraped reviews into predefined categories.
- **Summarization:** Uses the Transformer-based BART model to summarize the product reviews, providing concise and relevant information.

## Technologies Used

- **Programming Languages:** Python
- **Libraries and Frameworks:**
  - **Deep Learning:** TensorFlow, Keras
  - **Data Analysis:** Pandas, NumPy
  - **Web Scraping:** Selenium
  - **Multithreading:** Threading library in Python
  - **Summarization:** Transformers (Hugging Face BART)

## Getting Started

### Prerequisites

- pandas
- selenium==4.22.0
- requests
- tensorflow
- scikit-learn
- matplotlib
- seaborn
- nltk
- stopwords
- transformers (Hugging Face)
- tf_keras==2.16.0 

### Installation

1. Clone the repository.

2. cd Reviews-Classification-and-Summarizer

3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

### Usage

1. **Running the application**
  Add the amazon anf flipkart product links in the main.py file and the program will automatically scrape the reviews of the products and give app reviews and summaries of the positive and negative reviews.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

By following the above instructions, you can replicate the project setup and run the sentiment analysis and summarization tasks effectively.
