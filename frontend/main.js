
// Function to update the Alpine.js videos variable
function updateAlpineVideos(newVideos) {
    Alpine.store('videos', newVideos);
    console.log(Alpine.store('videos'));
}


const video_btn = document.getElementById("get_videos");
video_btn.addEventListener("click", function () {
    video_btn.disabled = true;
    video_btn.innerHTML = "Fetching videos...";
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "http://127.0.0.1:5000/videos", true);
    xhr.onload = function () {
        const newVideos = JSON.parse(xhr.response);
        updateAlpineVideos(newVideos);
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
        const newVideos = JSON.parse(xhr.response);
        updateAlpineVideos(newVideos);
        refresh_btn.disabled = false;
        refresh_btn.innerHTML = "Refresh";
    }
    xhr.send();
});

function delete_video() {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "http://127.0.0.1:5000/delete_one?videoId=" + this.video['videoId'], true);
    xhr.onload = function () {
        const videoId = xhr.response;
        console.log("Deleted: " + videoId);
    }
    xhr.send();
}

document.addEventListener('alpine:init', () => {
    Alpine.store('activeCategory', 'All')
})
