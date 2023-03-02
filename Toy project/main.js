function signup(e) {
  event.preventDefault();

  var username = document.getElementById("username").value;
  var password = document.getElementById("password").value;

  var user = {
    username: username,
    password: password,
  };
  var json = JSON.stringify(user);
  localStorage.setItem(username, json);
  console.log("user added");
}

function loginFn(e) {
  event.preventDefault();

  var username = document.getElementById("username").value;
  var password = document.getElementById("password").value;
  var result = document.getElementById("result");

  var user = localStorage.getItem(username);
  var data = JSON.parse(user);

  if (user == null) {
    result.innerHTML = "wrong username";
  } else if (username == data.username && password == data.password) {
    result.innerHTML = "logged in";
  } else {
    result.innerHTML = "wrong password";
  }
}
