var display_cafes = function(data){
    firstTen = 0;
  $.each(data, function(i, datum){
      if (firstTen < 11 && !datum['mark_as_deleted'] ) { 
        firstTen++; 
      var idx = datum["id"]
      var logoLink = datum["logo"] 
      var n = datum["name"] 
      var lo = datum["location"]
      var newDiv = $("<div id = "+idx+ " class = 'card' style = 'width: 18rem;'> <a href = '/view/"+idx+"'> <img class='card-img-top' src ="+logoLink+" alt ='logo'> </a> <div class = 'card body'> <h5 class='card-title'>"+n+"</h5> <p class='card-text'>"+lo+"</p>")
      $("#Cafe_List").append(newDiv)
        }
        })
      }

      var displayResultsName = function(n){
      $("#Cafe_Search_Name").val("")
      $("#results").empty()
      var count = 0; 
      $.each(data, function(i, datum){
          var namelow = datum['name']
          namelow = namelow.toLowerCase();
          n = n.toLowerCase(); 
      if (namelow.includes(n) && !datum['mark_as_deleted']){
          var ID1 = datum["id"]
          count ++
          var viewcard = $("<div class = 'card'> <a href = '/view/"+ID1+"'> <img class='card-img-top' style = 'width: 18rem; align-self: center;' src ="+datum['logo']+" alt ='logo'> </a> <div class = 'card body'> <h5 class='card-title'>"+datum['name']+"</h5> <p class='card-text'> Location: "+datum["location"]+"<br> <a href = '"+datum["website"]+"'> Website </a> <br>"+datum["rating"]+"/5 star rating <br>About: "+datum["about"]+"</p> </div>")
          var j = parseFloat(datum['rating'])
          var m = $("<div>")
          j = Math.round(j);
          var rating = ("<img src = 'https://image.shutterstock.com/image-vector/star-icon-vector-classic-rank-260nw-429574270.jpg' alt = 'star rating' height = '20', width = '20'> ")
          for (let i =0; i<j; i++) { 
              m.append(rating);   
          }
          viewcard.append(m)
          var Space = $("<div id = 'Add_Space_"+ID1+"'>")
          viewcard.append(Space)
          $("#results").append(viewcard)
      }
      })
      if (count > 0){ 
          $("#how_many").html("You have "+count+" result/s")
      }
      if (count == 0){
          $("#how_many").html("No result")
      }  
  }

  var displayResultsLoc = function(tofind){
      $("#results").empty()
      $("#Cafe_Search_Loc").val("")
      var count = 0;
      $.each(data, function(i, datum){ 
          if ((datum['location']).includes(tofind) && !datum['mark_as_deleted']){
          count ++
          var IDX = datum["id"]
          var viewcard = $("<div class = 'card'> <a href = '/view/"+IDX+"'> <img class='card-img-top' style = 'width: 18rem; align-self: center;' src ="+datum['logo']+" alt ='logo'> </a> <div class = 'card body'> <h5 class='card-title'>"+datum['name']+"</h5> <p class='card-text'> Location: "+datum["location"]+"<br> <a href = '"+datum["website"]+"'> Website </a> <br>"+datum["rating"]+"/5 star rating <br>About: "+datum["about"]+"</p> </div>")
          var j = parseFloat(datum['rating'])
          var m = $("<div>")
          j = Math.round(j);
          var rating = ("<img src = 'https://image.shutterstock.com/image-vector/star-icon-vector-classic-rank-260nw-429574270.jpg' alt = 'star rating' height = '20', width = '20'> ")
          for (let i =0; i<j; i++) { 
              m.append(rating);   
          }
          viewcard.append(m)
          var Space = $("<div id = 'Add_Space_"+IDX+"'>")
          viewcard.append(Space)
          $("#results").append(viewcard)
      }
      })
      if (count > 0){ 
          $("#how_many").html("You have "+count+" result/s")
      }
      if (count == 0){
          $("#how_many").html("No result")
      }  
  }

  var saveNew = function(new_cafe){
  var data_to_save = {
  "name": new_cafe["name"], 
  "website": new_cafe["website"], 
  "logo": new_cafe["logo"],
  "location":new_cafe["location"],
  "rating":new_cafe["rating"],
  "about":new_cafe["about"],
      };
  $.ajax({
  type: "POST",
  url: "save_cafe",                
  dataType : "json",
  contentType: "application/json; charset=utf-8",
  data : JSON.stringify(data_to_save),
  success: function(result){
      var all_data = result["data"]
      data = all_data
      var newclient = result["cafes"]
      cafes = newclient 
      var LOC = result["locations"]
      locations = LOC
      display_cafes(data)        
  },
  error: function(request, status, error){
      console.log("Error");
      console.log(request)
      console.log(status)
      console.log(error)
  }
   }); 
  }

  var deleteName = function(ID){
  var p_id = {"id" : ID}
  console.log("deletecafeajax")
  $.ajax({
  type: "DELETE",
  url: "/delete_cafe",  
  dataType : "json",
  contentType: "application/json; charset=utf-8",
  data: JSON.stringify(p_id), 
  success: function(result){
      var all_data = result["data"]
      data = all_data
      display_cafes(data)
  },
  error: function(request, status, error){
      console.log("Error");
      console.log(request)
      console.log(status)
      console.log(error)
  }
  });
}

