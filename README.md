##### DATA MODEL - DESIGN DECISIONS

creating a basic diagram representing the atomic relation between various entities we get this:


There can be N number of ***Insurers*** and each ***Insurers*** can provide policies for M ***Risk Types***.
also A single ***Risk Type*** can be common to multiple ***Insurers***, This is a ***Many-To-Many*** 
Relation between ***Risk*** and ***Insurer***

| InsurerID | InsurerName |
|-----------|-------------|
| I1         | Honda       |
| I2         | Bajaj       |
| I3         | Mahindra    |

| RiskID | RiskType |
|-----------|-------------|
| R1         | Car       |
| R2         | House       |
| R3         | Prize    |

A JUNCTION TABLE TO REPRESENT M-T-M relationship between ***Risk Type*** & ***Insurer***

| RiskID | InsurerID|
|-----------|-------------|
| I1        | R1       |
| I1        | R2       |
| I2        | R1    |


