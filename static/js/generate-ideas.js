function loadIdeas() {
    var audience = document.querySelector("#audience");
    var button_load = document.querySelector("#loadIdeas_btn");

    button_load.disabled = true;
    button_load.innerHTML = '<div class="spinner-border" role="status"></div>';

    fetch(`/load-ideas?a=${audience.value}`).then((response) => {
        response.json().then((data) => {
            var ideas = document.querySelector("#ideas_table");
            ideas.innerHTML = data[0];
            button_load.disabled = false;
            button_load.innerHTML = "Generate Ideas";
        });
    });
}

function useIdeas(i_id) {
    var title = document.querySelector(`#title_${i_id}`).innerHTML;
    var description = document.querySelector(`#desc_${i_id}`).innerHTML;
    var audience = document.querySelector("#audience").value;

    window.location.href = `/custom-ideas/${title}/${audience}/${description}`;
}