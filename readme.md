# Personal Data Generator Django App

The Personal Data Generator is a Django application that enables you to generate various sets of personal data. This `README` provides an overview of the app's features and how to use it.

## Data Generation Modes

The app operates in three main data generation modes:

### Basic Mode:
- Fields: First Name, Last Name

### PESEL Mode:
- Fields: First Name, Last Name, Date of Birth, PESEL (Personal Identification Number)

### Full Mode:
- Fields: First Name, Last Name, Date of Birth, PESEL, Identity Card, Phone Number, Address

## Data Sources

Data is generated based on two types of data sources:

1. Generation based on predefined rules, such as the PESEL, with data validation included in the testing section.
2. Data retrieved from external sources, such as addresses or names. You have the option to load data in limited quantities using the following endpoint:
http://localhost:8000/loading_data/<int:limit>


## API for Data Generation

The app provides an API for generating data in JSON format. You can specify the following parameters:

- **First Parameter**: Mode of data generation (Options: `basic`, `pesel`, `full`)
- **Second Parameter**: Gender selection (Options: `0` for random gender, `1` for 'Male', `2` for 'Female')

To access the API, use the following endpoint examples:

http://localhost:8000/api/basic/1

http://localhost:8000/api/full/2

## Installation

To install the Django project, follow these steps:

1. Clone the project repository from GitHub.
2. Create a new SQLite database: `db.sqlite3`.
3. Apply database migrations:

python manage.py makemigrations

python manage.py migrate

Populate the database with data using the following view (maximum data limit in the current files is 150,000 records):
http://localhost:8000/loading_data/<int:limit>

## Usage

Once the installation is complete, you can access the Personal Data Generator by running the Django development server. You can generate data in various modes and use the API to generate data with specific parameters.

