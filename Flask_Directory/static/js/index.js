const toggleDisplay = () => {
    let x = document.getElementById("form-post-comment");

    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}
