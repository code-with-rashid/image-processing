# Image Processing

## Getting Started

### Clone the Repository
```bash
$ https://github.com/code-with-rashid/image-processing.git
```

### Docker setup
Make sure Docker and Docker Compose are installed on your system. Navigate to the project directory and run the following commands:
```bash
$ make redo-db
```
Access the APIs at:<br>
http://127.0.0.1:8000/api/schema/swagger/

## Development Steps
#### Clone the Project:
```bash
$ git clone https://github.com/rashiidmahmood/image_processing_assignment.git
```
#### Install Dependencies:
Ensure that python3 and pip3 are installed on your system. Inside the project's root directory, install requirements (consider using a virtual environment):
```bash
$ pip install -r ./requirements/local.txt
```
#### Apply Database Migrations:
Run the following command to apply migrations into the database:
```bash
$ python manage.py migrate
````
#### Process Excel File:
Run the following management command to process the Excel file and save resized images into the database:
```bash
$ python manage.py process_excel_images data/img.csv
```
#### Start the Server:
Run the following command inside the project directory to start the server:
```bash
$ python3 manage.py runserver 8000
```
#### Swagger UI:
Open Swagger UI to access all project APIs:<br>
http://127.0.0.1:8000/api/schema/swagger/
#### Public API - Images List:
Access the public Images List API to list and filter images stored in the database without authentication.
#### Upload Excel Option:
Users can upload an Excel file at the following URL, where the code will be applied, and the images will be saved in the database:<br>
http://127.0.0.1:8000/images/process-csv/

### Tests
Run the following command to execute test cases:
```bash
$ make test
```
