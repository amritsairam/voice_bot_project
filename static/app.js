const recordBtn = document.getElementById("record-btn");
const transcription = document.getElementById("transcription");
const responseText = document.getElementById("response");
const audioPlayer = document.getElementById("audio-player");

let mediaRecorder;
let audioChunks = [];

recordBtn.addEventListener("mousedown", startRecording);
recordBtn.addEventListener("mouseup", stopRecording);

async function startRecording() {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    mediaRecorder = new MediaRecorder(stream);
    mediaRecorder.start();

    mediaRecorder.ondataavailable = event => {
        audioChunks.push(event.data);
    };

    console.log("Recording...");
}

async function stopRecording() {
    mediaRecorder.stop();
    mediaRecorder.onstop = async () => {
        console.log("Recording stopped.");
        const audioBlob = new Blob(audioChunks, { type: "audio/wav" });
        audioChunks = [];

        const formData = new FormData();
        formData.append("file", audioBlob, "audio.wav");

        const response = await fetch("/stt", { method: "POST", body: formData });
        const data = await response.json();
        transcription.innerText = `You: ${data.text}`;

        fetchChatResponse(data.text);
    };
}

async function fetchChatResponse(text) {
    const response = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text }),
    });

    const data = await response.json();
    responseText.innerText = `Bot: ${data.response}`;
    audioPlayer.src = data.audio_url;
    audioPlayer.play();
}
