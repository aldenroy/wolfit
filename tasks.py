from celery import Celery
from flask import current_app
import requests

celery = Celery('tasks', backend='redis://localhost:6379/0', broker='redis://localhost:6379/0')

@celery.task
def post_activity(activity):
    url = "http://0.0.0.0:8080/api/activities"  # Update this URL as needed
    try:
        r = requests.post(url, json=activity)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        current_app.logger.error(f"Error invoking microservice: {e}")
