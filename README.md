<h1>What Film?</h1>
<h3>Third Milestone Project: Data Centric Development - Code Institute</h3>
<h4>By Lewis Hamilton</h4>
<hr>
<p><a href="http://what-film.herokuapp.com/" rel="nofollow" target="_blank">What film?</a> Is a datacentric based movie review website.</p>
<br>
<p>I have built this application to engage movie critics and everyday people alike. Designed to be simplistic yet elegant, enabling users to create their own personal account, search for movies to find what their about, what others have said about it and also an official rating and rating given by other users. Very userfriendly, easy to navigate and is fully responsive to the users chosen device.</p>
<br>
<p>The implementation of TMDB API provides a complete collection of all movies, complemented by MongoDB to build collections of user profiles, reviews and ratings, gives a complete fully functioning movie review application.</p>
<p>The application allows people to see honest reviews from everyday people, while also giving users a platform to share their own thoughts and debate with others.</p>
<br>
<p>I have used HTML, CSS, Materialize, jQuery, JavaScript, Jinja, Flask, MongoDB and Python for this project, which will form part of my ongoing portfolio of work.</p>
<img src="images/what-film-mockup.jpg" alt="Desktop Demo" title="Desktop Demo" style="max-width:100%;">
<br>
<h3>Demo</h3>
<p>A live demo can be found here <a href="https://what-film.herokuapp.com/" rel="nofollow" target="_blank">here</a>.</p>
<br>
<h2><a id="user-content-table-of-contents" class="anchor" aria-hidden="true" href="#table-of-contents"></a>Table of Contents</h2>
<ol>
<li>
<p><a href="#ux"><strong>UX</strong></a></p>
<ul>
<li><a href="#user-stories"><strong>User Stories</strong></a></li>
<li><a href="#design-choices"><strong>Design choices</strong></a></li>
<li><a href="#wireframes"><strong>Wireframes</strong></a>
<ul>
<li><a href="#variation-between-wireframes-and-final-product">Variation Between Wireframes and Final Product</a></li>
</ul>
</li>
</ul>
</li>
<li>
<p><a href="#technologies-used"><strong>Technologies Used</strong></a></p>
</li>
<li>
<p><a href="#features"><strong>Features</strong></a></p>
<ul>
<li><a href="#existing-features"><strong>Existing Features</strong></a></li>
<li><a href="#features-to-be-implemented"><strong>Features To Be Implemented</strong></a></li>
</ul>
</li>
<li>
<p><a href="#testing"><strong>Testing</strong></a></p>
<ul>
<li><a href="#code-validation"><strong>Code Validation</strong></a></li>
<li><a href="#manual-testing"><strong>Manual Testing</strong></a></li>
</ul>
</li>
<li>
<p><a href="#deployment"><strong>Deployment</strong></a></p>
<ul>
<li><a href="#to-run-locally"><strong>To Run Locally</strong></a></li>
</ul>
</li>
<li>
<p><a href="#credits"><strong>Credits</strong></a></p>
<ul>
<li><a href="#api"><strong>Music and Sound Effects</strong></a></li>
<li><a href="#images"><strong>Images</strong></a></li>
<li><a href="#code-credits"><strong>Code Credits</strong></a></li>
<li><a href="#learning-resources"><strong>Learning Resources</strong></a></li>
<li><a href="#acknowledgements"><strong>Acknowledgements</strong></a></li>
</ul>
</li>
<li>
<p><a href="#disclaimer"><strong>Disclaimer</strong></a></p>
</li>
</ol>
<h2><a id="user-content-ux" class="anchor" aria-hidden="true" href="#ux"></a><strong>UX</strong></h2>
<h3><a id="user-content-user-stories" class="anchor" aria-hidden="true" href="#user-stories"></a>User stories</h3>
<p>As a user:</p>
<ul>
<li>
<p>I want the landing page to clearly represent what type of application im on, and give me options of engagment instantly, as this will encourage me to go on further and explore the site.</p>
</li>
<li>
<p>Manouvering around the site needs to be made clear and instructive wihtout any confusion.</p>
</li>
<li>
<p>Creating my own account needs to be striaght forward and quick.</p>
</li>
<li>
<p>Finding the movie of my choice needs to be easy to find and navigate too.</p>
</li>
<li>
<p>I want to be able to share my thoughts on the movies I watch and compare with what others think.</p>
</li>
<li>
<p>I want to be able to see new movies coming out soon.</p>
</li>
<li>
<p>I want the application to help me figure out if a movie is worth watching or not.</p>
</li>
<li>
<p>I want to be able to update my personal details or delete them if need be.</p>
</li>
</ul>
<h2><a id="user-content-design-choices" class="anchor" aria-hidden="true" href="#design-choices"></a>Design Choices</h2>
<h3><a id="user-content-colours" class="anchor" aria-hidden="true" href="#colours"></a>Colours</h3>
<ul>
<li>
<p><strong>Navbar</strong> - I decided to use <code>#711324</code>(Dark red) as I feel this colour represents the red curtains at cinemas, which should give the user a movie feel.</p>
</li>
<li>
<p><strong>Buttons and Icons</strong> - I decided to use red and blue which represents confirmation or cancel. Also it stands out against the black and white backgrounds.</p>
</li>
<li>
<p><strong>Font Colour</strong> - I decided to use <code>#FFFFFF</code>(White) &amp; <code>#000000</code>(Black) for the text as it keeps with the simplistic theme, but also stands out against the background colours.</p>
</li>
</ul>
<h3><a id="user-content-fonts" class="anchor" aria-hidden="true" href="#fonts"></a>Fonts</h3>
<ul>
<li>
<p><a href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="nofollow"><strong>Roboto</strong></a> - I used this font throughout the site, as I feel it fit in with the clean design, while also bold enough to stand out for readability.</p>
</li>
</ul>
<h3><a id="user-content-wireframes" class="anchor" aria-hidden="true" href="#wireframes"></a>Wireframes</h3>
<ul>
<li>
<p>The wireframes for the initial layout in the planning stage of the website were created using <a href="https://balsamiq.com/" rel="nofollow">Balsamiq</a>. You can view the wireframes for What Film? <a href="https://github.com/lewejuice/what_film/tree/master/wireframes">here</a>.</p>
</li>
<li>
<p>The wireframes include a design layout for Desktop and Mobile.</p>
</li>
<li>
<p>The colour scheme I had in mind when designing the mockups was not available on the site.</p>
</li>
</ul>
<h4><a id="user-content-variation-between-wireframes-and-final-product" class="anchor" aria-hidden="true" href="#variation-between-wireframes-and-final-product"></a>Variation Between Wireframes and Final Product</h4>
<p>I only made a couple changes from the initial design plan, as certain things I feel didn't work while building the site:</p>
<h5><a id="user-content-landing-page" class="anchor" aria-hidden="true" href="#landing-page"></a>Landing Page</h5>
<ul>
<li>For the homescreen I changed to show multiple catergories with movie posters to engage users instantly, instead of having them navigate to a categorie.</li>
</ul>
<h4><a id="user-content-level-select-modal" class="anchor" aria-hidden="true" href="#level-select-modal"></a>Modal</h4>
<ul>
<li>I did not include the design for my modal as I thought, instead of loading a new page, a modal window pop up is more efficient.</li>
</ul>
<h2><a id="user-content-technologies-used" class="anchor" aria-hidden="true" href="#technologies-used"></a>Technologies Used</h2>
<ol>
<li>
<p><a href="https://en.wikipedia.org/wiki/HTML" rel="nofollow">HTML</a> - This was used for the overall structure of the website.</p>
</li>
<li>
<p><a href="https://en.wikipedia.org/wiki/Cascading_Style_Sheets" rel="nofollow">CSS</a> - This was used for the styling of elements on the website.</p>
</li>
<li>
<p><a href="https://en.wikipedia.org/wiki/JavaScript" rel="nofollow">JavaScript</a> - This was mainly used to retrieve and display data from the API, but also a couple small animations i.e displaying the modals.</p>
</li>
<li>
<p><a href="https://en.wikipedia.org/wiki/JQuery" rel="nofollow">jQuery</a> - This was used in my javascript files to help achieve complex ideas in a simpler way.</p>
</li>
<li>
<p><a href="https://en.wikipedia.org/wiki/Python_(programming_language)" rel="nofollow">Python</a> - This was used for the majority of the backend development of the site, from using CRUD functionality with forms and database collections, to navigating the website through different html templates.</p>
</li>
<li>
<p><a href="https://en.wikipedia.org/wiki/Flask_(web_framework)" rel="nofollow">Flask</a> - This was used to add more sophisticated features in a simpler way, from form validation to it's extremely useful jinja functions in HTML.</p>
</li>
<li>
<p><a href="https://en.wikipedia.org/wiki/MongoDB" rel="nofollow">MongoDB</a> - This NoSQL database program was used to store all the data from user information, to the movie reviews and ratings.</p>
</li>
<li>
<p><a href="https://getbootstrap.com/" rel="nofollow">Materialize Framework</a> - This was used to create a well structured grid layout, forms and icons.</p>
</li>
<li>
<p><a href="https://fonts.google.com/" rel="nofollow">Google Fonts</a> - I used Google Fonts to source the fonts I used on the website.</p>
</li>
<li>
<p><a href="https://www.themoviedb.org/" rel="nofollow">TMDB</a> - This was the API i chose to go with for retrieving all the movie data for my application, that is updated regularly.</p>
</li>
<li>
<p><a href="https://github.com/">GitHub</a> - I used to store my repository for the project and record all my commits.</p>
</li>
<li>
<p><a href="https://www.heroku.com/">Heroku</a> - I used to deploy my website, and store my enviroment variables.</p>
</li>
<li>
<p><a href="https://validator.w3.org/" rel="nofollow">Markup Validation service</a> - I used this to make sure my HTML had no errors or faults.</p>
</li>
<li>
<p><a href="https://autoprefixer.github.io/" rel="nofollow">Autoprefixer</a> - I used this to make sure all CSS prefixes were exact for the best optimization.</p>
</li>
<li>
<p><a href="https://extendsclass.com/python-tester.html" rel="nofollow">Python tester</a> - I used this to make sure all my Python syntax had no faults.</p>
</li>
<li>
<p><a href="https://codebeautify.org/jsvalidate" rel="nofollow">Code Beautify/JavaScript</a> - I used this to make sure all my JavaScript had no faults.</p>
</li>
</ol>
<h2><a id="user-content-features" class="anchor" aria-hidden="true" href="#features"></a>Features</h2>
<h3><a id="user-content-existing-features" class="anchor" aria-hidden="true" href="#existing-features"></a>Existing Features</h3>
<p>Landing Page</p>
<ul>
<li>
<p>The landing page starts with a screen size optimized navbar to help navigate the site, and also displays log in if no user account is logged or log out if vice versa.</p>
</li>
<li>
<p>There is also a search bar to help users find the movie their looking for effieciently, which then displays a collection of possible movie posters matching their search input</p>
</li>
<li>
<p>Also a collection of catergroised movie posters are displayed under certain headings i.e Trending movies. They are elgantly animated and can be scrolled through.</p>
</li>
</ul>
<p>Movie Information page</p>
<ul>
<li>
<p>The Movie information page includes main information about the movie selected i.e Title, release date and synopsis.</p>
</li>
<li>
<p>Also two ratings are displayed. One is an official rating pulled from the API and the other is a rating from the sites users which is an average of all the ratings given.</p>
</li>
<li>
<p>There is also a list of reviews and ratings in table format, displaying the username, review and rating given.</p>
</li>
</ul>
<p>Review Modal</p>
<ul>
<li>
<p>The review modal displays a message telling the user to log in to write a review with a link to the log in screen below.</p>
</li>
<li>
<p>Once logged in, it has a text area input for the review and then a number choosing input between 1-10 for the rating with a submit or cancel button.</p>
</li>
</ul>
<p>Log in page</p>
<ul>
<li>
<p>The log in page is made up of a simple form asking for the users username and password.</p>
</li>
<li>
<p>With the option to log in and submit that information or a register now option which link the user to the registration page.</p>
</li>
</ul>
<p>Registration page</p>
<ul>
<li>
<p>The registration page is made up of a form to create a new user, asking for the users choice of username, password and email.</p>
</li>
<li>
<p>There is a submit button which when clicked will first validate the form checking all the correct information has been provided before then passing it to the backend and stored into the database.</p>
</li>
</ul>
<p>Account page</p>
<ul>
<li>
<p>The account page displays all the users information with input boxes to update or change each detail, apon selecting the submit button the form is then validated to makesure valid information is given.</p>
</li>
<li>
<p>There is also a delele account button which brings up a delete account modal.</p>
</li>
</ul>
<p>Delete account modal</p>
<ul>
<li>
<p>The delete account modal is a simple form asking to confirm the users password.</p>
</li>
<li>
<p>There is then two button options of either delete account or cancel which will close the modal.</p>
</li>
<li>
<p>If delete account is selected and the password provided is correct, the users account details and reviews are then removed from the database.</p>
</li>
</ul>
<h3><a id="user-content-features-to-be-implemented" class="anchor" aria-hidden="true" href="#features-to-be-implemented"></a>Features To Be Implemented</h3>
<ul>
<li>
<p>The next thing I would implement is a feature to remove and maybe edit reviews after the user has submitted them.</p>
</li>
<li>
<p>I also would like to implement a chat option for the users so people can discuss movies with others.</p>
</li>
</ul>
<h2><a id="user-content-testing" class="anchor" aria-hidden="true" href="#testing"></a>Testing</h2>
<h3><a id="user-content-code-validation" class="anchor" aria-hidden="true" href="#code-validation"></a>Code Validation</h3>
<p>All code written has been thoroughly validated and passed through the following online validators:</p>
<ul>
<li>
<p>HTML - All code was run through the <a href="https://validator.w3.org/" rel="nofollow">W3C HTML Validator</a> to ensure it was valid code and no errors were made.</p>
</li>
<li>
<p>CSS - All styling was run through the <a href="https://jigsaw.w3.org/css-validator/" rel="nofollow">W3C CSS Validator</a> to ensure it was valid and no errors were made.</p>
</li>
<li>
<p>JavaScript - All my script was run through the <a href="https://jshint.com/" rel="nofollow">JSHint</a> validator to makesure it was clean and valid.</p>
</li>
<li>
<p>Python - All my script was run through the <a href="https://extendsclass.com/python-tester.html" rel="nofollow">Python tester</a> to make sure all my Python syntax had no faults.</p>
</li>
</ul>
<h3><a id="user-content-manual-testing" class="anchor" aria-hidden="true" href="#manual-testing"></a>Manual Testing</h3>
<p>You can view the testing done in the <a href="https://github.com/lewejuice/what_film/blob/master/test.md">test.md</a> where I have written in-depth on the various tests I have performed.</p>
<h2><a id="user-content-deployment" class="anchor" aria-hidden="true" href="#deployment"></a>Deployment</h2>
<p>I developed this project using <a href="https://www.gitpod.io/" rel="nofollow">Gitpod</a>. Version control was done using git and hosting the repository was done through <a href="https://github.com/lewejuice/what_film">repository in GitHub</a>.</p>
<p>The live site was deployed via <a href="https://www.heroku.com/" rel="nofollow">Heroku</a>. The deployed site will update when pushed from to heroku via gitpod terminal. The Heroku app location can be found <a href="http://what-film.herokuapp.com/">here.</a></p>
<p>To deploy What Film? from <a href="https://www.gitpod.io/" rel="nofollow">Gitpod</a>, I completed the following steps:</p>
<ol>
<li>Database and Tables were created in an Atlas <a href="https://www.mongodb.com/" rel="nofollow">MongoDB</a> account</li>
<li>Project workspace was created in <a href="https://www.gitpod.io/" rel="nofollow">Gitpod</a>. In this workspace: Flask was installed - <code>pip3 install Flask</code>.</li>
<li>Setup app.py file and imported flask and os - <code>from flask import Flask. import os</code></li>
<li>Created an instance of flask - <code>app = flask(__name__)</code></li>
<li>Inside the app run() function set the host, ip and debug=true</li>
<li>Create a new Heroku App - unique name and EU Server</li>
<li>Install <a href="https://www.heroku.com/" rel="nofollow">Heroku</a> through the CLI using <code>CLI: npm install -g heroku</code></li>
<li>In <a href="https://www.gitpod.io/" rel="nofollow">Gitpod</a> login to Heroku through CLI to confirm existance of app. <code>CLI: heroku login -i. CLI: heroku apps</code>.</li>
<li>Create requirements.txt file - <code>CLI: pip3 freeze --local > requirements.txt</code></li>
<li>Create Procfile - <code>echo web: python app.py > Procfile</code></li>
<li>Add and Commit to Git Repository using  <code>CLI: git add .</code> and then <code>CLI: git commit -m "initial commit"</code></li>
<li>Push to Heroku using <code>CLI: git push heroku</code></li>
<li><code>CLI - heroku ps:scale web=1</code> Command to tell Heroku to run the app</li>
<li>Login to Heroku to add config variables including IP, Port, Mongo_DB and Mongo_URI</li>
<li>Get Flask to talk to MongoDB - <code>CLI: pip3 install pymongo</code> and <code>CLI: pip3 install dnspython</code></li>
<li>Add extra libraries to app.py - <code>from flask_pymongo import Pymongo</code></li>
<li>Add DB connection code to app.py which should be stored in enviroment variables.</li>
<li>Set Debug to False</li>
<li>Click Open App in <a href="https://www.heroku.com/" rel="nofollow">Heroku</a></li>
</ol>
<h3><a id="user-content-to-run-locally" class="anchor" aria-hidden="true" href="#to-run-locally"></a>To Run Locally</h3>
<p>If you wanted to run this project locally and not use GitHub Pages, you can follow these steps:</p>
<ol>
<li>
<p>Go to the repository for <a href="https://github.com/lewejuice/starwars-quiz/"><strong>Star Wars Quiz</strong></a>.</p>
</li>
<li>
<p>Below the repository name, you will see a green button with the text <strong>Code</strong>.</p>
</li>
<li>
<p>Click on this button and a box will appear called <strong>Clone with HTTPS</strong>.</p>
</li>
<li>
<p>Copy this clone URL.</p>
</li>
<li>
<p>In your local development program, open <strong>Git Bash</strong>. Makesure <strong>Git</strong> has been installed.</p>
</li>
<li>
<p>Change the directory to where you want the cloned directory to be made.</p>
</li>
<li>
<p>Type <code>git clone</code> and then paste in the URL you took previously, using HTTPS.</p>
<ul>
<li>
<p>Here is an example:</p>
<p><code>git clone https://github.com/lewejuice/what_film.git</code></p>
</li>
</ul>
</li>
<li>
<p>You can cut ties with the original GitHub repository by typing in:</p>
<ul>
<li><code>git remote rm origin</code></li>
</ul>
</li>
</ol>
<h2><a id="user-content-credits" class="anchor" aria-hidden="true" href="#credits"></a>Credits</h2>
<h3><a id="api" class="anchor" aria-hidden="true" href="#api"></a>Images & Data</h3>
<ol>
<li>
<p>An API called <a href="https://www.themoviedb.org/" rel="nofollow">TMDB(The Internet Movie Database)</a> was used to get all the data and images.</p>
</li>
</ol>
<h3><a id="logo" class="anchor" aria-hidden="true" href="#logo"></a>Fonts</h3>
<ol>
<li>
<p>The typeface used for the logo was from a website called <a href="https://www.dafont.com/" rel="nofollow">Dafont</a>.</p>
</li>
<li>
<p>The typeface used throughout was from <a href="https://fonts.google.com/" rel="nofollow">Google Fonts</a>, called Roboto.</p>
</li>
</ol>
<h3><a id="user-content-code-credits" class="anchor" aria-hidden="true" href="#code-credits"></a>Code Credits</h3>
<ol>
<li>
<p><a href="https://www.themoviedb.org/" rel="nofollow">TMDB</a> provided some useful documentation to get the data needed.</p>
</li>
<li>
<p>An extremely useful tool I used was <a href="https://stackoverflow.com/" rel="nofollow">Stack Overflow</a>, for help with many syntax and functions.</p>
</li>
<li>
<p>I used <a href="https://www.youtube.com/" rel="nofollow">Youtube</a>, for useful tutorials if I wanted to implement something new that I didn't understand.</p>
</li>
</ol>
<h3><a id="user-content-acknowledgements" class="anchor" aria-hidden="true" href="#acknowledgements"></a>Acknowledgements</h3>
<p>A special thanks to:</p>
<ul>
<li>My Code Institute Mentor, <a href="https://github.com/precious-ijege">Precious Ijege</a> for his guidance and critical analysis.</li>
</ul>
<h3><a id="user-content-learning-resources" class="anchor" aria-hidden="true" href="#learning-resources"></a>Learning Resources</h3>
<ul>
<li>
<p>I have learnt so much from this project from start to finish, broadening my knowledge on both front and backend development. I found using Python extremely interesting and also combining multiple technologies such as databases and Flask. Here are some resources that helped me along the way:</p>
</li>
<li>
<p><a href="https://codeinstitute.net/" rel="nofollow">Code Institute</a>.</p>
</li>
<li>
<p><a href="https://www.codecademy.com/" rel="nofollow">Codecademy</a>.</p>
</li>
<li>
<p><a href="https://stackoverflow.com/" rel="nofollow">Stack Overflow</a>.</p>
</li>
<li>
<p><a href="https://www.w3schools.com/" rel="nofollow">w3schools</a>.</p>
</li>
<li>
<p><a href="https://www.youtube.com/" rel="nofollow">Youtube</a>.</p>
</li>
</ul>
<h2><a id="user-content-disclaimer" class="anchor" aria-hidden="true" href="#disclaimer"></a>Disclaimer</h2>
<p>This site has been created entirely for <strong>educational purposes</strong> only and has not been intended for anything else.</p>
</article>