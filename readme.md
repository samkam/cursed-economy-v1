# Cursed Economy

A "would you rather" website where users can submit their own ideas into the deck.


Learning project using Django's admin functionality and built-in forms to have a website where only registered users are able to submit new curses to the deck, but anyone can vote on existing curses. 


Currently abandoned, working the same idea from the ground up using TDD.

to run:

`pip install -r requirements.txt`
`python manage.py runserver`

Current issues:
* sign up page currently broken. Can only create new accounts through admin
* no curses in database on repository (need to find way to initialize from csv for instance)
* Not hosted (yet)
* No end-to-end tests