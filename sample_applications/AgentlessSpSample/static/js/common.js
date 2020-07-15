function toggleShowRaw(rawContentElementId, showRawLinkId) {
    let rawContentElement = document.getElementById(rawContentElementId);
    let showRawLinkElement = document.getElementById(showRawLinkId);

    if (rawContentElement.style.display === "block") {
        showRawLinkElement.innerHTML = "Show raw";
        rawContentElement.style.display = "none";
    } else {
        showRawLinkElement.innerHTML = "Hide raw";
        rawContentElement.style.display = "block";
    }
}

function back() {
    window.history.go(-1);
    event.preventDefault();
    return false;
}
