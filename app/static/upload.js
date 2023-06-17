function toggleEmailField() {
    var radio = document.getElementsByName("access");
    var emailField = document.getElementById("emailField");

    if (radio[2].checked) 
    {
      emailField.style.display = "block";
    } else {
      emailField.style.display = "none";
    }
  }

  function addEmailField() {
    var emailContainer = document.getElementById("emailContainer");
    var newEmailField = document.createElement("div");
    newEmailField.className = "email-container";

    var emailLabel = document.createElement("label");
    emailLabel.innerText = "Email:";
    newEmailField.appendChild(emailLabel);

    var emailInput = document.createElement("input");
    emailInput.type = "email";
    emailInput.name = "email";
    newEmailField.appendChild(emailInput);

    var deleteButton = document.createElement("button");
    deleteButton.className = "delete-button";
    deleteButton.innerText = "Delete";
    deleteButton.onclick = function() {
      emailContainer.removeChild(newEmailField);
    };
    newEmailField.appendChild(deleteButton);

    emailContainer.appendChild(newEmailField);
  }