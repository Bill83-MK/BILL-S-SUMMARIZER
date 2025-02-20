from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
import re

# Initialize FastAPI app
app = FastAPI()

# Load the summarization model
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

class TextRequest(BaseModel):
    text: str

def clean_text(text):
    """Pre-process text by removing extra spaces and URLs."""
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = re.sub(r'http\S+', '', text)  # Remove links
    return text.strip()

def summarize_text(text, max_len=50):
    """Summarize text while dynamically adjusting max_length."""
    text = clean_text(text)
    input_words = text.split()
    input_length = len(input_words)  # Count words in input text

    if input_length < 5:
        return "Text too short for summarization."

    # Limit input to 512 words (model constraint)
    if input_length > 512:
        input_words = input_words[:512]
        text = " ".join(input_words)

    # Adjust summarization length
    adjusted_max_length = min(max_len, input_length)

    summary = summarizer(text, max_length=adjusted_max_length, min_length=10, do_sample=False)
    return summary[0]['summary_text']

@app.post("/summarize")
def summarize(request: TextRequest):
    summary = summarize_text(request.text)
    return {"summary": summary}
