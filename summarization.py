import pandas as pd
from transformers import pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

class Summary:

    def __init__(self, amazon_df, flipkart_df):
        self.amazon_df = amazon_df
        self.amazon_df['Star'] = self.amazon_df['Star'].astype(int, errors='ignore')
        self.flipkart_df = flipkart_df
        self.flipkart_df['Star'] = self.flipkart_df['Star'].astype(int, errors='ignore')

    
    def make_summary(self, text_to_summarize):
        summary = summarizer(text_to_summarize, min_length=50, do_sample=False)
        return (summary[0]['summary_text'])
        

    def summarize_amazon(self):
        positive = ''
        negative = ''
        for index, row in self.amazon_df.iterrows():
            if int(row['Star']) >= 3:
                positive  = positive + '. ' + row['Description']
            else:
                negative  = negative + '. ' + row['Description']

        positive = positive[:1000]
        negative = negative[:1000]
        
        print("Positive review summary from amazon: \n")
        print(self.make_summary(positive))
        print("\n Negative review summary from amazon: \n")
        print(self.make_summary(negative))

    def summarize_flipkart(self):
        positive = ''
        negative = ''
        for index, row in self.flipkart_df.iterrows():
            if int(row['Star']) >= 3:
                positive  = positive + '. ' + row['Description']
            else:
                negative  = negative + '. ' + row['Description']
        
        positive = positive[:1000]
        negative = negative[:1000]

        print("Positive review summary from flipkart: \n")
        print(self.make_summary(positive))
        print("\n Negative review summary from flipkart: \n")
        print(self.make_summary(negative))

    def summarize(self):
        self.summarize_amazon()
        self.summarize_flipkart()