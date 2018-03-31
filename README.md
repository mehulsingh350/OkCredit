## Dependencies and installation commands
* Python 2.7
* Django 1.1.4 `pip3 install django`
* Django Rest Framework `pip install django restframework`
## Significance of different files in the project
* **models.py** - Defines database used in the project.
* **urls.py** - To specify the API urls for the project
* **views.py** - To specify the action when a url is hit
* **serializers.py** - File for data serialization to store in database
## Running the project
Clone the repo and in the project root directory run the following commands:  
> `python manage.py makemigrations`  
`python manage.py migrate`  
`python manage.py runserver`  

A server will get started at `127.0.0.1:8000`  
Then send get/post request at `127.0.0.1:8000/getlist`
## Workflow
* When the user hit a url, it first see to which view it it linked. Views are specified using python class.
* Views are using serializers to convert the data object into `jSON`(serialization) to save it into the database.
* After serialization the data gets saved into database(In case of a post request) and the view will provide the appropriate response to the user in return.
