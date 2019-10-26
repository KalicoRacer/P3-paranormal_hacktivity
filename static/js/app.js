// 1. update the h5 file
// 2. create an HTML tag with the text
// 3. update the text of the HTML tag from the function below (add the response to it)

function loadFile(event) {
    // var output = document.getElementById('blah');
    var fileName = event.target.files[0];
    var url = `/filelink/${fileName}`;
    d3.json(url).then(function(response){
      console.log(response);
      // d3.find("response").text = response
    })
    // output.src = URL.createObjectURL(event.target.files[0]);
    // console.log(event.target.files[0].name)
    // console.log(event.target.files[0])
  };
