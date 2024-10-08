# app/scheduler.py
from apscheduler.schedulers.background import BackgroundScheduler

from app.fetchPolitics import fillDicPolitics
from app.fetchScience import fillDicScience
from app.fetchSports import fillDicSports
from app.fetchWorld import fillDicWorld

# Global variables to store fetched data
global_data = {
    'world': None,
    'politics': None,
    'science': None,
    'sports': None,
}

last_update = "00:00"

def task():
    global global_data
    global last_update
    global_data['world'] = fillDicWorld()
    global_data['politics'] = fillDicPolitics()
    global_data['science'] = fillDicScience()
    global_data['sports'] = fillDicSports()
    print("Data fetched and updated")

def start_scheduler():
    scheduler = BackgroundScheduler()
    
    # Schedule task to run at specified times
    # scheduler.add_job(task, 'cron', hour=19, minute=7)
    scheduler.add_job(task, 'cron', hour=12, minute=00)
    scheduler.add_job(task, 'cron', hour=0, minute=1)
    scheduler.start()
