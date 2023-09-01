from celery import Celery
import requests
import uuid

r = requests.Session()

# app = Celery('tasks', broker='pyamqp://guest@localhost//')
app = Celery('tasks', broker='amqps://xyflaopn:30d4kbm9LnAQDsSEAkckr-3tKC5daNmA@puffin.rmq2.cloudamqp.com/xyflaopn')

@app.task
def fetch(url: str) -> bool:
    try:
        req = r.get(url)
        if req.ok:
            with open(f"./pages/{uuid.uuid4()}_{url.split('://')[1]}.html", "wb") as file:
                file.write(req.content)
            return True
    except:
        print(f"Error while fetching: {url}")
    return False