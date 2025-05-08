## CHANGES

- We have changed the architecture of our code in order to integrate the usuage of streamlit UI. 
- We have updated our functions for death rate and Rt, to reflect the reflect the new structure and added the visualistions.

## Pylint
Changes found under formatter.md

## Principles of abstraction and decomposition 
From the beginning of the project we have aimed to design our code with abstraction and decomposition in mind. 
Abstraction is achieved by breifly outlining what each function does, so that even a naive user is able to understabd without much effort. 
Additionally, by using streamlit UI, the user is able to simply run the app without having to look into the source code. 
Decomposition is achieved by modulating our code. Each statistic calculation, data processing, and plotting have their own functions.
