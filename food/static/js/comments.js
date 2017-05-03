$(function() {
  // C3JS initialization
  $('.modal').modal();
  var carbs = $('#recipe').data('carbs');
  var fat = $('#recipe').data('fat');
  var protein = $('#recipe').data('protein');

  var chart = c3.generate({
    bindto: '#chart',
    size: {
        height: 300,
        width: 300
    },
    data: {
      columns: [
        ['Carbohydrates', carbs],
        ['Fat', fat],
        ['Protein', protein]
      ]
    }
  });
  chart.transform('pie');

  $('.chart-button').on('click', function() {
    var value = $(this).val();
    chart.transform(value);
  });
  setInterval(update, 5000);
});

// This variable is used so that the polling is paused
// when modal dialogs are open
var update_allowed = true;


// Update comment section
function update() {

  if (update_allowed) {
    var recipe_id = $('#recipe').data('id');
    var url = '/recipes/'+ recipe_id + '/comments';
    $.get(url).done(function(data) {
      var container = $('#comments');
      var previous_count = $(container).find('.card-panel').length;
      var new_element = $('<div></div>').html(data).find('.card-panel');
      var new_element_count = $(new_element).length;
      if (previous_count === new_element_count) {
        return;
      } else {
        container.html(new_element);
      }
    });
  }
}


// This function retrieves the csrftoken
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


// Modal open handler
$(document).on('click', '.modal-trigger', function() {
  var id = $(this).data('button');
  var comment_id = $(this).data('id');
  update_allowed = false;
  if (id == 'delete_button'){
    $('#delete_modal').find('.btn-delete').attr('data-id', comment_id);
  } else if (id == 'edit_button') {
    var body = $('#body_' + comment_id).html().trim();
    $('#edit_comment_form').find("#id_body").val(body);
  }
});


// Continue longpolling for new messages after
// modal has been closed
$(document).on('click', '.modal-close', function() {
  update_allowed = true;
  setTimeout(update, 200);
});

// Delete comment js functionality
$(document).on('click', '.delete_confirm', function() {
  var comment_id = $(this).attr('data-id');
  var csrftoken = getCookie('csrftoken');
  $.post('/comments/delete/' + comment_id, {csrfmiddlewaretoken: csrftoken});
});


// Send a new comment only if body is not empty
$('#add_comment_form').on('submit', function(event) {
  event.preventDefault();
  var csrftoken = getCookie('csrftoken');
  var body = $(this).find('#id_body');
  var recipe_id = $('#comments').data('recipe-id');

  if (body.val().trim()) {
    $.post($(this).attr('action'), {
      csrfmiddlewaretoken: csrftoken,
      body: body.val().trim(),
      recipe_id: recipe_id
    });
  }
  body.val("");
});
