// Wait for the DOM to be fully loaded
document.addEventListener("DOMContentLoaded", function () {
    // Get Data button click handler
    document.getElementById("getDataBtn").addEventListener("click", function () {
        fetch("/api/data")
            .then(response => response.json())
            .then(data => {
                const outputDiv = document.getElementById("output");
                outputDiv.innerHTML = JSON.stringify(data, null, 2);
            });
    });

    // Set Cookie button click handler
    document.getElementById("setCookieBtn").addEventListener("click", function () {
        fetch("/set_cookie")
            .then(response => response.text())
            .then(message => {
                const outputDiv = document.getElementById("output");
                outputDiv.innerHTML = message;
            });
    });
});
