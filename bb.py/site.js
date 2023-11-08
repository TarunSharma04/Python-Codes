function playVideo() {
    var videoLink = document.getElementById("video-link").value;
    var viewsCount = document.getElementById("views-count").value;

    var videoId = videoLink.split("=")[1];
    var videoUrl = "https://www.youtube.com/embed/" + videoId;

    var iframe = document.createElement("iframe");
    iframe.width = "560";
    iframe.height = "315";
    iframe.src = videoUrl + "?autoplay=1&controls=0&showinfo=0";
    document.getElementById("video-container").innerHTML = "";

    for (var i = 0; i < viewsCount; i++) {
        document.getElementById("video-container").appendChild(iframe.cloneNode(true));
    }
}
