## Table of Contents
  - [Erd For Data Models](#erd)
    - [Data Model Design explanation](#erdexplanation)
  - [Backend - falcon (python) ](#backend)
    - [Configuration & running locally](#backendrunlocal)
    - [Backend Test Suite (pyresttest)](#backendtestsuite)
  - [Frontend - Vuejs (Typescript) ](#frontend)
    - [running locally](#runlocalfrontend)

## erd



![alt text](/data/erd.png)


There can be N number of ***Insurers*** and each ***Insurers*** can provide policies for M ***Risk Types***.
also A single ***Risk Type*** can be common to multiple ***Insurers***, This is a ***Many-To-Many*** 
Relation between ***Risk*** and ***Insurer***

           (INSURER)        
| insurer_id | insurer_name |
|------------+--------------|
|          1 | Honda        |
|          2 | Bajaj        |

         (RISK)

| risk_id | risk_type  |
|---------|------------|
|       1 | House      |
|       2 | Automobile |
|       3 | Prize      |


`(A JUNCTION TABLE TO REPRESENT M-T-M relationship between ***Risk Type*** & ***Insurer***)`

| insurer_id | risk_id |
------------|---------|
|          1 |       1 |
|          2 |       1 |
|          1 |       2 |



Now Every Instance of ***Risk Type*** can have multiple instances of a ***Form*** ( collection of field that is associted with a risk type)

Ex - For a ***Risk Type*** `House` , `Honda` might need a particular set of fields( data to be collected from insurance bearer) whereas `Bajaj` Can have a completely different set of fields for the same ***Risk Type***. so we capture this relation as


| form_id | insurer_id | risk_id |
|---------|------------|---------|
|       1 |          1 |       1 |
|       2 |          1 |       2 |
|       3 |          2 |       1 |


A Form has many instances of field also We want to allow only ceratin types of fields( like `TEXT`, `NUMBER`, `DATE`, `ENUM` to present in form so we create  a Table representing form fields mapping & their types (if we ever need to extend the field type we want to accept, it can easily be defined in the orm schema), also some fields may be mandatory to fill while others might not be mandatory so we have a column to indicate that.  
   
           ( FORM_FIELD )
| field_id | form_id | field_type | field_label   | mandatory |
|----------|---------|------------|---------------|-----------|
|        1 |       1 | TEXT       | Name          |         1 |
|        1 |       2 | TEXT       | Name          |         1 |
|        2 |       1 | TEXT       | Country       |         1 |
|        2 |       2 | TEXT       | Country       |         1 |
|        3 |       1 | NUMBER     | Age           |         1 |
|        3 |       2 | NUMBER     | Age           |         1 |
|        4 |       1 | DATE       | Date Of Birth |         1 |
|        4 |       2 | DATE       | Date Of Birth |         1 |
|        5 |       2 | NUMBER     | PHONE NUMBER  |         1 |


Every Field has a `field value` along with that we would want to know which user(risk bearer, provided the field value & with which risk was this field value associated) so we create a table to reflect this relationship.

              (FormFieldValue)
| field_id | user_id | form_id | field_value |
|----------|---------|---------|-------------|
|        1 |       1 |       1 | Guido       |
|        2 |       1 |       1 | Alaska      |
|        3 |       1 |       1 | 38          |
|        4 |       1 |       1 | 2017-01-01  |

Now for every risk Bearer we would want to know the every instances of form(which can be multiple beacuse a user can apply to many risk defined by one or more insurer ) that he/she has filled/applied.so we have this table

| user_id | form_id |
|---------|---------|
|       1 |       1 |
|       2 |       1 |
|       1 |       2 |


## erdexplanation
## backend
## backendtestsuite
## frontend
