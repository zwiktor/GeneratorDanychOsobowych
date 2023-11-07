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
