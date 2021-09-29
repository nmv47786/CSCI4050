<html>
<head>
   <title>Login and Reg Page</title>
   <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
   <div class="hero">
      <div class="form-box">
         <div class="button-box">
            <div id="btn"></div>
            <button type="button" class="toggle-btn" onclick="login()">Log In</button>
            <button type="button" class="toggle-btn" onclick="register()">Register</button>

         </div>
         <form id="login" class="input">
            <input type="text" class="input-field" placeholder="User Id" required>
            <input type="text" class="input-field" placeholder="Enter Password" required>
            <input type="checkbox" class="check-box"><span>Remember Password</span>
            <button type="submit" class="submit-btn">Log In</button>
         </form>
         <form id="register" class="input">
            <input type="text" class="input-field" placeholder="User Id" required>
            <input type="email" class="input-field" placeholder="Email Id" required>
            <input type="text" class="input-field" placeholder="Enter Password" required>
            <input type="checkbox" class="check-box"><span>I agree to the terms and conditions</span>
            <button type="submit" class="submit-btn">Register</button>
         </form>
      </div>
   </div>
   <script>
      var x=document.getElementById("login");
      var y=document.getElementById("register");
      var z=document.getElementById("btn");
      var img = document.body.style.backgroundImage="url('dune.jpg')";
      var newimg = new Image;
      newimg.onload = function() {
      img.src = this.src;
      }
      function login(){
         x.style.left="50px";
         y.style.left="450px";
         z.style.left="0px";
         document.body.style.backgroundImage = "url('film.jpg')";
      }
      function register(){
         x.style.left="-400px";
         y.style.left="50px";
         z.style.left="110px";
         document.body.style.backgroundImage = "url('movie.jpg')";
      }
      
   </script>
</body>
</html>
