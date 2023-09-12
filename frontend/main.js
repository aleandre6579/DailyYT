const btn = document.getElementById("get_videos");
btn.addEventListener("click", function () {
    btn.disabled = true;
    btn.innerHTML = "Fetching videos...";

    var xhr = new XMLHttpRequest();
    xhr.open("GET", "http://127.0.0.1:5000/videos?url=" + "THISISURL", true);
    xhr.onload = function () {
        var text = xhr.responseText;
        const p = document.getElementById("output");
        p.innerHTML = text;
        btn.disabled = false;
        btn.innerHTML = "Get videos";
    }
    xhr.send();
});

