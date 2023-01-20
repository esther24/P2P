window.onload = () => {
    $("#cam1").click(() => {
      console.log("evoked openCam");
      $.ajax({
        url: "/yolo-words-detect",
        type: "GET",
        error: function (data) {
          console.log("upload error", data);
        },
        success: function (data) {
          console.log(data);
        }
      });
    })


  
    $("#cam2").click(() => {
      console.log("evoked openCam");
      $.ajax({
        url: "/yolo-alpha-detect",
        type: "GET",
        error: function (data) {
          console.log("upload error", data);
        },
        success: function (data) {
          console.log(data);
        }
      });
    })
  

  
    $("#cam3").click(() => {
      console.log("evoked openCam");
      $.ajax({
        url: "/lstm-detect-1",
        type: "GET",
        error: function (data) {
          console.log("upload error", data);
        },
        success: function (data) {
          console.log(data);
        }
      });
    })
  

  
    $("#cam4").click(() => {
      console.log("evoked openCam");
      $.ajax({
        url: "/lstm-detect-2",
        type: "GET",
        error: function (data) {
          console.log("upload error", data);
        },
        success: function (data) {
          console.log(data);
        }
      });
    })
  

 
    $("#cam5").click(() => {
      console.log("evoked openCam");
      $.ajax({
        url: "/lstm-detect-3",
        type: "GET",
        error: function (data) {
          console.log("upload error", data);
        },
        success: function (data) {
          console.log(data);
        }
      });
    })
  

 
    $("#cam6").click(() => {
      console.log("evoked openCam");
      $.ajax({
        url: "/lstm-detect-4",
        type: "GET",
        error: function (data) {
          console.log("upload error", data);
        },
        success: function (data) {
          console.log(data);
        }
      });
    })
  

  
    $("#cam7").click(() => {
      console.log("evoked openCam");
      $.ajax({
        url: "/lstm-detect-5",
        type: "GET",
        error: function (data) {
          console.log("upload error", data);
        },
        success: function (data) {
          console.log(data);
        }
      });
    })
  

  
    $("#cam8").click(() => {
      console.log("evoked openCam");
      $.ajax({
        url: "/lstm-detect-6",
        type: "GET",
        error: function (data) {
          console.log("upload error", data);
        },
        success: function (data) {
          console.log(data);
        }
      });
    })
};


  
function openCam1(e){
    console.log("evoked openCam");
    e.preventDefault();
    console.log("evoked openCam");
    console.log(e);
  }

function openCam2(e){
    console.log("evoked openCam");
    e.preventDefault();
    console.log("evoked openCam");
    console.log(e);
  }

function openCam3(e){
    console.log("evoked openCam");
    e.preventDefault();
    console.log("evoked openCam");
    console.log(e);
  }

function openCam4(e){
    console.log("evoked openCam");
    e.preventDefault();
    console.log("evoked openCam");
    console.log(e);
  }

function openCam5(e){
    console.log("evoked openCam");
    e.preventDefault();
    console.log("evoked openCam");
    console.log(e);
  }

function openCam6(e){
    console.log("evoked openCam");
    e.preventDefault();
    console.log("evoked openCam");
    console.log(e);
  }

function openCam7(e){
    console.log("evoked openCam");
    e.preventDefault();
    console.log("evoked openCam");
    console.log(e);
  }

function openCam8(e){
    console.log("evoked openCam");
    e.preventDefault();
    console.log("evoked openCam");
    console.log(e);
  }

  // function scrollFunction1() {
  //   let e = document.getElementById("el1");
  //   e.scrollIntoView({
  //     block: 'start',
  //     behavior: 'smooth',
  //     inline: 'start'
  //   });
  // }