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
<p><a href="#manual-testing"><strong>Manual Testing</strong></a></p>
<ul>
<li>
<p><a href="#responsive-design-testing"><strong>Responsive Design Testing</strong></a></p>
<ul>
<li><a href="#overview"><strong>Overview</strong></a>
<ul>
<li><a href="#landing-page"><strong>Landing Page</strong></a></li>
<li><a href="#modals"><strong>Modals</strong></a></li>
<li><a href="#game-area"><strong>Forms</strong></a>
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
<li><a href="#audio-and-music-testing"><strong>Audio and Music Testing</strong></a></li>
<li><a href="#game-functionality-testing"><strong>Game Functionality Testing</strong></a></li>
<li><a href="#responsivness-and-browser-compatibilty"><strong>Responsiveness and Broswer compatibilty</strong></a></li>
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
<p>Python - All my Python code was run through the <a href="https://extendsclass.com/python-tester.html" rel="nofollow">Python tester</a> to ensure full functionality without errors.</p>
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
<h2><a id="user-content-manual-testing" class="anchor" aria-hidden="true" href="#manual-testing"></a>Manual Testing</h2>
<p>I have included the manual testing processes which took place during the development stage to ensure that all aspects of the site work as intended.</p>
<h3><a id="user-content-responsive-design-testing" class="anchor" aria-hidden="true" href="#responsive-design-testing"></a>Responsive Design Testing</h3>
<p>During the development and testing phase of the site, I used Google Chrome Dev Tools to test the layout as I built my code and viewed each stage on different screen displays to makesure the site is optimized for multiple platforms.</p>
<p>All testing was performed using:</p>
<ul>
<li>Google Chrome</li>
<li>Explorer</li>
<li>Mozilla Firefox</li>
<li>Safari</li>
<li>Desktop - Two different screen sizes.</li>
<li>Mobile Phones - All inclusive devices provided by Chrome dev tools and on an actual iPhone 12 pro.</li>
<li>Tablets - All inclusive devices provided by Chrome Dev Tools as well as an iPad Air.</li>
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
</ul>
<p>Fix Applied:</p>
<ul>
<li>Using the media rule, I enlarged the size of the modal and it's contents.</li>
</ul>
</ul>
<h4><a id="forms" class="anchor" aria-hidden="true" href="#forms"></a>Forms</h4>
<p>The quiz area is the main aspect of the game, so I wanted to thoroughly test it, to makesure, no matter what device it is being dislayed on, or which question is being displayed, I wanted it to look and feel exactly as a user would want.</p>
<br>
<p><strong>Progression Structure</strong></p>
<ul>
<li>
<p>Progressing to the next question when it should was an important aspect of the game, and so I tested this function thoroughly to makesure it did so correctly, but then also knew when the last question came, to progress to the scoreStructure() function.</p>
</li>
<li>
<p>Bug Discovered:</p>
<ul>
<li>No bugs were found</li>
</ul>
</li>
</ul>
</li>
<p><strong>Exit Function</strong></p>
<ul>
<li>
<p>I tested that the exit buttons were all working correctly, by refreshing the game which cleared all current game data.</p>
</li>
<li>
<p>No bugs were discovered with this functionality and it works as intended.</p>
</li>
</ul>
</li>
</ol>
</li>
</ol>
<h4><a id="user-content-audio-and-music-testing" class="anchor" aria-hidden="true" href="#audio-and-music-testing"></a>Audio and Music Testing</h4>
<p>Audio tests were carried out extensively on Desktop, Mobile phone, and tablets. They were also tested on a variety of browsers: Google Chrome, Mozilla Firefox and Safari.</p>
<p>The physical mobile/tablet devices tested on were a Samsung S20, iPhone 11 pro, and an iPad Air and also the devices included in Chrome Dev tools.</p>
<ol>
<li>
<p><strong>Audio &amp; Music</strong></p>
<ol>
<li>
<p><strong>Clicking Sound Effect Function</strong></p>
<ul>
<li>
<p>I firstly tested to wether this function was working correctly, and that it had access to the right audio file, which it did.</p>
</li>
<li>
<p>I then decided to use the same function structure but for different audio files which played when you clicked other elements, like the instruction modal close button.</p>
</li>
<li>
<p>I also tested to makesure the audio file did not play, if the sound icon was set to mute.</p>
</li>
<li>
<p>No bugs were found.</p>
</li>
</ul>
</li>
<li>
<p><strong>Wrong/right Sound Effect Function</strong></p>
<ul>
<li>
<p>I tested to makesure that when selecting the wrong or right answer a different sound would play, which gave another way the user could easily distinguish wether they were successful or not.</p>
</li>
<li>
<p>Bug Discovered:</p>
<ul>
<li>On the last question, when clicking your answer, sound of the answer would overlap the sound given for the score structure. This caused the user not being able to hear either sound which resulted in mixture of noises.</li>
</ul>
</li>
<li>
<p>Fix Applied:</p>
<ul>
<li>Too fix this issue I had to go into my audio.js file and add an if statement <code>if (currentQuestion <= 8)</code> too the right/wongAudio() function, so it would only play if it was on the second to last question or less.</strong></li>
</ul>
</li>
</ul>
</li>
<li>
<p><strong>Quiz Complete Audio Function</strong></p>
<ul>
<li>
<p>I tested to makesure when the quiz was completed, depending on the side the user chose and the score they got, a unique sound would play.</p>
</li>
<li>
<p>I tested that the function does not play if the sound is muted.</p>
</li>
<li>
<p>No bugs were found other than the one earlier mentioned on the wrong/right answer audio function.</p>
</li>
</ul>
</li>
<li>
<p><strong>Lightsaber hover audio function</strong></p>
<ul>
<li>
<p>I tested to see if when the light or dark side buttons are hovered over on larger screen sizes, that the audio plays along with the lightsaber animation.</p>
</li>
<li>
<p>No bugs were found.</p>
</li>
</ul>
</li>
<li>
<p><strong>Quiz background music</strong></p>
<ul>
<li>
<p>I tested to makesure as soon as the quiz starts, the audio is played, and then also once the score structure is displayed, the audio stops.</p>
</li>
<li>
<p>I also wanted to makesure it was muted, when the sound icon is set to mute.</p>
</li>
<li>
<p>No bugs were found.</p>
</li>
</ul>
</li>
</ol>
</li>
</ol>
<h4><a id="user-content-game-functionality-testing" class="anchor" aria-hidden="true" href="#game-functionality-testing"></a>Game Functionality Testing</h4>
<p>Game functionality tests were carried out extensively on Desktop, Mobile phone, and tablets. They were also tested on a variety of browsers: Google Chrome, Mozilla Firefox and Safari.</p>
<p>The physical mobile/tablet devices tested on were a Samsung S20, iPhone 11 pro, and an iPad Air and also the devices included in Chrome Dev tools.</p>
<ol>
<li>
<p><strong>Answer check function</strong></p>
<ul>
<li>
<p>I tested that the <code>checkAnswer()</code> function is called when an answer is selected, assuming that all the requirments for the function call have been met and it then moves on to it's next functions to progress further</p>
</li>
<li>
<p>No bugs were found.</p>
</li>
</ul>
</li>
<li>
<p><strong>Random Question Function</strong></p>
<ul>
<li>
<p>I tested that the random question function was working correctly, by displaying different questions each time the user plays the quiz.</p>
</li>
<li>
<p>No bugs were found</p>
</li>
</ul>
<li>
<p><strong>Counter Structure Function</strong></p>
<ul>
<li>
<p>I tested that the counter structure function worked correctly, by counting down from twenty, and if reaching zero, will score the question wrong and move on.</p>
</li>
<li>
<p>No bugs were found</p>
</li>
</ul>
<li>
<p><strong>Choose side function</strong></p>
<ul>
<li>
<p>I tested this function extensively as it effect almost every function, it's main purpose being that it told the other functions which side was selected on the home-page, so each function could act accordingly.</p>
</li>
<li>
<p>No bugs were found</p>
</li>
</ul>
<li>
<p><strong>Start Quiz function</strong></p>
<ul>
<li>
<p>I tested that the start quiz function to makesure everything is rendered correctly from the click of the start button.</p>
</li>
<li>
<p>No bugs were found.</p>
</li>
</ul>
</li>
</ul>
</li>
</ol>
<h4><a id="responsivness-and-browser-compatibilty" class="anchor" aria-hidden="true" href="#responsivness-and-browser-compatibilty"></a>Responsiveness and Broswer compatibilty</h4>
<p>Tests were carried out on Desktop, Mobile phone, and tablets. They were also tested on a variety of browsers: Google Chrome, Mozilla Firefox and Safari.</p>
<p>The physical mobile/tablet devices tested on were a Samsung S20, iPhone 11 pro, and an iPad Air and also the devices included in Chrome Dev tools.</p>
<ol>
<li>
<p><strong>Page Render</strong></p>
<ul>
<li>
<p>On all broswers and devices, pages all rendered correctly, apart from Ipad pro where there seemed to be allot of empty space on the page.</p>
</li>
<li>
<p>To fix this issue, I changed the CSS styling for that specific screen size to enlarge font-sizes and icon sizes to fill more of the screen.</p>
</li>
</ul>
</li>
<li>
<p><strong>URL's</strong></p>
<ul>
<li>
<p>I tested to makesure all page URL's worked correctly accross all devices and browsers, which they did.</p>
</li>
<li>
<p>No issues were found</p>
</li>
</ul>
<li>
<p><strong>Media Files</strong></p>
<ul>
<li>
<p>All media files rendered correctly on all devices and browsers except I found the question image would go over it's boundary on mobile screens.</p>
<p>Also some larger image files on low signal mobile network, would take an excessive ammount of time to load which caused a large issue for questions that needed the image to answer.</p>
</li>
<li>
<p>To fix the first issue I had to change the image width on smaller screen through CSS. The image load time however was a little more complex as I tried to squash down the image files, where I did loose some quality but still worked well for the sizes and screens I was working with.</p>
</li>
</ul>
</li>
</ul>
</li>
</ol>
<h3><a id="user-content-additional-testing" class="anchor" aria-hidden="true" href="#additional-testing"></a>Additional Testing</h3>
<p>I asked my friends and family to try the quiz out, and ask for their feedback on how it functioned on their personal device and how they found the game in general.</p>
</article>
</div>