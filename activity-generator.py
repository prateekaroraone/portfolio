import os
import datetime
from random import randint
import subprocess

# Git configuration
GIT_USERNAME = "prateekaroraone"
GIT_EMAIL = "pratiek.arora7@gmail.com"

# Set Git user globally (only needed once, but included for completeness)
subprocess.call(["git", "config", "user.name", GIT_USERNAME])
subprocess.call(["git", "config", "user.email", GIT_EMAIL])

def create_commit(date):
    """Create a dummy commit with the given date."""
    with open('dummy.txt', 'a') as file:
        file.write(f"{date} - {randint(1, 1000)}\n")
    
    date_string = date.strftime('%Y-%m-%dT%H:%M:%S+01:00')

    os.environ['GIT_AUTHOR_DATE'] = date_string
    os.environ['GIT_COMMITTER_DATE'] = date_string
    
    subprocess.call(['git', 'add', 'dummy.txt'])
    subprocess.call(['git', 'commit', '-m', f'Activity for {date.strftime("%Y-%m-%d")}'])

def generate_activity(start_date, end_date, frequency=0.10):
    """
    Generate commits between start_date and end_date.
    Frequency reduced to 35% (previously 70%).
    """
    current_date = start_date
    while current_date <= end_date:
        # Decide whether to commit this day
        if randint(1, 100) <= frequency * 100:
            # Create 1–3 commits for the day (fewer than before)
            num_commits = randint(1, 2)
            for _ in range(num_commits):
                hour = randint(9, 18)
                minute = randint(0, 59)
                commit_date = datetime.datetime(
                    current_date.year,
                    current_date.month,
                    current_date.day,
                    hour,
                    minute
                )
                create_commit(commit_date)
        
        current_date += datetime.timedelta(days=1)

if __name__ == "__main__":
    start = datetime.date(2026, 6, 1)
    end = datetime.date(2026, 9, 5)
    generate_activity(start, end)
