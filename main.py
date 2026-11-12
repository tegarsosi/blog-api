from flask import Flask

app = Flask(__name__)

@app.get("/posts")
def get_posts():
    return [], 200