# tsoha-quizzer

tsoha-quizzer is an application that allows users to partake in weekly quizzes. A single quiz consists of 1 to n question/answer pairs. A player can't partake in a given quiz more than once. The score of a player is saved, and under every quiz the top 10 scorers are shown. A top 25 all-time scorers page allows the users to view the all-time ranking.

The application has two types of users – players and admins.

## Test the application

https://tsoha-quizzer.herokuapp.com/

## What is working

- User login
- User logout
- User registration
- Viewing and creation of quizzes and questions

## What is missing

- Refactor code into more easily maintainable packages.
- Does not differentiate between regular users (players) and admin's. Anyone registering is essentially an admin with the priviliges to create new quizzes.
- Answering quizzes is not yet implemented.
- Scoring is not yet implemented.
    - Top scores for quizzes, and for users is thus currently not yet implemented.
- Messaging system is not implemented.
- Bootstrap/Material UI etc.

___

## Players
- Login.
- Logout.
- Register.
- Partake in a quiz by viewing the questions and answering.
- Comment on the quiz, and read other users comments.
- View the top 10 scorers for the quiz.
- View the all-time top 25 scorers (all available quizzes accounted for, total points).

## Admins
- Login.
- Logout.
- Create and publish quizzes.
- Edit and/or delete comments made by users.

## Pages / Views
- Login page.
- Main page lists available quizzes.
- Quiz page lists the quizzes questions and a form for providing answers.
- Once a player has participated in a quiz, the quiz page shows the top 10 scorers for the quiz.
- A separate all-time ranking page is also available, which shows the top-25 players all-time.
- For the admins there should exist a page that allows for the creation of new quizzes.
- Logout should be possible from every page.
