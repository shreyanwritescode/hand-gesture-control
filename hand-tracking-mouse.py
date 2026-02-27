import cv2
import mediapipe as mp
import pyautogui
import time
screen_w, screen_h = pyautogui.size()
pyautogui.FAILSAFE = False
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(1, cv2.CAP_AVFOUNDATION)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 730)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 450)
prev_x, prev_y = screen_w // 2, screen_h // 2
alpha = 0.25     
dead_zone = 6       
last_click_time = 0
click_delay = 0.5 
def finger_up(tip, pip):
    return tip.y < pip.y
def distance(p1, p2):
    return ((p1.x - p2.x)**2 + (p1.y - p2.y)**2) ** 0.5
while True:
    success, frame = cap.read()
    if not success:
        break
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            lm = hand_landmarks.landmark
            index_tip = lm[8]
            index_pip = lm[6]
            thumb_tip = lm[4]
            if finger_up(index_tip, index_pip):
                x = int(index_tip.x * screen_w)
                y = int(index_tip.y * screen_h)
                smooth_x = int(prev_x + alpha * (x - prev_x))
                smooth_y = int(prev_y + alpha * (y - prev_y))
                if abs(smooth_x - prev_x) > dead_zone or abs(smooth_y - prev_y) > dead_zone:
                    pyautogui.moveTo(smooth_x, smooth_y)
                    prev_x, prev_y = smooth_x, smooth_y
            if distance(index_tip, thumb_tip) < 0.03:
                if time.time() - last_click_time > click_delay:
                    pyautogui.click()
                    last_click_time = time.time()
    cv2.imshow("Hand Mouse Smooth + Click", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
# python3.11 -m venv handenv 
# source handenv/bin/activate
# python3 /Users/shreyan/Documents/handtracking/hand_tracking.py