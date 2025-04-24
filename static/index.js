const format = document.getElementById("format");
const videoQuality = document.getElementById("video_quality");
const submitBtn = document.getElementById("submit-btn");

format.addEventListener("change", () => {
  if (format.value === "audio") {
    videoQuality.classList.add("hidden-option");
  } else if (
    format.value !== "audio" &&
    videoQuality.classList.contains("hidden-option")
  ) {
    videoQuality.classList.remove("hidden-option");
  }
});

submitBtn.addEventListener("click", () => {
  alert("URL Submited 😎");
});
