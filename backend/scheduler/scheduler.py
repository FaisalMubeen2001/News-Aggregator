from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from backend.scheduler.jobs import fetch_and_enrich_articles

scheduler = BackgroundScheduler()


def start_scheduler():
    scheduler.add_job(
        fetch_and_enrich_articles,
        trigger=IntervalTrigger(minutes=30),
        id="fetch_articles_job",
        name="Fetch and enrich articles every 30 minutes",
        replace_existing=True
    )
    scheduler.start()
    print("✅ Scheduler started - articles will refresh every 30 minutes.")


def stop_scheduler():
    scheduler.shutdown()
    print("🛑 Scheduler stopped.")