function play_pause(button, id){
  // No movie is playing
  if (button.children[0].style.display == "none"){
    send_command('pause', id);
    button.children[0].style.display = "";
    button.children[1].style.display = "none";
  // Movie is playing
  } else if (button.children[1].style.display == "none"){
    send_command('play', id);
    button.children[0].style.display = "none";
    button.children[1].style.display = "";
  }
}

function show_sub_div(row, id){
  // Hide openned sub row
  div_list = document.getElementById('movie_list').children[1].children;
  for (i=0; i<div_list.length; i++){
    if (div_list[i].id.match(/^sub_row\d+$/)) {
      div_list[i].style.display = "None";
    } else if (div_list[i].id.match(/^row\d+$/)) {
      div_list[i].className = "active";
    }
  }

  row.className = "info"
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
