import prime.constants as c
from prime.prime import Prime
from email.email import Email

# Triggering the entire project
# Do this by python run.py


def run():
    p = Prime(start=c.START, finish=c.FINISH)
    prettier = p.prettify()
    print(prettier)
    new_email = Email()
    new_email.to = "JohnDoe@email.com"
    new_email.subject = f"Prime Numbers execution betwee {c.START} to {c.FINISH}"
    new_email.body = prettier
    new_email.send()


if __name__ == "__main__":
    run()
