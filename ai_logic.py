import openai

OPENAI_API_KEY = "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"
openai.api_key = OPENAI_API_KEY

def classify_sentiment(user_message):
    if "love" in user_message or "great" in user_message:
        return "positive"
    elif "okay" in user_message or "fine" in user_message:
        return "neutral"
    else:
        return "negative"

def generate_reply(user_message):
    sentiment = classify_sentiment(user_message)

    if sentiment == "positive":
        return "Glad you liked it! Want to upgrade to our premium version?"
    elif sentiment == "neutral":
        return "Let me know if you need help with anything!"
    else:
        return "Oh no! Would you like to talk to support?"
