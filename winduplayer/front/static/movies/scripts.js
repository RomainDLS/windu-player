function play_movie(row){
  show_sub_div(row);
}

function show_sub_div(row){
  sub_line = document.createElement('div');
  sub_line.className = 'row';
  sub_line.id = "sub_div"
  // add div
  if (row.nextSibling) {
    row.parentNode.insertBefore(sub_line, row.nextSibling);
  } else {
    row.parentNode.appendChild(sub_line);
  }
}
