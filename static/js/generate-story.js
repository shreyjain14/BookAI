function generateStory() {
    var title = document.querySelector("#title").value;
    var description = document.querySelector("#description").value;
    var audience = document.querySelector("#audience").value;
    var button_load = document.querySelector("#loadIdeas_btn");
    var story = document.querySelector("#story");

    button_load.disabled = true;
    button_load.innerHTML = '<div class="spinner-border" role="status"></div>';

    fetch(`/load-overview?a=${audience}&t=${title}&d=${description}`).then((response) => {
        response.json().then((data) => {
            story.innerHTML = data[0];
            button_load.disabled = false;
            button_load.innerHTML = "Generate Ideas";
        });
    });
}