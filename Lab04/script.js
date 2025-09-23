document.getElementById("loginForm").addEventListener("submit", function(e) {
  e.preventDefault(); // Ngăn load lại trang

  let username = document.getElementById("username").value.trim();
  let password = document.getElementById("password").value.trim();
  let message = document.getElementById("message");

  if (username === "" || password === "") {
    message.style.color = "red";
    message.textContent = "Please enter both username and password!";
  } else if (password.length < 6) {
    message.style.color = "red";
    message.textContent = "Password must be at least 6 characters!";
  } else {
    message.style.color = "green";
    message.textContent = "Login successful! (demo)";
  }
});

function cancelLogin() {
  document.getElementById("loginForm").reset();
  document.getElementById("message").textContent = "";
}
