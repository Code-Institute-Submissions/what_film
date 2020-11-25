<div id="readme" class="Box-body readme blob js-code-block-container p-5 p-xl-6">
    <article class="markdown-body entry-content container-lg" itemprop="text"><h1><a id="user-content-dwarf-match-testing" class="anchor" aria-hidden="true" href="#dwarf-match-testing"></a>What Film? Testing</h1>
<p>The build of What Film? has been tested through a manual process during each stage and on a wide range of browsers &amp; devices.</p>
<h2><a id="user-content-table-of-contents" class="anchor" aria-hidden="true" href="#table-of-contents"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Table of Contents</h2>
<ol>
<li>
<p><a href="#code-validation"><strong>Code Validation</strong></a></p>
</li>
<li>
<p><a href="#testing-against-user-stories"><strong>Testing Against User Stories</strong></a></p>
</li>
<li>
<p><a href="#auto-testing"><strong>Automated Testing</strong></a></p>
</li>
<li>
<p><a href="#manual-testing"><strong>Manual Testing</strong></a></p>
<ul>
<li>
<p><a href="#responsive-design-testing"><strong>Responsive Design Testing</strong></a></p>
<ul>
<li><a href="#responsivness"><strong>Responsiveness</strong></a></li>
<li><a href="#browser-compatibilty"><strong>Broswer compatibilty</strong></a></li>
<li><a href="#overview"><strong>Overview</strong></a>
<ul>
<li><a href="#landing-page"><strong>Landing Page</strong></a></li>
<li><a href="#modals"><strong>Modals</strong></a></li>
<li><a href="#forms"><strong>Forms</strong></a>
</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li>
<p><a href="#functionality-testing"><strong>Functionality Testing</strong></a></p>
<ul>
<li><a href="#overview"><strong>Modal Testing</strong></a></li>
<li><a href="#python-testing"><strong>Python Testing</strong></a></li>
<li><a href="#game-functionality-testing"><strong>Game Functionality Testing</strong></a></li>
</ul>
</li>
<li>
<p><a href="#additional-testing"><strong>Additional Testing</strong></a></p>
</li>
</ul>
</li>
</ol>
<h2><a id="user-content-code-validation" class="anchor" aria-hidden="true" href="#code-validation"></a>Code Validation</h2>
<p>All code written has been thoroughly validated and passed through the following online validators:</p>
<ul>
<li>
<p>HTML - All code was run through the <a href="https://validator.w3.org/" rel="nofollow">W3C HTML Validator</a> to ensure it was valid code and no errors were made.</p>
</li>
<li>
<p>CSS - All styling was run through the <a href="https://autoprefixer.github.io/" rel="nofollow">Autoprefixer</a> to ensure it was valid and no errors were made.</p>
</li>
<li>
<p>JavaScript - All my script was run through the <a href="https://jshint.com/" rel="nofollow">JSHint</a> & <a href="https://codebeautify.org/jsvalidate" rel="nofollow">Code Beautify/JavaScript</a> validators to ensure full functionality without errors.</p>
</li>
<li>
<p>Python - All my Python code was run through the <a href="http://pep8online.com/" rel="nofollow">Pepe8</a> to ensure my Python code had full functionality without errors.</p>
</li>
</ul>
<h2><a id="user-content-testing-against-user-stories" class="anchor" aria-hidden="true" href="#testing-against-user-stories"></a>Testing Against User Stories</h2>
<p>The below goes through of of the user stores listed in the UX section of the <a href="https://github.com/lewejuice/what_film/blob/master/README.md">README.md</a>.</p>
<p><strong>As a user, I want:</strong></p>
<ol>
<li>
<p>I want the landing page to clearly represent what type of application im on, and give me options of engagment instantly, as this will encourage me to go on further and explore the site.</p>
<ul>
<li>The landing page has a variety of different movie posters that have different headings i.e. Trending movies, Popular movies etc. These movie posters instantly tell the user it is a movie related website.</li>
<li>The dark deep red used for the navbar relates to the cinema curtains to add further to movie theme.</li>
<li>The hover and scroll animations on the movie posters give the site a sleek professional feel to give users confidence in the sites ability.</li>
</ul>
</li>
<li>
<p>I want to be able to sign in and out of my account.</p>
<ul>
<li>A login and logout feature has been added so users can sign in and out with ease via the navbar.</li>
</ul>
</li>
<li>
<p>I want to be able to search for a particular movie.</p>
<ul>
<li>A search bar has been added on the homepage so a user can search for any movie they desire, and can submit their search via an enter key press or clicking the search button.</li>
</ul>
</li>
<li>
<p>Manouvering around the site needs to be made clear and instructive wihtout any confusion.</p>
<ul>
<li>The navbar on both desktop and mobile screens are simple and instructive to navigate efficiently through the site.</li>
<li>All buttons are clearly marked with either text or an icon, as well as colours to represent confirm or cancel.</li>
<li>The scrolling through the different movie collections is simple and clear, but also paired with a user friendly search bar.</li>
</ul>
</li>
<li>
<p>Creating my own account needs to be striaght forward and quick.</p>
<ul>
<li>The log in page can be navigated to easily through the navbar or through attempting to do an activity which requires the user to login</li>
<li>The registration form is made up of only three inputs, and doesn't ask for irrelevent information.</li>
</ul>
</li>
<li>
<p>Finding the movie of my choice needs to be easy to find and navigate too.</p>
<ul>
<li>A search bar has been included so a user can quickly find a specific film, once they have typed out the title they can press the enter button to submit the search or press the search icon.</li>
<li>The search results are displayed in a similar way to the other movie posters to fit in perfectly with the site layout. The results displayed show multiple options that match the title or word they have searched for.</li>
<li>The homepage movie collections are extremely useful if the user doesn't know exactly what their looking for, and might be curious to find a new movie to watch. These are easily navigated and can be smoothly scrolled through.</li>
</ul>
</li>
<li>
<p>I want to be able to share my thoughts on the movies I watch and compare with what others think.</p>
<ul>
<li>This has been acomplished by giving users the ability to review and rate movies and also list others reviews and ratings on each movies information page.</li>
<li>The ratings given for each movie are averaged and displayed on the information page to give a user an efficient idea of what the majority think.</li>
<li>To acomplish these reviews and ratings, a NoSQL database called mongoDB has been used to store them when the user submits them, and they are organised by the movieId.</li>
</ul>
</li>
<li>
<p>I want to be able to see new movies coming out soon.</p>
<ul>
<li>On the homepage, I have included a collection of movies titled Upcoming Movies, which is a collection that TMDB API provides.</li>
</ul>
</li>
<li>
<p>I want the application to help me figure out if a movie is worth watching or not.</p>
<ul>
<li>Not only does the site average out the ratings given by all the users, it also displays an official rating and synopsis for each movie, which it derives from the TMDB API.</li>
</ul>
</li>
<li>
<p>I want to be able to update my personal details or delete them if need be.</p>
<ul>
<li>I have included an account page where the user can view thier information if they are logged into their account, otherwise it will take them to the log in screen.</li>
<li>The account page is also a form where the user can change their username, email, password or all of them. This form upon submit and with the correct password provided, then updates the database with the new information.</li>
<li>It also has a button named "Remove Account", which when pressed brings up a modal where the user can enter their password and click remove account, and then that account and all reviews they have made will be deleted.</li>
</ul>
</li>
</ol>
<h2><a id="auto-testing" class="anchor" aria-hidden="true" href="#auto-testing"></a>Automated Testing</h2>
<p>Using pythons built-in <a href="https://docs.python.org/3/library/unittest.html" rel="nofollow">Unit Test Framework</a>, automated tests were carried out on routes. A testcase was created by subclassing unittest.TestCase.</p>
<p>To test the app routes, the test runs each app route to makesure there are no page loading errors.
<p>Automated tests were setup and confirmed that all routes behaved correctly i.e 200 - route ok.</p>
<p>To run the test just simply type in the CLI - <code>python3 test_whatfilm.py</code></p>
<h2><a id="user-content-manual-testing" class="anchor" aria-hidden="true" href="#manual-testing"></a>Manual Testing</h2>
<p>I have included the manual testing processes which took place during the development stage to ensure that all aspects of the site work as intended.</p>
<h3><a id="user-content-responsive-design-testing" class="anchor" aria-hidden="true" href="#responsive-design-testing"></a>Responsive Design Testing</h3>
<p>During the development and testing phase of the site, I used Google Chrome Dev Tools to test the layout as I built my code and viewed each stage on different screen displays to makesure the site is optimized for multiple platforms.</p>
<h4><a id="responsivness" class="anchor" aria-hidden="true" href="#responsivness"></a>Responsiveness</h4>
<p>I tested the application over multiple devices to ensure a greater audience of users. There are many different devices on the market, so I wanted to makesure all users could easily navigate and use all the features of the application.</p>
<p>The main things I tested for was the overall layout of the pages, so they worked well on different screen sizes. I also wanted to makesure the forms were easily readable and useable, as they were an important feature in the applicaton and also all the text on the site needed to be readable on all devices.</p>
<ul>
<li>Desktop screen sizes 1400 x 700  and 1280 x 800- I tested these sizes to makesure the site adapted to smaller and larger monitors, no issues were found.</li>
<li>
<p>Mobile devices:</p>
<ul>
<li>Moto g4 - No issues found.</li>
<li>Galaxy S5 - No issues found.</li>
<li>Pixel 2 - No issues found.</li>
<li>All iphone sizes - Only issues on iphone x and above had some sizing issues with allot of empty space, but css styling was used to prevent it.</li>
</ul>
</li>
<li>
<p>Tablet devices tested were:</p>
<ul>
<li>Ipad - No issues found.</li>
<li>Ipad Pro - The logo in the navbar was far too small and also the layout was styled like a desktop on movie information page, so a media query was put in place to fix these issues.</li>
<li>Surface Duo - No issues found.</li>
<li>Galaxy Fold - No issues found.</li>
</ul>
</li>
</ul>
<p>The physical devices tested on were a Macbook Air ,Samsung S20, iPhone 12 pro, and an iPad Air.</p>
<h4><a id="browser-compatibilty" class="anchor" aria-hidden="true" href="#browser-compatibilty"></a>Broswer compatibilty</h4>
<p>I tested the application over multiple browsers to makesure all fonts, images, and features worked on a variety of browsers.</p>
<p>Testing was carried out on the following browsers:</p>
<ul>
<li>Google Chrome - No issues were found.</li>
<li>Mozilla Firefox - No issues were found.</li>
<li>Safari - No issues were found.</li>
</ul>
<h4><a id="user-content-overview" class="anchor" aria-hidden="true" href="#overview"></a>Overview</h4>
<p>What Film? was designed and built to be displayed and used on multiple devices such as mobile phones, tablets, desktops.</p>
<p>Throughout the testing I made notes on what elements needed work and altered them accordingly.</p>
<p>The site used the Materialize Framework, which was extremely useful in honing the sites full flexibility and creating a tidy grid layout. With further styling to complement, enabled elements to adapt to different screen sizes.</p>
<h5><a id="user-content-landing-page" class="anchor" aria-hidden="true" href="#landing-page"></a>Landing and Home Page</h5>
<ul>
<li>
<p>The landing page was quite straightforward as materialize adapted the navbar for multiple screen sizes and then movie poster collections displayed and worked well on all screen sizes.</p>
</li>
<li>
<p>I tested all text and buttons on the landing page so that it remained clearly visible on multiple platforms.</p>
</li>
</ul>
<ul>
<li>
<p>Bug Identified - Navbar on Ipad pro</p>
<li>Materialize did not recognise ipad pro as a mobile styled screen layout, so it was still displayed as a desktop</li>
<p>Fix Applied:</p>
<p>In order to correct this issue I had to personalize the navbar styling with CSS <code>@media (min-width:max-width)</code> which makes the site on ipad pro more functional and asthetically pleasing.</li>
</ul>
<h5><a id="user-content-modals" class="anchor" aria-hidden="true" href="#modals"></a>Modals</h5>
<p>I tested the instruction modal on a variety of screen sizes, and found on a mobile phone, the modals were far too small to read and the buttons were too small to press.</p>
<p>Bug Discovered - Modals on small screens</p>
<ul>
<li>Modals were too small and unusable on mobile screens.</li>
</ul>
<p>Fix Applied:</p>
<ul>
<li>Using the media rule, I enlarged the size of the modal and it's contents.</li>
</ul>
</ul>
<h4><a id="forms" class="anchor" aria-hidden="true" href="#forms"></a>Forms</h4>
<p>The forms used throughout the application are a key source of getting data from the user, so they needed to be tested vigorously to ensure they collect valid data but also provide a user friendly experience across all platforms</p>
<br>
<p><strong>Form Validation</strong></p>
<ul>
<li>
<p>I tested the form validation to ensure valid data was being passed to the server.</p>
</li>
<li>
<p>Bug Discovered - Invalid form inputs</p>
<ul>
<li>I noticed that even though I was checking on the backend for the forms data lengths to makesure data was there, the user could simply type in special characters or spaces to fill inputs.</li>
</ul>
<p>Fix Applied:</p>
<ul>
<li>I needed the data to be validated on the frontend, before being sent to the server, so I used <code>required pattern=""</code> on the inputs which disabled the user from submitting invalid data to the server.</li>
</ul>
</li>
</ul>
</li>
<p><strong>Screen size adaptability</strong></p>
<ul>
<li>
<p>The forms need to be easily read and understood on all devices.</p>
</li>
<li>
<p>Bug Discovered - Unusable on mobile devices</p>
<ul>
<li>On smaller devices the text inputs were too small to read and the submit buttons were too small to press.</li>
</ul>
<p>Fix Applied:</p>
<ul>
<li>To fix the input font-sizes, I used a combination of media queries <code>label[class=""]</code>, which enabled me to target the input font-size in all the forms accross the application.</li>
</ul>
</li>
</ul>
</li>
</ol>
</li>
</ol>
<h4><a id="python-testing" class="anchor" aria-hidden="true" href="#python-testing"></a>Python Testing</h4>
<p>Thorough testing was carried out on all python functions to ensure the functionality of the application.</p>
<ol>
<li>
<p><strong>Home Function</strong></p>
<ul>
<li>
<p>The home function was tested to ensure the site took the user to the homepage first, which was straightforward.</p>
</li>
<li>
<p>I did not like showing a login and logout button on the same page, so to fix this, in the home function I added <code>if 'username' in session: user = 'username'</code> to check if a user was logged in.</p>
</li>
<li>
<p>To further add to this, in my index.html file I added a jinja function to read if a user was logged in to display only the logout button or if not the login button.</p>
</li>
<li>
<p>No bugs were found.</p>
</li>
</ul>
</li>
<li>
<p><strong>Login Function</strong></p>
<ul>
<li>
<p>The login function was tested to makesure it linked the input data to data stored in the database.</p>
</li>
<li>
<p>No bugs were found.</p>
</li>
</ul>
</li>
<li>
<p><strong>Logout Function</strong></p>
<ul>
<li>
<p>To makesure users were logged out correctly, I tried to post reviews and look at account information after the logout function was invoked, all worked as it should.</p>
</li>
<li>
<p>No bugs were found.</p>
</li>
</ul>
</li>
<li>
<p><strong>Update Account Function</strong></p>
<ul>
<li>
<p>This was one the most challenging functions to build and test. I tested it by inputing new data to update all information and then just updating one singular piece of data</p>
</li>
<li>
<p>Bug Discovered - Updates all information even when left blank:</p>
<ul>
<li>
<p>When wanting to update only one peice of information, the function was still updating the other pieces of information, so was changing the data to blank in the database.</p>
</li>
</ul>
</li>
<li>
<p>Fix Applied:</p>
<ul>
<li>
<p>To fix this issue I had to implement a way that it only updated the information that the user wanted by checking what data was input into the form and then having the other information stay exactly how it was.</p>
</li>
</ul>
</li>
</ul>
</li>
<li>
<p><strong>Delete Account function</strong></p>
<ul>
<li>
<p>To makesure users could remove their personal details and account from the site correctly, I tested this function by creating new accounts and then deleting them, and checking the database to see if it correctly removed that user.</p>
</li>
<li>
<p>I also wanted to clear the reviews that user had made, so I left reviews with that user and then deleted them, and checked if they were cleared from the database.</p>
</li>
<li>
<p>No bugs were found.</p>
</li>
</ul>
</li>
<li>
<p><strong>Register function</strong></p>
<ul>
<li>
<p>To test the function I created a range of accounts and then checked if the details were being passed and stored correctly and safely.</p>
</li>
<li>
<p>Bug Discovered - Passwords visable in mongoDB:</p>
<ul>
<li>
<p>When looking at the database I could see the passwords of all the users stored, which I dont think is very safe.</p>
</li>
</ul>
</li>
<li>
<p>Fix Applied:</p>
<ul>
<li>
<p>To fix this issue I imported bcrypt to store the passwords in an unreadable secret script.</p>
</li>
</ul>
</li>
</ul>
</li>
<li>
<p><strong>Movie page function</strong></p>
<ul>
<li>
<p>To test this function I first printed each statement to makesure the right movie Id was being recieved. I then searched multiple movies to check the pages were displaying the correct information, reviews and ratings.</p>
</li>
<li>
<p>Bug Discovered - Section empty when no reviews or rating:</p>
<ul>
<li>
<p>When there are no reviews or rating for the movie in the database, the reviews section would just be an empty table and the rating would be empty also.</p>
</li>
</ul>
</li>
<li>
<p>Fix Applied:</p>
<ul>
<li>
<p>In the function I added a way of counting the ammount of ratings for that movie, and if none, the rating is "No rating".</p>
</li>
<li>
<p>To fix the reviews, I found the easiest way was to incorperate a Jijna function in the html to check the length of the review and if none were found, it displays "No reviews" instead of a table.</p>
</li>
</ul>
</li>
</ul>
</li>
<li>
<p><strong>Review function</strong></p>
<ul>
<li>
<p>To test the review function, I tried various inputs of reviews and ratings, and checked the database to see if they were being stored correctly.</p>
</li>
<li>
<p>No bugs were found.</p>
</li>
</ul>
</li>
</ol>
<h3><a id="user-content-additional-testing" class="anchor" aria-hidden="true" href="#additional-testing"></a>Additional Testing</h3>
<p>I asked my friends and family to try the quiz out, and ask for their feedback on how it functioned on their personal device and how they found the game in general.</p>
</article>
</div>