const {remote} = require('electron');


function close_current_window() {
  remote.getCurrentWindow().close();
}


function minimize_current_winodow() {
  remote.getCurrentWindow().minimize();
}


$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip();
});
