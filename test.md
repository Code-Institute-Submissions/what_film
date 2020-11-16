<div id="readme" class="Box-body readme blob js-code-block-container p-5 p-xl-6">
    <article class="markdown-body entry-content container-lg" itemprop="text"><h1><a id="user-content-dwarf-match-testing" class="anchor" aria-hidden="true" href="#dwarf-match-testing"></a>Star Wars Quiz Testing</h1>
<p>The build of Star Wars Quiz has been tested through a manual process during each stage and on a wide range of browsers &amp; devices.</p>
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
<li><a href="#modals"><strong>Modal</strong></a></li>
<li><a href="#game-area"><strong>Game Area</strong></a>
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
<p>CSS - All styling was run through the <a href="https://jigsaw.w3.org/css-validator/" rel="nofollow">W3C CSS Validator</a> to ensure it was valid and no errors were made.</p>
</li>
<li>
<p>JavaScript - All my script was run through the <a href="https://jshint.com/" rel="nofollow">JSHint</a> validator to ensure full functionality without errors.</p>
</li>
</ul>
<h2><a id="user-content-testing-against-user-stories" class="anchor" aria-hidden="true" href="#testing-against-user-stories"></a>Testing Against User Stories</h2>
<p>The below goes through of of the user stores listed in the UX section of the <a href="https://github.com/lewejuice/starwars-quiz/blob/master/README.md">README.md</a>.</p>
<p><strong>As a user, I want:</strong></p>
<ol>
<li>
<p>I want the landing page to engage me instantly, as this will encourage me to go on further and actually play the game.</p>
<ul>
<li>The landing page is an introduction to the game which instantly relates the game to star wars with it's star wars crawling text. For users returning to the game there is an optional skip button so they dont have to sit through this every time</li>
<li>The background image on the home page has been animated through the use of JavaScript to give the user the feel of flying through stars which was done to again, build the star wars feel.</li>
<li>The colour scheme used is consistent throughout, and matches the star wars colours.</li>
<li>The use of the lightsaber images programed to appear when the button is hovered on, along with lightsaber sound effects, is a fun interactive take on simply pressing a button.</li>
</ul>
</li>
<li>
<p>Manouvering around the site needs to be made clear and instructive wihtout any confusion.</p>
<ul>
<li>All buttons are clearly marked with either text or an icon.</li>
<li>Once the quiz has started it has a clear, understandable structure, with a timer letting the user know how long they have to answer the question.</li>
</ul>
</li>
<li>
<p>The quiz needs to be accessible and straightforward, with instructions and a mute button if needed.</p>
<ul>
<li>All options and instructions are accessible in clear manor, with a simple to follow structure.</li>
<li>The audio control has been kept as basic as possible, with a speaker icon with either sound or an 'X' for mute, to visually tell the user if the sound is on or off.</li>
</ul>
</li>
<li>
<p>I want to make the game personal to myself, so it gives me a unique experience.</p>
<ul>
<li>This is acomplished through an optional pathway between light and dark(good or evil), which will completely change the audio, images and questions.</li>
<li>It also randomises the questions each time, so users will get different questions each time.</li>
<li>Also depending on the users choices previously and the score they obtain, will asign the user with a star wars character that matches their choices.</li>
</ul>
</li>
<li>
<p>I want to be able to share my score with my friends, and compare.</p>
<ul>
<li>This has been acomplished via a social media sharing API from <a href="https://www.shareaholic.com/">Shareaholic</a>. Their API provides buttons to easily transfer the user to their chosen social platform, with a shared post made up.</li>
</ul>
</li>
<li>
<p>I want to be able to stay updated with my correct and wrong answers during the quiz how long I have to answer a question.</p>
<ul>
<li>Throughout the quiz it has star wars style icons, that represent each question, which turn blue or red depending on the right or wrong answer.</li>
</ul>
</li>
<li>
<p>I want to be able to see how long I have to answer each question.</p>
<ul>
<li>A timer counting down from twenty is also clearly shown, which restarts with each question and when the timer ends, it will render the question wrong and move on.</li>
</ul>
</li>
<li>
<p>I want the questions to be randomised so they are not the same as previous games.</p>
<ul>
<li>Through JavaScript, the quiz has been programed to pick at random, ten questions from fifty on each side(light or dark), to ensure the user doesn't repeat the same questions each time.</li>
</ul>
</li>
</ol>
<h2><a id="user-content-manual-testing" class="anchor" aria-hidden="true" href="#manual-testing"></a>Manual Testing</h2>
<p>I have included the manual testing processes which took place during the development stage to ensure that all aspects of the quiz work as intended.</p>
<h3><a id="user-content-responsive-design-testing" class="anchor" aria-hidden="true" href="#responsive-design-testing"></a>Responsive Design Testing</h3>
<p>During the development and testing phase of the site, I used Google Chrome Dev Tools to test the layout as I built my code and viewed each stage on different screen displays to makesure the quiz worked across multiple platforms.</p>
<p>All testing was performed using:</p>
<ul>
<li>Google Chrome</li>
<li>Explorer</li>
<li>Mozilla Firefox</li>
<li>Safari</li>
<li>Desktop - Two different screen sizes.</li>
<li>Mobile Phones - All inclusive devices provided by Chrome dev tools and on an actual iPhone 11 pro.</li>
<li>Tablets - All inclusive devices provided by Chrome Dev Tools as well as an iPad Air.</li>
</ul>
<h4><a id="user-content-overview" class="anchor" aria-hidden="true" href="#overview"></a>Overview</h4>
<p>Star Wars Quiz was designed and built to be displayed and used on multiple devices such as mobile phones, tablets, desktops.</p>
<p>Throughout the testing I made notes on what elements needed work and altered them accordingly.</p>
<p>The main quiz page was designed using the Bootstrap Framework, which was extremely useful in honing the sites full flexibility. Some elements had to be made to measure, instead of letting the element size changing itself to adapt to a new space.</p>
<h5><a id="user-content-landing-page" class="anchor" aria-hidden="true" href="#landing-page"></a>Landing and Home Page</h5>
<p>The landing page was a tricky obstical, due to it's animated text, I had to makesure the time span wasn't too long for the user, while also making sure the full text displayed, I managed to change the letter and line spacing to achieve the desired outcome.</p>
<ul>
<li>
<p>I tested all text and buttons on the landing and home page so that it remained clearly visible on multiple platforms.</p>
</li>
<li>
<p>Another tool which improved the sites responsiveness to multiple screen sizes was the online CSS <a href="https://autoprefixer.github.io/" rel="nofollow">Autoprefixer</a>.</p>
</ul>
<ul>
<li>
<p>Bug Identified - Lightsaber Button Glitch</p>
<li>The animation used for the 'light' and 'dark' buttons had a problem on screens smaller than desktop, where the light saber would travel out of alignment.</li>
<p>Fix Applied:</p>
<p>In order to correct this issue I had to remove them on smaller screen sizes, while increasing the button size using the CSS <code>@media (min-width:)</code> which although, did make the smalller screen version a little less interactive, but it was more functional and asthetically pleasing.</li>
</ul>
<h5><a id="user-content-modals" class="anchor" aria-hidden="true" href="#modals"></a>Instruction Modal</h5>
<p>I tested the instruction modal on a variety of screen sizes, and found on a mobile phone, it worked better filling the entire screen, instead of just a pop up.</p>
<p>Bug Discovered - A large ammount of blank space at the bottom of the modal on larger screen sizes</p>
<ul>
<li>The ammount of space is obvious to user, as the text was small and hard to read and would need to zoom in to see it.</li>
</ul>
</ul>
<p>Fix Applied:</p>
<ul>
<li>This issue was fixed by creating a custom screen width in dev tools to resemble a large monitor, and adjusting the size with css so the text was easier to read and filled up more space on the screen.</li>
</ul>
</ul>
<h4><a id="user-content-game-area" class="anchor" aria-hidden="true" href="#game-area"></a>Game Area</h4>
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