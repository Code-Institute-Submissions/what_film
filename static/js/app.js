// Initial Values
let INITIAL_SEARCH_VALUE = 'Top Rated Movies';
let log = console.log;

// Selecting elements from the DOM
let searchButton = document.querySelector('#searchBtn');;
let searchInput = document.querySelector('#search');
let moviesContainer = document.querySelector('#movies-container');
let moviesSearchable = document.querySelector('#movies-searchable');

function createImageContainer(imageUrl, id) {
    let tempDiv = document.createElement('div');
    tempDiv.setAttribute('class', 'imageContainer');
    tempDiv.setAttribute('data-id', id);

    let movieElement = `
        <a href="https://8080-e82a8606-a355-4dd6-a74f-98cfd43f4084.ws-eu01.gitpod.io/movie/${id}" class="img-a"><img src="${imageUrl}" alt="" data-movie-id="${id}">
    `;
    tempDiv.innerHTML = movieElement;

    return tempDiv;
}

function resetInput() {
    searchInput.value = '';
}

function handleGeneralError(error) {
    log('Error: ', error.message);
    alert(error.message || 'Internal Server');
}

/*function createVscreen(video) {
    let videoKey = (video && video.key) || 'No key found!!!';
    let vScreen = document.createElement('vScreen');
    vScreen.src = `http://www.youtube.com/embed/${videoKey}`;
    vScreen.width = 360;
    vScreen.height = 315;
    vScreen.allowFullscreen = true;
    return vScreen;
}

function insertVscreenIntoContent(video, content) {
    let videoContent = document.createElement('div');
    let vScreen = createVscreen(video);

    videoContent.appendChild(vScreen);
    content.appendChild(videoContent);
}


function createVideoTemplate(data) {
    let content = this.content;
    content.innerHTML = '<p id="content-close">X</p>';
    
    let videos = data.results || [];

    if (videos.length === 0) {
        content.innerHTML = `
            <p id="content-close">X</p>
            <p>No Trailer found for this film title of ${data.id}</p>
        `;
        return;
    }

    for (let i = 0; i < 4; i++) {
        let video = videos[i];
        insertVscreenIntoContent(video, content);
    }
}*/

function createSectionHeader(title) {
    let header = document.createElement('h2');
    header.innerHTML = title;

    return header;
}


function renderMovies(data) {
    let moviesBlock = generateMoviesBlock(data);
    let header = createSectionHeader(this.title);
    moviesBlock.insertBefore(header, moviesBlock.firstChild);
    moviesContainer.appendChild(moviesBlock);
}



function renderSearchMovies(data) {
    if ((window.location.pathname == '/' || window.location.pathname == '/home')) {
        moviesSearchable.innerHTML = '';
        let moviesBlock = generateMoviesBlock(data);
        moviesSearchable.appendChild(moviesBlock);
    }    
}

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
/*let imgAnchor = document.getElementsByClassName("img-a");
imgAnchor.onclick = function activateMovieInfo() {
    debugger;
    renderMovieInfo();
}*/

/*testPage = document.getElementById("test-page");
testPage.onload = function onLoad() {
    debugger;
    renderMovieInfo(data)
};*/

/*function renderMovieInfo() {
    debugger;
    filmPoster = `
        <img class="filmPoster" src="${imageUrl}" alt="" data-movie-id="${id}">
    `;
    filmTitle = `<h2 id="film-title">${title}</h2>`;
    plot = `<div class="plot-container"><p class="plot">${overview}</p></p></div>`;
    titleContainer = document.getElementById("title-container");
    imgContainer = document.getElementById("img-container");
    plotContainer = document.getElementById("plot-container");
    hello = document.getElementById("hello");
    titleContainer.innerHTML = filmTitle;
    hello.innerHTML = "<p>Hello</p>";
}*/

//Get movie info page rendered
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

let closeFlash = document.getElementById("close-flash");
let flashPop = document.getElementById("flash-pop");
// When the user clicks on <span> (x), close the flash
$(closeFlash).click(function(){
        $(flashPop).css("display", "none");
    });