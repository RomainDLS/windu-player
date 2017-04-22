function play_movie(id){
  send_command('play', id);
  show_sub_div(id);
}

function show_sub_div(id){
  // Hide openned sub row
  div_list = document.getElementById('movie_list').children[1].children;
  for (i=0; i<div_list.length; i++){
    if (!div_list[i].id.match(/^\d+$/)) {
      div_list[i].style.display = "None";
    }
  }

  document.getElementById("sub_row" + id).style.display = "block";
}

function send_command(command, movie_pk){
  var http = new XMLHttpRequest();
  var url = "/api/movies/" + movie_pk;
  var params = new FormData();
  params.append('command', command)
  http.open("POST", url, true);

  //Send the proper header information along with the request
  http.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));

  http.send(params);
}

// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
