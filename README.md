# Project Title : SportsRelated

#### Video Demo:  https://youtu.be/DKhrCNEC144

#### Description:

SportsRelated is a web application made with microframework Flask that allows users to write blogs related to anything and everything about Sports! It allows users to Register as a new account, Sign In, and start blogging about their passion for Sports. Users have the ability to view blogposts written by fellow sports enthusiasts, as well as update or delete their posts whenever needed. Users can also change their account details if they ever feel like doing so.
The main objective behind creating a sports blogging website is so that users can bring their ardent opinions and passionate views to the virtual world and share it with other fanatics. SportsRelated allows users to voice their opinions and socialise with other users sharing a similar view. It is a great way to build a person's network while writing something they are zealous about.


Technologies used:

- Flask
- Python
- HTML
- CSS
- Javascript
- SQLite
- Bootstrap
- Flask Modules and Libraries

Application.py - The application.py file is the controller of the Flask framework that controls the entire functionality and operation of the Web Application. In this file, all the packages, libraries, and modules required for the web application are imported. Furthermore, certain configurations too are made to enable the application, to ensure templates are auto-reloaded, to ensure responses aren't cached, and to most importantly enable sessions on the application, so that each user can have their independent accounts and make changes to their account without it affecting the Web Application for other users. A configuration to use SQLite database is also written in this file so that queries can be made to the back-end database from the controller to write some functionality in our code. Each route is declared in this file along with the route definition i.e the purpose of every route. Most routes in this application take both 'GET' and 'POST' request methods which allows a user to send data through a route too rather than just getting the template associated with that route.

Database - The SQLite database is the Model of the Flask framework that stores all the account details of every user registered on the application. The database has tables for storing the login details, the blog details and also the account information of a particular user. The database uses Foreign keys to link posts and account details of a particular user to their user id with which they are logged in. The username field is unique in the database which enables that no two users have the same username. The database file for this web application is 'sportsrelated.db'.

The Routes present in the Web Application Include:

Register Route -

The register route renders the 'register.html' file that consists of form fields related to the registration process of the user. Certain validations are needed to be met while registering for a new account and failure in meeting the requirements or submitting empty fields results in an error message that informs the user about the particular requirement not met.
Form validations are an absolute necessity as they prevent abuse from malicious users on the web. Improper validations might result in security vulnerabilities and expose our applications to injection attacks and cross-site scriptings. Therefore this web application has placed validations on every user input field to ensure complete security from malicious users and also to provide a much more user-friendly interface which informs users about the exact issue if and when they fail to meet a requirement.

Login Route -

The Login Route prompts the user to enter their valid credentials by rendering 'login.html' file which after verifying with the database logs them in to the web application.
Here too, user input is checked for invalid credentials or empty fields and an error message is displayed if Log In details are incorrect. The project directory also consists of a file called 'helpers.py' in which a function, login_required(), is written which acts as a route decorater in the Controller, 'application.py', that ensures that a user is automatically redirected to the login route first when they visit the web application or when a they try to manually visit another route by changing the url without logging in first.

Home Route -

The Homepage Route or the home route consists of a carousel of sports images followed by the Blog feed where users can read blogs posted by themselves or other users.
The blogs posted include the title of the blog, the Author's name, and the date and time at which the blog was posted or last updated along with the blog content.
The blog structure is made by using the <article> tag in html which gives it a formal and neat look.
SportsRelated's Homepage also consists of a sidebar with several links i.e Basic Usage, Announcements, Calendars and Socials that keeps the users notified of the changes or updates made to the web application along with their socials if any user feels the need to interact with them on different social media platforms. Files related to the Home Route are : 'index.html', 'usage.html', 'announcements.html', 'calender.html' and 'socials.html'.

About Route -

The About Route explains to the user the significance of creating this web application, the advantages it offers to the users, the requirements needed to start blogging and certain disclaimers the users need to keep in mind while using SportsRelated.
The 'about.html' file renders all the information regarding the about route. The about page is a must have on almost all websites today as it enlightens the users about the people behind the website, the purpose and values of the website, and what users can expect to find while using the web application.
It is a great way of building trust among the audience as it offers clarity and transparency to the users who then can feel comfortable while writing blogs that are personal on the web application.

New Post Route -

The New Post Route allows users to write a blogpost and post it to the feed on the homepage. It is rendered by the 'newpost.html' file and consists of three user input fields namely Title, Author, and Content which prompt the user for the Title of the Blog Post, the name of the Author, and the Blog Content respectively. All three fields are of type TEXT in the SQLite database and cannot contain a null value. There are no word limitations in the Content field which enables users to write more and express their thoughts even better. The Upload button at the end of the form successfully uploads the Blog to the Blog Feed where the blog appears at the top of the feed as it was posted most recently.

My Blogs Route -

The My Blogs route enables users to keep track of all the blogs they have written by rendering the 'myblogs.html' file and also allows users to update or delete a blog if and when required. If a user decides to update a certain post, clicking on the update button takes them to 'update.html' where the blog details are already rendered in the title, author, and content fields. Users can then make changes to any of the fields and all those changes when updated will be reflected on the blog feed. If a user wants to delete a post, clicking on the delete button would result in the blog being erased from the feed. The blog will no longer be found on the My Blogs Route as well.

Account Route -

The account route displays the account information of the current user by rendering 'account.html' which gets the user's username from the database. It also has a couple of more fields for the user to fill which asks the user about their favorite sport and a short description about themselves. These fields are empty when a user logs in to their account. Once a user has filled these fields and saved changes, the account route renders the saved changes too along with the username. Users can change any of the fields in the account whenever they feel like doing so.

Log Out Route -

The Log Out route enables a user to successfully Log Out of the Web Application. To make sure that the user is not Logged in automatically the next time they visit the application, the Log Out route forgets the user by clearing the session related to that user.

Possible Improvements

Every Application has scope for improvement and SportsRelated is no different. The Possible Improvements that can me made to this web application to make it even more interactive and user-friendly are:

- Allowing users to add Profile Pictures to their accounts.
- Sending users an email authentication if they ever forget their password.
- Making use of more Flask libraries to make the interface easier to use and more secure.

Launching the Application

The steps required to launch the Web application are:

- Installing the latest version of Flask
- Installing all the packages mentioned in 'requirements.txt'
- Making sure that all files are present in the folders they are required to be in by flask convention.
- Running command 'flask run' in the terminal to launch the server and the url to the application where it is served.
