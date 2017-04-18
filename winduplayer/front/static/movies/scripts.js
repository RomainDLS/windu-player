function play_movie(row){
  send_command('play', row.id);
  show_sub_div(row);
}

function show_sub_div(row){
  sub_line = document.createElement('div');
  sub_line.className = 'row';
  sub_line.id = "sub_div";

  // add div
  if (row.nextSibling) {
    row.parentNode.insertBefore(sub_line, row.nextSibling);
  } else {
    row.parentNode.appendChild(sub_line);
  }
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
