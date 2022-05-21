from flask import Flask
import os
import openai


from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.environ.get('OPENAI_API_KEY')
app = Flask(__name__)

@app.route('/')
def hello():
    text="Classify the sentiment in these tweets:\n\n1. \"I can't stand homework\"\n2. \"This sucks. I'm bored 😠\"\n3. \"I can't wait for Halloween!!!\"\n4. \"My cat is adorable ❤️❤️\"\n5. \"I hate chocolate\"\n\nTweet sentiment ratings:",

    response = openai.Completion.create(engine="text-davinci-002", prompt=text, temperature=0.5, max_tokens=20)

    return response


if __name__ == '__main__':
    app.run(debug=True)