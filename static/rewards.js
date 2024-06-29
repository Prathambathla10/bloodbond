document.addEventListener("DOMContentLoaded", function() {
    function toggleDetails(detailsId) {
        var detailsElement = document.getElementById(detailsId);
        if (detailsElement.style.display === "none" || detailsElement.style.display === "") {
            detailsElement.style.display = "block";
        } else {
            detailsElement.style.display = "none";
        }
    }

    window.toggleDetails = toggleDetails;
});