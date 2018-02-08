## Table of Contents
  - [GitHub](#erd)
  - [Backend](#backend-falcon)

## erd



![alt text](/data/erd.png)


There can be N number of ***Insurers*** and each ***Insurers*** can provide policies for M ***Risk Types***.
also A single ***Risk Type*** can be common to multiple ***Insurers***, This is a ***Many-To-Many*** 
Relation between ***Risk*** and ***Insurer***

           (INSURER)        
| InsurerID | InsurerName |
|-----------|-------------|
| I1         | Honda      |
| I2         | Bajaj      |
| I3         | Mahindra   |


         (RISK)
| RiskID | RiskType       |
|-----------|-------------|
| R1         | Car        |
| R2         | House      |
| R3         | Prize      |

`(A JUNCTION TABLE TO REPRESENT M-T-M relationship between ***Risk Type*** & ***Insurer***)`

| RiskID (FK) | InsurerID (FK)|
|-----------|-------------|
| I1        | R1          |
| I1        | R2          |
| I2        | R1          |



Now Every Instance of ***Risk Type*** can have multiple instances of a ***Form*** ( collection of field that is associted with a risk type)

Ex - For a ***Risk Type*** `House` , `Honda` might need a particular set of fields( data to be collected from insurance bearer) whereas `Bajaj` Can have a completely different set of fields for the same ***Risk Type***. so we capture this relation as

|InsurerID   | RiskID | FormID   |
|-----------|--------|-----------|
| I1        | R1     |FOMR_1     |
| I1        | R2     |FORM_2     |
| I2        | R1     |FORM_3     |






We want to allow only ceratin types of fields( like `TEXT`, `NUMBER`, `DATE`, `ENUM` to present in FORMS so we create  a Table representing ***Field Types***  
   
           ( FIELD TYPE)
| TypeID (PK)  | TypeName (ENUM)|
|-----------|--------------|
| T1        | TEXT         |
| T2        | NUMBER       |
| T3        | DATE         |
| T4        | ENUM         |

A seperate table for fields types removes ***Deletion anomly*** That could have happened.



Every **Field** is associated

## backend-falcon
io
