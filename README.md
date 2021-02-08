# Backend-Test-Mederos

The project consists of the creation of a lunch menu created by an administrator. Two types of users (administrator and employees) have access to the application. The administrator can create the menu, modify it and see the orders that each worker has made. Employees can request a menu option and specify customizations of the option, the order must be made before 11:00 am. SQLite is used as a relational database management system (RDBMS.

The Project has three applications( users, menu and order):
-In the users application, users are identified and new users of the type employees are created.
-In the menu application (used by the administrator), menus are created and modified and the orders of the rest of the workers are seen. The menu table is created where all the menus are stored.
-In the order application (used by employees), orders are created with their customizations. The order table is created where all the orders are stored.
Tests performed: 
-In each application the urls used are tested, using the SimpleTestCase library.
 -In the order application, the time_now() function is tested, using the SimpleTestCase library.

Created users:
-User: Admin (administrator)  Password: Pol65Pol63
-User: Pepe (empleado)        Password: Pol63Pol65
-User: cesar(empleado)        Password: Pototo12	

Commands used:
-Raise server:
>> python manage.py runserver
-Perform test:
>> python manage.py test users
>> python manage.py test order
>> python manage.py test menu
