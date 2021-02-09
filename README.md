# Backend-Test-Mederos (Challenger Cornershop 🥑)

The project consists of the creation of a lunch menu created by an administrator. Two types of users (administrator and employees) have access to the application. The administrator can create the menu, modify it and see the orders that each worker has made. Employees can request a menu option and specify customizations of the option, the order must be made before 11:00 am. SQLite is used as the relational database.

## Applications

The project has three applications (users, menu and order):

* **Users app:** users are identified and new users of the type employees are created.
* **Menu app**: (used by the administrator), menus are created and modified and the orders of the rest of the workers are seen. The menu table is created where all the menus are stored.
* **Order app:** (used by employees), orders are created with their customizations. The order table is created where all the orders are stored.

## Tests suits

* In each application the urls used are tested, using the SimpleTestCase library's django.
* In the order application, the time_now() function is tested, using the SimpleTestCase library's django.

## Users

| Type     | User  | Password   |
|----------|-------|------------|
| Admin    | Admin | Pol65Pol63 |
| Employee | Pepe  | Pol63Pol65 |
| Employee | cesar | Pototo12   |	

## Commands

* Up server:

	* `python manage.py runserver`

* Execute tests:

	*  `python manage.py test users`
 
	*  `python manage.py test order`
 
	*  `python manage.py test menu`

## To do

* Python script for to send the notification message with the link of the menu of the day to Slack API. [ref](https://api.slack.com/messaging/sending#composing)
* Schedule job (send a message) to run every day (Monday to Friday) at 9:00 am (Chilean Time):
	* Django-celery for execute periodic work. [documentation](https://docs.celeryproject.org/en/latest/faq.html#what-kinds-of-things-should-i-use-celery-for)
	* Cronjob `0 9 * * 1-5` [ref](https://crontab.guru/#0_9_*_*_1-5)
* Add more tests.

## Author

Julio C. Mederos Arias [juliomederosarias@gmail.com](mailto:juliomederosarias@gmail.com)

---
### Happy Coding 🎉
