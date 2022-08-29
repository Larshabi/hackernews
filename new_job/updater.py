import json
import requests
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from .new import hacker

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(hacker, 'interval', seconds=300)
    scheduler.start()