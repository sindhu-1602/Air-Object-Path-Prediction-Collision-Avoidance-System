// LOGIN
document.getElementById("loginForm")?.addEventListener("submit", function (e) {
  e.preventDefault();
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  console.log("🔐 Attempting login with:", username, password);

  fetch("http://localhost:5000/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password }),
  })
    .then(res => res.json())
    .then(data => {
      console.log("✅ Login response:", data);

      if (data.success) {
        localStorage.setItem("username", username);
        console.log("🎉 Login successful. Redirecting to dashboard...");
        window.location.href = "dashboard.html";
      } else {
        console.warn("❌ Login failed.");
        alert("Invalid username or password!");
      }
    })
    .catch(err => {
      console.error("🚨 Login error:", err);
    });
});


// REGISTER
document.getElementById("registerForm")?.addEventListener("submit", function (e) {
  e.preventDefault();
  const u = document.getElementById("newUsername").value;
  const p1 = document.getElementById("newPassword").value;
  const p2 = document.getElementById("confirmPassword").value;

  console.log("📝 Registering user:", u);

  if (p1 !== p2) {
    alert("Passwords do not match");
    console.warn("❌ Registration failed: passwords don't match");
    return;
  }

  fetch("http://localhost:5000/register", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username: u, password: p1 }),
  })
    .then(res => res.json())
    .then(data => {
      console.log("✅ Register response:", data);

      if (data.success) {
        alert("Registered! Login now");
        console.log("🎉 Registration successful. Redirecting to login page...");
        window.location.href = "index.html";
      } else {
        alert("Registration failed");
        console.warn("❌ Registration failed.");
      }
    })
    .catch(err => {
      console.error("🚨 Registration error:", err);
    });
});


// CHANGE PASSWORD
document.getElementById("changePasswordForm")?.addEventListener("submit", function (e) {
  e.preventDefault();
  const u = document.getElementById("changeUsername").value;
  const oldP = document.getElementById("oldPassword").value;
  const newP = document.getElementById("newPasswordChange").value;

  console.log("🔁 Changing password for:", u);

  fetch("http://localhost:5000/change-password", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      username: u,
      old_password: oldP,
      new_password: newP
    }),
  })
    .then(res => res.json())
    .then(data => {
      console.log("✅ Change password response:", data);

      if (data.success) {
        alert("Password changed! Please login again.");
        console.log("🔒 Password successfully changed. Redirecting to login.");
        window.location.href = "index.html";
      } else {
        alert("Change failed.");
        console.warn("❌ Password change failed.");
      }
    })
    .catch(err => {
      console.error("🚨 Change password error:", err);
    });
});
