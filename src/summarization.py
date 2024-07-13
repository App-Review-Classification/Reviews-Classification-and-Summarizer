from transformers import pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def make_summary(text_to_summarize):
    summary = summarizer(text_to_summarize, min_length=50, do_sample=False)
    return (summary[0]['summary_text'])