$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  const films = data.results;
  films.forEach(element => {
    $('#list_movies').append(`<li>${element.title}</li>`);
  });
});
