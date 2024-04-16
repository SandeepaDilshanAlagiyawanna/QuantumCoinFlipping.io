document.addEventListener("DOMContentLoaded", function () {
  const flipButton = document.getElementById("flipButton");
  const resultDisplay = document.getElementById("result");
  const errorDisplay = document.getElementById("error");

  flipButton.addEventListener("click", function () {
    // Send a GET request to the backend API endpoint
    fetch("/api/coin-flip")
      // Parse the JSON response
      .then((response) => response.json())
      // Handle the data received from the backend
      .then((data) => {
        // Update the UI with the result
        resultDisplay.textContent = "Result: " + data.result;
        // Clear any previous error message
        errorDisplay.textContent = "";
      })
      // Handle errors
      .catch((error) => {
        // Display an error message in the UI
        errorDisplay.textContent = "An error occurred: " + error.message;
        // Clear the result display
        resultDisplay.textContent = "";
      });
  });
});
