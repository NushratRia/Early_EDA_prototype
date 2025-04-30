import cv2
import threading
import mediapipe as mp

class FingertipTracker:
    def __init__(self):
        self.fingertips = []
        self.running = False
        self.thread = threading.Thread(target=self._run, daemon=True)

    def start(self):
        self.running = True
        self.thread.start()

    def _run(self):
        mp_hands = mp.solutions.hands
        cap = cv2.VideoCapture(0)
        fingertip_ids = [4, 8, 12, 16, 20]

        with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7) as hands:
            while self.running:
                ret, frame = cap.read()
                if not ret:
                    continue

                frame = cv2.flip(frame, 1)
                rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                result = hands.process(rgb)

                if result.multi_hand_landmarks:
                    h, w, _ = frame.shape
                    hand_landmarks = result.multi_hand_landmarks[0]
                    self.fingertips = [
                        (int(hand_landmarks.landmark[i].x * w),
                         int(hand_landmarks.landmark[i].y * h))
                        for i in fingertip_ids
                    ]

        cap.release()

    def stop(self):
        self.running = False
        self.thread.join()
