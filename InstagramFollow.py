from instapy import InstaPy
from instapy import smart_run

my_username = 'panoc.team'
my_password = 'panoc25'

def job():
session = InstaPy(username = insta_username,
                  password = insta_password,
                  headless_browser = True)

with smart_run(session):   
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=4590,
                                    min_followers=45,
                                    min_following=77)

        session.set_do_follow(true, percentage=100)
        session.set_dont_like(['nsfw', 'kia'])

        session.like_by_tags(['bmw', 'mercedesbenz'], amount=100)

schedule.every().day.at("6:00").do(job)
schedule.every().day.at("18:00").do(job)

while True:
schedule.run_panding()
time.sleep(10)
