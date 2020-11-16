// Initial Variables
let INITIAL_SEARCH_VALUE = 'Top Rated Movies';
let log = console.log;

let searchButton = document.querySelector('#searchBtn');;
let searchInput = document.querySelector('#search');
let moviesContainer = document.querySelector('#movies-container');
let moviesSearchable = document.querySelector('#movies-searchable');

// Anchor element for movie posters to take the user to an info page for that movie via the movie id
function createImageContainer(imageUrl, id) {
    let tempDiv = document.createElement('div');
    tempDiv.setAttribute('class', 'imageContainer');
    tempDiv.setAttribute('data-id', id);

    let movieElement = `
        <a href="/movie/${id}" class="img-a"><img src="${imageUrl}" alt="" data-movie-id="${id}">
    `;
    tempDiv.innerHTML = movieElement;

    return tempDiv;
}

// Reset search input after search
function resetInput() {
    searchInput.value = '';
}

// Error message 
function handleGeneralError(error) {
    log('Error: ', error.message);
    alert(error.message || 'Internal Server');
}

// Retrieve categorie title
function createSectionHeader(title) {
    let header = document.createElement('h2');
    header.innerHTML = title;

    return header;
}

// Display posters and category title
function renderMovies(data) {
    let moviesBlock = generateMoviesBlock(data);
    let header = createSectionHeader(this.title);
    moviesBlock.insertBefore(header, moviesBlock.firstChild);
    moviesContainer.appendChild(moviesBlock);
}


// Search movies and display in movie block
function renderSearchMovies(data) {
    if ((window.location.pathname == '/' || window.location.pathname == '/home')) {
        moviesSearchable.innerHTML = '';
        let moviesBlock = generateMoviesBlock(data);
        moviesSearchable.appendChild(moviesBlock);
    }    
}

// Retrieving and displaying movie posters
function generateMoviesBlock(data) {
    let movies = data.results;
    let section = document.createElement('section');
    section.setAttribute('class', 'section');

    for (let i = 0; i < movies.length; i++) {
        let { poster_path, id } = movies[i];

        if (poster_path) {
            let imageUrl = MOVIE_DB_IMAGE_ENDPOINT + poster_path;
    
            let imageContainer = createImageContainer(imageUrl, id);
            section.appendChild(imageContainer);
        }
    }

    let movieSectionAndContent = createMovieContainer(section);
    return movieSectionAndContent;
}



// Inserting section before content element
function createMovieContainer(section) {
    let movieElement = document.createElement('div');
    movieElement.setAttribute('class', 'movie');

    let template = `
        <div class="content">
            <p id="content-close">X</p>
        </div>
    `;

    movieElement.innerHTML = template;
    movieElement.insertBefore(section, movieElement.firstChild);
    return movieElement;
}

// Search button function
$(document).ready(function() {
      if ((window.location.pathname == '/' || window.location.pathname == '/home')) {
            searchButton.onclick = function (event) {
                event.preventDefault();
                let value = searchInput.value

            if (value) {
                searchMovie(value);
            }
                resetInput();
            }
      }
    })      

//Get movie info page rendered, functions from api.js
function renderMovieInfo() {
    searchMovieTitle();
    searchMovieDate();
    searchMovieImg();
    searchMovieRating();
    searchMovieSynapsis();
}

// Initialize the search
$(document).ready(function() {
      if ((window.location.pathname == '/' || window.location.pathname == '/home')) {
            searchMovie(INITIAL_SEARCH_VALUE);
            searchUpcomingMovies();
            getTopRatedMovies();
            searchPopularMovie();
            getTrendingMovies();
    }
})    

// Review modal elements
let reviewBtn = document.getElementById("review-button");
let modal = document.getElementById("review-modal");
let cancelBtn = document.getElementById("cancel-review");
// When the user clicks on the button, open the modal
$(reviewBtn).click(function(){
        $(modal).css("display", "block");
    });

// When the user clicks on <span> (x), close the modal
$(cancelBtn).click(function(){
        $(modal).css("display", "none");
    });

// Open mondal to remove account
let removeAccountBtn = document.getElementById("remove-button");
let accountModal = document.getElementById("remove-modal");
let cancelRemove = document.getElementById("cancel-remove");
// When the user clicks on the button, open the modal
$(removeAccountBtn).click(function(){
        $(accountModal).css("display", "block");
    });

// When the user clicks on <span> (x), close the modal
$(cancelRemove).click(function(){
        $(accountModal).css("display", "none");
    });

// Flash message variables
let closeFlash = document.getElementById("close-flash");
let flashPop = document.getElementById("flash-pop");
// When the user clicks on <span> (x), close the flash
$(closeFlash).click(function(){
        $(flashPop).css("display", "none");
    });