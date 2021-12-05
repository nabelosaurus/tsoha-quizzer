# tsoha-quizzer

tsoha-quizzer is an application that allows users to partake in weekly quizzes. A single quiz consists of 1 to n question/answer pairs. A player can't partake in a given quiz more than once. The score of a player is saved, and under every quiz the top 10 scorers are shown. A top 25 all-time scorers page allows the users to view the all-time ranking.

The application has two types of users – players and admins.

## Test the application

<https://tsoha-quizzer.herokuapp.com/>

Login can be tested with the following credentials, or a new user can be created by registering.

    Username: adminadmin
    Password: adminadmin

## Updates since last deadline

- Refactored code to use SQL statements instead of using SQLAlchemy:s ORM.
- Added Bootstrap for a more pleasing look and feel.
- Taking part in quizzes by answering questions implemented.
- Scoring system implemented.
- Improved error messaging.
- Now uses flask-wtforms for input validation and CSRF prevention (still not implemented on forms of non-fixed length)

## What is working

- User login
- User logout
- User registration
- Viewing and creation of quizzes and questions
- Answering quizzes/questions
- Scoring / Top score working

## What is missing

- Does not differentiate between regular users (players) and admin's. Anyone registering is essentially an admin with the priviliges to create new quizzes.
- Messaging system is not implemented.
- Robust error handling.
- High scores for logged in user, and top high score for specific quizzes.
- Currently a user can take part in the same quiz multiple times. This should not be possible according to the original specificaitons.
- After a user has answered a quiz, the answers should be displayed when viewing the quiz.
- All forms are still not being validated.

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
