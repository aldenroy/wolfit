from app.helpers import pretty_date
from datetime import datetime, timedelta

def test_now():
    assert pretty_date(datetime.utcnow()) == "just now"
    assert pretty_date(datetime.utcnow() - timedelta(seconds=59)) == "59 seconds ago"
    assert pretty_date(datetime.utcnow() - timedelta(seconds=119)) == "a minute ago"
    assert pretty_date(datetime.utcnow() - timedelta(seconds=3599)) == "59 minutes ago"
    assert pretty_date(datetime.utcnow() - timedelta(seconds=7199)) == "an hour ago"
    assert pretty_date(datetime.utcnow() - timedelta(seconds=86399)) == "23 hours ago"
 
def test_about_now():
    assert (pretty_date(datetime.utcnow() - timedelta(days = -1))) == "just about now" 
    
def test_yesterday():
    assert (pretty_date(datetime.utcnow() - timedelta(days = 1))) == "Yesterday"
    
def test_days_ago():
    assert (pretty_date(datetime.utcnow() - timedelta(days = 6))) == "6 days ago"
    
def test_weeks_ago():
    assert (pretty_date(datetime.utcnow() - timedelta(days = 30))) == "4 weeks ago"
    
def test_months_ago():
    assert (pretty_date(datetime.utcnow() - timedelta(days = 364))) == "12 months ago"
    
def test_years_ago():
    assert (pretty_date(datetime.utcnow() - timedelta(days = 1000))) == "2 years ago"
    
def test_not_time():
    assert pretty_date()