// Initial Values
let MOVIE_DB_API = '7086f3df7f1d4285192dbd81ceafdd50';
let MOVIE_DB_ENDPOINT = 'https://api.themoviedb.org';
let MOVIE_DB_IMAGE_ENDPOINT = 'https://image.tmdb.org/t/p/w500';
let DEFAULT_POST_IMAGE = 'https://via.placeholder.com/150';

function requestMovies(url, onComplete, onError) {
    fetch(url)
        .then((res) => res.json())
        .then(onComplete)
        .catch(onError);
}

function generateMovieDBUrl(path) {
    let url = `${MOVIE_DB_ENDPOINT}/3${path}?api_key=${MOVIE_DB_API}`;
    return url;
}


function getTopRatedMovies() {
    let url = generateMovieDBUrl(`/movie/top_rated`);
    let render = renderMovies.bind({ title: 'Top Rated Movies' })
    requestMovies(url, render, handleGeneralError);
}

function getTrendingMovies() {
    let url = generateMovieDBUrl('/trending/movie/day');
    let render = renderMovies.bind({ title: 'Trending Movies' })
    requestMovies(url, render, handleGeneralError);
}


function searchUpcomingMovies() {
    let url = generateMovieDBUrl('/movie/upcoming');
    let render = renderMovies.bind({ title: 'Upcoming Movies' })
    requestMovies(url, render, handleGeneralError);
}

function searchMovieTitle() {
    idElement = document.getElementById("movie-id");
    movieId = idElement.innerHTML;
    let url = generateMovieDBUrl(`/movie/${movieId}`);
    axios.get(url)
        .then(function (response) {
            title = response.data.title;
            filmTitle = `<h2 id="film-title">${title}</h2>`;
            titleContainer = document.getElementById("title-container");
            titleContainer.innerHTML = filmTitle;   
    });  
}

function searchMovieDate() {
    idElement = document.getElementById("movie-id");
    movieId = idElement.innerHTML;
    let url = generateMovieDBUrl(`/movie/${movieId}`);
    axios.get(url)
        .then(function (response) {
            date = response.data.release_date.slice(0, 4);
            filmRelease = `<p id="film-date">(${date})</p>`;
            dateContainer = document.getElementById("release-container");
            dateContainer.innerHTML = filmRelease;   
    });  
}

function searchMovieImg() {
    idElement = document.getElementById("movie-id");
    movieId = idElement.innerHTML;
    let url = generateMovieDBUrl(`/movie/${movieId}`);
    axios.get(url)
        .then(function (response) {
            img = response.data.poster_path;
            filmImg = `<img id="film-img" src="${MOVIE_DB_IMAGE_ENDPOINT + img}" alt="">`;
            imgContainer = document.getElementById("img-container");
            imgContainer.innerHTML = filmImg;   
    });  
}

function searchMovieRating() {
    idElement = document.getElementById("movie-id");
    movieId = idElement.innerHTML;
    let url = generateMovieDBUrl(`/movie/${movieId}`);
    axios.get(url)
        .then(function (response) {
            rating = response.data.vote_average;
            filmRating = `<p id="film-rating" class="rating">TMDB rating: ${rating}</p>`;
            ratingContainer = document.getElementById("rating-container");
            ratingContainer.innerHTML = filmRating;   
    });  
}

function searchMovieSynapsis() {
    idElement = document.getElementById("movie-id");
    movieId = idElement.innerHTML;
    let url = generateMovieDBUrl(`/movie/${movieId}`);
    axios.get(url)
        .then(function (response) {
            plot = response.data.overview;
            filmPlot = `<p id="film-plot">${plot}</p>`;
            plotContainer = document.getElementById("plot-container");
            plotContainer.innerHTML = filmPlot;   
    });  
}

function searchPopularMovie() {
    let url = generateMovieDBUrl('/movie/popular');
    let render = renderMovies.bind({ title: 'Popular Movies' });
    requestMovies(url, render, handleGeneralError);
}

// Different function for search movies
function searchMovie(value) {
    let url = generateMovieDBUrl('/search/movie') + '&query=' + value;
    requestMovies(url, renderSearchMovies, handleGeneralError);
}


function getVideosByMovieId(movieId, content) {
    let url = generateMovieDBUrl(`/movie/${movieId}/videos`);
    let render = createVideoTemplate.bind({ content });
    requestMovies(url, render, handleGeneralError);
}