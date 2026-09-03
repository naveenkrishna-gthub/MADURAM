"""
Trainable Emotion Classifier Script (Updated: SMILE, CRY, LAUGH, ANGRY, FREEZE)
=============================================================================
This script trains the model on the refined emotion classes:
- SMILE: mouth corners spread wide & pulled up
- CRY: mouth corners pulled down + inner brows raised
- LAUGH: wide open mouth + expanded smile
- ANGRY: eyebrows furrowed tight together
- FREEZE: zero landmark movement delta
- NEUTRAL: relaxed resting face

Outputs:
1. `emotion_model.json` (Frontend weights to upload directly to your website)
2. `emotion_model.pkl`  (Python model file for backend)
=============================================================================
"""

import json
import numpy as np
from sklearn.linear_model import LogisticRegression

EMOTIONS = ["NEUTRAL", "SMILE", "CRY", "LAUGH", "ANGRY"]

def generate_synthetic_features():
    """
    Features:
    [0] mouth_width_ratio       (mouth width / face height)
    [1] mouth_open_ratio        (lip gap / face height)
    [2] mouth_corner_elevation  (lip center Y - corners Y) / face height [positive=smile, negative=cry]
    [3] brow_lift_ratio         (eyebrow to eye distance / face height)
    [4] inner_brow_dist         (distance between inner brows / face height)
    """
    X = []
    y = []

    # 0. Neutral
    for _ in range(300):
        feat = [
            np.random.normal(0.32, 0.02),
            np.random.normal(0.04, 0.01),
            np.random.normal(0.00, 0.01),
            np.random.normal(0.13, 0.01),
            np.random.normal(0.16, 0.01),
        ]
        X.append(feat)
        y.append(0)

    # 1. Smile
    for _ in range(300):
        feat = [
            np.random.normal(0.44, 0.03), # wide
            np.random.normal(0.08, 0.02),
            np.random.normal(0.04, 0.01), # corners up!
            np.random.normal(0.14, 0.01),
            np.random.normal(0.17, 0.01),
        ]
        X.append(feat)
        y.append(1)

    # 2. Cry / Frown
    for _ in range(300):
        feat = [
            np.random.normal(0.30, 0.02),
            np.random.normal(0.06, 0.02),
            np.random.normal(-0.04, 0.01), # corners pulled DOWN!
            np.random.normal(0.16, 0.02),  # inner brows raised
            np.random.normal(0.13, 0.01),
        ]
        X.append(feat)
        y.append(2)

    # 3. Laugh (Big open mouth + smile)
    for _ in range(300):
        feat = [
            np.random.normal(0.42, 0.03), # wide
            np.random.normal(0.24, 0.03), # very open mouth!
            np.random.normal(0.03, 0.01),
            np.random.normal(0.18, 0.02),
            np.random.normal(0.17, 0.01),
        ]
        X.append(feat)
        y.append(3)

    # 4. Angry / Scowl
    for _ in range(300):
        feat = [
            np.random.normal(0.31, 0.02),
            np.random.normal(0.03, 0.01),
            np.random.normal(-0.01, 0.01),
            np.random.normal(0.09, 0.01), # brow lowered
            np.random.normal(0.09, 0.01), # brows furrowed tight together!
        ]
        X.append(feat)
        y.append(4)

    return np.array(X), np.array(y)

def train_and_export():
    print("[*] Generating training vectors for SMILE, CRY, LAUGH, ANGRY...")
    X, y = generate_synthetic_features()

    clf = LogisticRegression(max_iter=1000)
    clf.fit(X, y)
    acc = clf.score(X, y)
    print(f"[+] Training Accuracy: {acc * 100:.2f}%")

    model_payload = {
        "model_name": "EmotionReverseRoasterModel",
        "version": "2.0",
        "classes": EMOTIONS[:5], # Classifier handles top 5, FREEZE is handled by temporal delta
        "features": [
            "mouth_width_ratio",
            "mouth_open_ratio",
            "mouth_corner_elevation",
            "brow_lift_ratio",
            "inner_brow_dist"
        ],
        "coefficients": clf.coef_.tolist(),
        "intercepts": clf.intercept_.tolist(),
        "malayalam_opposite_roasts": {
            "SMILE": {
                "win": "ഓ പിന്നെ, വലിയൊരു ഇളി! പല്ല് മൊത്തം താഴെ വീഴുമല്ലോ മോനേ.",
                "fail": "ഇളിക്കാൻ പറഞ്ഞപ്പോൾ കരയുന്നോ? സീൻ കോൺട്രാ, ഔട്ട്!"
            },
            "CRY": {
                "win": "ആഹാ, ഏഷ്യാനെറ്റ് സീരിയൽ ലെവൽ കരച്ചിൽ! കണ്ണ് നിറഞ്ഞു പോയി, 10 പോയിന്റ്.",
                "fail": "കണ്ണീരും വന്നില്ല ചിരിയും വന്നില്ല! പണി പാളി, ഔട്ട്!"
            },
            "LAUGH": {
                "win": "വാ പൊളിച്ചത് കണ്ടാൽ കൊതുക് മൊത്തം അകത്തു കേറും! എജ്ജാതി അലറൽ.",
                "fail": "വാ പൊളിക്കാൻ പറഞ്ഞപ്പോൾ ഉറങ്ങുകയായിരുന്നോ? ഔട്ട്!"
            },
            "ANGRY": {
                "win": "അയ്യോ ഞാൻ പേടിച്ചു വിറച്ചു പോയി! വലിയ ഗുണ്ടയാണെന്നാ വിചാരം.",
                "fail": "ഇത്രയും പാവമാണോ നീ? മുഖത്ത് ഒരു ദേഷ്യവും ഇല്ല! ഔട്ട്!"
            }
        }
    }

    with open("emotion_model.json", "w", encoding="utf-8") as f:
        json.dump(model_payload, f, indent=2, ensure_ascii=False)
    print("[+] Successfully exported: emotion_model.json")

    import pickle
    with open("emotion_model.pkl", "wb") as f:
        pickle.dump(clf, f)
    print("[+] Successfully exported: emotion_model.pkl")

if __name__ == "__main__":
    train_and_export()
