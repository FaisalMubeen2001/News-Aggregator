from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.cron import CronTrigger
from backend.scheduler.jobs import fetch_and_enrich_articles, send_digest_job

scheduler = BackgroundScheduler()


def start_scheduler():
    scheduler.add_job(
        fetch_and_enrich_articles,
        trigger=IntervalTrigger(minutes=30),
        id="fetch_articles_job",
        name="Fetch and enrich articles every 30 minutes",
        replace_existing=True
    )

    scheduler.add_job(
        send_digest_job,
        trigger=CronTrigger(hour=8, minute=0),
        id="daily_digest_job",
        name="Send daily email digest at 8:00 AM",
        replace_existing=True
    )

    scheduler.start()
    print("✅ Scheduler started - articles will refresh every 30 minutes.")
    print("✅ Daily digest scheduled at 8:00 AM every day.")


def stop_scheduler():
    scheduler.shutdown()
    print("🛑 Scheduler stopped.")