# My Workout App

## Resources

Jira Board: https://mhutt.atlassian.net/jira/software/projects/DP/boards/3

App: 

Presentation:

## The brief:

• Create a monolithic Flask application that serves both the frontend and backend of the application.

• The frontend aspect of the app will use HTML templates to serve the web pages that allow the user to perform CRUD functionality with information from the database.

• The backend aspect of the application will use SQLAlchemy to model and integrate with the database.

### An explanation of My Workout App and how it fulfils the brief:

My workout app is an app that allows users to create an account and then log in. On their account page, they can view and change their details, and delete their account. Once logged in they can see all exercises in the database, with the option to update or delete each exercise in the form of a button. Users can also add their own exercises. Users can then create a workout plan name and add exercises from the exercise database to their workout plan. They can view each workout plan they create by selecting its name and for each exercise in that workout plan they have the option to delete that exercise from that workout plan. Workout plans are specific to the logged in user, so users cannot see other users' workout plans.

### A technical explanation of my app:

My Workout App is a monolithic Flask application factory serving both the frontend and backend of the application. It uses HTML templates to serve web pages with forms that allow the user to create an account (satisfies 'Create'), log in to that account with their email address and password (satisfies 'Read'), change their account details (including password, username and email address - satisfies 'Update'), and delete their account (satisfies 'Delete') by clicking buttons that call functions which query the attached mysql database and then perform said CRUD functions. Passwords are stored as hashes (SHA256) and passwords entered at the login page are hashed and then compared to hashes stored in the database for that user.

Once logged in, a user can create exercises by setting a name, number of repetitions, and number of sets (satisfies 'Create'). A separate template allows users to view, update and delete for each exercise by clicking buttons under each exercise (satisfies 'Read', 'Update', and 'Delete'). All exercises in the database are visible regardless of current user ID.

They can also create a workout plan and then add any of those exercises to their workout by selecting them from a dynamically populated drop down list and then clicking submit. They can then select the workout plan they wish to view by navigating to the view workout hyperlink and selecting the workout name from another dynamically populated list (this queries the users table using the current user ID to ensure that only workouts created by that user can be viewed and then cross references that user ID with the foreign key user ID in the workout plans table). They are then redirected to a page showing all exercises contained in that workout plan.

As an addendum, when users delete their accounts, the database is queried so that every workout plan associated to that user is also deleted. This shows that CRUD is performed on multiple tables simultaneously to achieve the outcome of deleting the user.

Users can log out at any time by clicking the log out hyperlink, which will log the user out of the login manager and they will then be returned to the log in page.

## Architecture:
I initially thought that only three tables would be required to fulfil the brief, with a many-to-many relationship between users and exercises achieved through a workout programs join table:

Initial entity relationship diagram:

![Initial ERD](ERD.drawio.png)

However, during coding, I realised that an association table would be needed between exercises and workout plans as it is in fact a many-to-many relationship between workout plans and exercises. To expand, each workout plan can have many exercises, but each exercise can also be present in multiple workout plans. Thus, this explains the need for an association table. Similarly, I realised when creating the workout plan user stories that I would need to have a table specifically to manage workout plan names so that each workout plan could be viewed individually and contain only those exercises which related to that workout plan by name as queried from the foreign key workout name. There is also a one-to-many relationship between users and workout_plans, as each user can have many workout plans but each workout plan can only be attached to the current user.

Final entity relationship diagram:

![Final ERD](UpdatedERD.drawio.png)

## Project Tracking with the Agile Scrum method using Jira:

Link to jira board: https://mhutt.atlassian.net/jira/software/projects/DP/boards/3

User stories with MoSCoW Prioritisation

Must have:

•	As a user, I want to be able to create an account (2 story points)

•	As a user, I want to be able to view my account details (2 story points)

•	As a user, I want to be able to delete my account (2 story points)

•	As a user, I want to be able to create an exercise (2 story points)

•	As a user, I want to be able to view exercises (3 story points)

•	As a user, I want to be able to update an exercise (5 story points)

•	As a user, I want to be able to delete an exercise (5 story points)

•	As a user, I want to be able to create a workout plan (2 story points)

•	As a user, I want to be able to add an exercise to a workout plan (3 story points)

•	As a user, I want to be able to view my workout plan that I've created (8 story points)


Should have:

•	As a user, I want to be able to log in to my account (8 story points)

•	As a user, I want to be able to update my account information (5 story points)

•	As a user, I want my passwords to be stored safely as hashes (3 story points)

•	As a user, I want to be able to remove an exercise from a workout plan (5 story points)


Could have:

•	As a user, I want my passwords to be stored as salted hashes (3 story points)


Won’t have:

•	As a user, I want to be able to add pictures of exercises for reference (13 story points)

•	As a user, I want to be able to reset my password via email if I’ve forgotten it (20 story points)

## A technical description of how the pipeline works.

## A report on the success and code coverage of my unit tests.

## Future Improvements
