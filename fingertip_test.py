import cv2
import mediapipe as mp

# Setup MediaPipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Fingertip landmark indices in MediaPipe
fingertip_ids = [4, 8, 12, 16, 20]

# Start webcam
cap = cv2.VideoCapture(0)

with mp_hands.Hands(
        max_num_hands=2,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.5) as hands:

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            continue

        image = cv2.flip(image, 1)  # Mirror image
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Process the frame
        results = hands.process(image_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw landmarks on the hand
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                h, w, _ = image.shape
                for idx in fingertip_ids:
                    x = int(hand_landmarks.landmark[idx].x * w)
                    y = int(hand_landmarks.landmark[idx].y * h)
                    cv2.circle(image, (x, y), 8, (0, 0, 255), -1)  # Red fingertip

        cv2.imshow("Fingertip Detection", image)
        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
