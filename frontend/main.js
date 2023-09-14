const video_btn = document.getElementById("get_videos");
video_btn.addEventListener("click", function () {
    video_btn.disabled = true;
    video_btn.innerHTML = "Fetching videos...";

    var xhr = new XMLHttpRequest();
    xhr.open("GET", "http://127.0.0.1:5000/videos", true);
    xhr.onload = function () {
        var text = xhr.responseText;
        const p = document.getElementById("output_videos");
        p.innerHTML = text;
        video_btn.disabled = false;
        video_btn.innerHTML = "Get videos";
    }
    xhr.send();
});

const refresh_btn = document.getElementById("refresh");
refresh_btn.addEventListener("click", function () {
    refresh_btn.disabled = true;
    refresh_btn.innerHTML = "Refreshing...";

    var xhr = new XMLHttpRequest();
    xhr.open("GET", "http://127.0.0.1:5000/refresh", true);
    xhr.onload = function () {
        var text = xhr.responseText;
        const p = document.getElementById("output_videos");
        p.innerHTML = text;
        refresh_btn.disabled = false;
        refresh_btn.innerHTML = "Refresh";
    }
    xhr.send();
});

document.addEventListener('alpine:init', () => {
    Alpine.store('activeCategory', 'All')
})