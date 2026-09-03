# Teammate Handover Package 📦
### *Background Emotion Matcher + Sarcastic Malayalam Reverse Roaster*

Here is the exact code and trained model files ready to upload directly into your website.

---

## 📁 What You Have In This Folder

| File | Role for Website |
| :--- | :--- |
| **`emotionDetector.js`** | **The Core Brain:** Detects **SMILE, CRY, LAUGH, ANGRY, FREEZE** via webcam and includes the **Opposite Malayalam Roaster voice engine** (`speakOppositeRoast()`). |
| **`emotion_model.json`** | **The Trained Model Weights:** JSON file containing the trained weights and Malayalam roaster response dictionaries. |
| **`index.html`** | **Full Working Demo:** Complete UI showing the background emotion demands, matching loop, timer, and audio roaster. |

---

## 🚀 How to Add This to Your Website (3 Simple Steps)

### Step 1: Put MediaPipe in your HTML `<head>`
```html
<script src="https://cdn.jsdelivr.net/npm/@mediapipe/camera_utils/camera_utils.js" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/@mediapipe/face_mesh/face_mesh.js" crossorigin="anonymous"></script>
<script src="emotionDetector.js"></script>
```

### Step 2: Add a `<video>` element
```html
<video id="webcam" autoplay playsinline style="transform: scaleX(-1); width: 640px; height: 480px;"></video>
```

### Step 3: Game Matching & Reverse Malayalam Roast in JS
```javascript
const detector = new EmotionDetector({ confidenceThreshold: 0.50, voiceEnabled: true });
const video = document.getElementById('webcam');

// Target demanded by background: 'SMILE', 'CRY', 'LAUGH', 'ANGRY', 'FREEZE'
let backgroundTarget = 'SMILE'; 

await detector.start(video, (result) => {
    console.log("Detected Face:", result.emotion); 
    // e.g. 'SMILE', 'CRY', 'LAUGH', 'ANGRY', 'FREEZE', or 'NEUTRAL'

    // 1. Check if user matched the background demand!
    if (result.emotion === backgroundTarget) {
        console.log("User matched the emotion!");
        
        // 2. Play the OPPOSITE sarcastic Malayalam roast!
        // E.g. When user smiles: "Ooo pinne velya oru chiri! Enthoru asahaneeyatha."
        // E.g. When user cries: "Aaha mega serial-il abhinayikkan pattiya karachil!"
        const roastSaid = detector.speakOppositeRoast(backgroundTarget, true);
        
        // Pick next random target for background
        backgroundTarget = 'CRY'; 
    }
});

// If the timer runs out before user matches:
function onTimeout() {
    // Speaks sarcastic fail roast: "Ithanu ninte expression enkil kashtam thanne! Game over."
    detector.speakOppositeRoast(backgroundTarget, false);
}
```

---

## 🎭 The Built-In Opposite Malayalam Roasts

| Emotion Demanded | When User Wins (Opposite / Sarcastic Roasts) |
| :--- | :--- |
| **SMILE** | *"Ooo pinne velya oru chiri! Enthoru asahaneeyatha."*<br>*"Aha, pallu muzhuvan kaanichu chirikkunnu! Pity points awarded."* |
| **CRY** | *"Aaha, mega serial-il abhinayikkan pattiya karachil! Oscar tharam."*<br>*"Karayan paranjappol kooduthal sankadam abhinayikkunnu! Points edutholu."* |
| **LAUGH** | *"Vaa polichathu kandal aana vare akathu kerum! Hideousness points."*<br>*"Ooo velya chiri aanallo! Ayye, adutha round."* |
| **ANGRY** | *"Ayyoo njan pedichu poyi! Bheekara look thanne."*<br>*"Kovam kandal thonnum collector aavan varunnu ennu. Point eduthu podey."* |
| **FREEZE** | *"Velya statue aanenna vicharam! Shwasam polum vidunnilla. Points."*<br>*"Aha rock pole nilkkunnu. Charisma zero, pakshe points 10."* |
