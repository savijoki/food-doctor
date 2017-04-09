$('#find_recipe').on('submit', function(event) {
  event.preventDefault();

  $('#search_results').html(`
    <div class="valign-wrapper" style="height:300px;">
      <div class="preloader-wrapper big active" style="margin:auto;">
        <div class="spinner-layer spinner-blue">
          <div class="circle-clipper left">
            <div class="circle"></div>
          </div>
          <div class="gap-patch">
            <div class="circle">
          </div>
        </div>
        <div class="circle-clipper right">
          <div class="circle"></div>
        </div>
      </div>
    </div>
  `);

  $.get($(this).attr('action'), {'search': $('#search').val()})
    .done(function(data) {
      var results = data['results'];
      var image_url = data['IMG_URL'];
      var container = $('#search_results');
      var element = "";
      $.each(results, function(index, value) {
        element += `
          <div class="col l3 m4 s6">
            <div class="card large">
              <div class="card-image waves-effect waves-block waves-light">
                <div class="activator" 
                  style="width:100%; height:300px;background: url('${image_url}${value['image']}') no-repeat 50% 50%; background-size:cover;"></div>
              </div>
              <div class="card-content">
                <i class="material-icons right">more_vert</i>
                <span class="card-title activator grey-text text-darken-4">${value['title']}
                </span>
              </div>
              <div class="card-reveal">
                <span class="card-title grey-text text-darken-4"><i class="material-icons right">close</i>${value['title']}</span>
                <p><b>Cooking time: </b> ${value['readyInMinutes']} minutes</p>
                <div class="content-bottom center-align">
                  <a href="/recipes/${value['id']}"
                    class="btn btn-large waves-effect waves-light">Read more...</a>
                </div>
              </div>
            </div>
          </div>
        `;
      });
      if (results.length == 0) {
        element = `
          <center>
            <h3>No recipes found! Try searching again!</h3>
          </center>
        `;
      }
      $(container).html(element);
  });
});