var undo = function(ID){
  var my_id = {"id" : ID}
  $.ajax({
  type: "POST",
  url: "undo_cafe",  
  dataType : "json",
  contentType: "application/json; charset=utf-8",
  data: JSON.stringify(my_id), 
  success: function(result){
      var all_data = result["data"]
      data = all_data
      display_cafes(data)
  },
  error: function(request, status, error){
      console.log("Error");
      console.log(request)
      console.log(status)
      console.log(error)
  }
  });
}

var viewit = function(myid){ 
      $("#viewme").empty()
      var count = 0;
      $.each(data, function(i, datum){ 
          if (datum['id'] == myid){
          count ++
          var viewcard = $("<div class = 'card'> <a href = '/view/"+myid+"'> <img class='card-img-top' style = 'width: 18rem; align-self: center;' src ="+datum['logo']+" alt ='logo'> </a> <div class = 'card body'> <h5 class='card-title'>"+datum['name']+"</h5> <p class='card-text'> Location: "+datum["location"]+"<br> <a href = '"+datum["website"]+"'> Website </a> <br>"+datum["rating"]+"/5 star rating <br>About: "+datum["about"]+"</p> </div>")
          var j = parseFloat(datum['rating'])
          var m = $("<div>")
          j = Math.round(j);
          var rating = ("<img src = 'https://image.shutterstock.com/image-vector/star-icon-vector-classic-rank-260nw-429574270.jpg' alt = 'star rating' height = '20', width = '20'> ")
          for (let i =0; i<j; i++) { 
              m.append(rating);   
          }
          viewcard.append(m)
          var Delete = $("<br> <button id ="+myid+" class ='Button btn-danger'>")
          Delete.html("Delete Cafe")
          var Update = $("<button id ="+myid+" class ='Update btn-warning'>")
          Update.html("Update Cafe")
          viewcard.append(Delete)
          viewcard.append(Update)
          var Space = $("<div id = 'Add_Space_"+myid+"'>")
          viewcard.append(Space)
          $("#viewme").append(viewcard)
      }
      })
      if (count > 0){ 
          $("#how_many").html("You have "+count+" result/s")
      }
      if (count == 0){
          $("#how_many").html("No result")
      }  
      $(".Button").on('click',function(){
          var ID = $(this).attr('id')
          deleteName(ID) //how to reassign index numbers 
          $("#viewme").val("")
          $("#viewme").html("<div class= 'successMe'> Item successfully deleted! Click <button id='undo'> here </button> to undo  </div>");
          $("#undo").on('click',function(){
          undo(ID)
          $("#viewme").val("")
          $("#viewme").html("<div class= 'successMe'> Undo successful! </div>");
          })
        })
        $(".Update").on('click',function(){
          var ID = $(this).attr('id')
          updateCafe(ID) //how to reassign index numbers 
          })
    }
    
    var updateCafe = function(ID){
      var un;
      var ul;
      var ulo;
      var uw;
      var ur;
      var ua; 

      $.each(data, function(i, datum){
          if (datum["id"]== ID) { 
      ul = datum["logo"] 
      ulo = datum["location"] 
      uw = datum["website"]
      un = datum["name"]
      ur = datum["rating"]
      ua = datum["about"]
          }
      })
      $("#Add_Space_"+ID).append("<input id='new_website' size = '32' value ="+uw+">")
      $("#Add_Space_"+ID).append("<br>")
      $("#Add_Space_"+ID).append("<input id='new_logo' size = '32' value ="+ul+">")
      $("#Add_Space_"+ID).append("<br>")
      $("#Add_Space_"+ID).append("<input id='new_location' size = '32' value ="+ulo+">")
      $("#Add_Space_"+ID).append("<br>")
      $("#Add_Space_"+ID).append("<input id='new_rating' size = '32' value ="+ur+">")
      $("#Add_Space_"+ID).append("<br>")
      $("#Add_Space_"+ID).append("<button id ='Submit_Up_"+ID+"' class = 'btn btn-success'> Submit Update </button>")
      $("#Add_Space_"+ID).append("<button id ='discard' class = 'btn btn-danger'> Discard changes </button>")

      $("#Submit_Up_"+ID).click(function(){
          var s = new Object();
          s.website = $('#new_website').val()
          s.logo = $('#new_logo').val()
          s.location = $('#new_location').val()
          s.rating = $('#new_rating').val()
          updateMe(ID,s)
          $("#Add_Space_"+ID).html("<div class= 'successMe'> Successfully updated! </div>")
      })

      $("#discard").click(function(){
        $("#Add_Space_"+ID).html("")
      })
  }

  var updateMe = function(ID, s){
    var updated = {"id" : ID, "website":s["website"], "logo": s["logo"], "rating": s["rating"], "location":s["location"]}
    $.ajax({
    type: "POST",
    url: "update",  
    dataType : "json",
    contentType: "application/json; charset=utf-8",
    data: JSON.stringify(updated), 
    success: function(result){
        var all_data = result["data"]
        data = all_data
        display_cafes(data)
    },
    error: function(request, status, error){
        console.log("Error");
        console.log(request)
        console.log(status)
        console.log(error)
    }
    });
  }

  $(document).ready(function(){
      $('#Cafe_Search_Name').autocomplete({
      source: cafes
      })  
      $('#Cafe_Search_Loc').autocomplete({
      source: locations
      }) 

      display_cafes(data)

      $('#Cafe_Search_Name').keypress(function(e){
      if (e.which == '13') { 
      $("#Submit_Name").click();
      }
      })

      $("#Submit_Name").click(function(){
      var n = $('#Cafe_Search_Name').val()
      displayResultsName(n)
      })

      $('#Cafe_Search_Loc').keypress(function(e){
      if (e.which == '13') { 
      $("#Submit_Loc").click();
      }
      })

      $("#Submit_Loc").click(function(){
      var tofind = $('#Cafe_Search_Loc').val()
      displayResultsLoc(tofind)
      })

      $("#Submit_New").click(function(){
          if ( $('#new_name').val().trim().length > 0 && $('#new_rating').val().trim().length > 0 && $('#new_website').val().trim().length > 0 && $('#new_logo').val().trim().length > 0 && $('#new_location').val().trim().length > 0 && $('#new_about').val().trim().length > 0){ 
          var new_cafe = new Object();
          new_cafe.name = $('#new_name').val()
          new_cafe.website = $('#new_website').val()
          new_cafe.logo = $('#new_logo').val()
          new_cafe.location = $('#new_location').val()
          new_cafe.rating = $('#new_rating').val()
          new_cafe.about = $('#new_about').val()
          saveNew(new_cafe)
          $("#successAdd").html("<div class= 'successMe'> New item successfully created! See it on the home page or search it! </div>");
          $("#new_name").val("")
          $("#new_website").val("")
          $("#new_logo").val("")
          $("#new_location").val("")
          $("#new_rating").val("")
          $("#new_about").val("")   
          $("#new_name").focus()
          $("#new_website").css('background-color','white');
          $("#new_logo").css('background-color','white');
          $("#new_location").css('background-color','white');
          $("#new_rating").css('background-color','white');
          $("#new_about").css('background-color','white');
          $("#new_name").css('background-color','white');
          }
          else {
          if ($('#new_name').val().trim().length < 1){
              $("#new_name").css('background-color','red');
              $("#new_name").attr("placeholder", "Please fill in the name");
              $("#new_name").focus();
          }
          if ($('#new_website').val().trim().length < 1){
              $("#new_website").css('background-color','red');
              $("#new_website").attr("placeholder", "Please fill in the website");
              $("#new_website").focus();
          }
          if ($('#new_logo').val().trim().length < 1){
              $("#new_logo").css('background-color','red');
              $("#new_logo").attr("placeholder", "Please fill in the logo link");
              $("#new_logo").focus();
          }
          if ($('#new_location').val().trim().length < 1){
              $("#new_location").css('background-color','red');
              $("#new_location").attr("placeholder", "Please fill in the location");
              $("#new_location").focus();
          }

          if ($('#new_rating').val().trim().length < 1){
              $("#new_rating").css('background-color','red');
              $("#new_rating").attr("placeholder", "Please rate the cafe out of 5");
              $("#new_rating").focus();
          }

          if ($('#new_about').val().trim().length < 1){
              $("#new_about").css('background-color','red');
              $("#new_about").attr("placeholder", "Please tell us about the cafe");
              $("#new_about").focus();
          }
          }
      })

    })