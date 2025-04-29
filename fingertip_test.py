import cv2
import numpy as np

hand_hist = None
traverse_point = []
total_rectangle = 9
hand_rect_one_x = None
hand_rect_one_y = None
hand_rect_two_x = None
hand_rect_two_y = None

def contours(hist_mask_image):
    gray = cv2.cvtColor(hist_mask_image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 0, 255, 0)
    cont, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return cont

def draw_rect(frame):
    rows, cols, _ = frame.shape
    global total_rectangle, hand_rect_one_x, hand_rect_one_y, hand_rect_two_x, hand_rect_two_y

    hand_rect_one_x = np.array([
        6 * rows / 20, 6 * rows / 20, 6 * rows / 20,
        9 * rows / 20, 9 * rows / 20, 9 * rows / 20,
        12 * rows / 20, 12 * rows / 20, 12 * rows / 20
    ], dtype=np.uint32)

    hand_rect_one_y = np.array([
        9 * cols / 20, 10 * cols / 20, 11 * cols / 20,
        9 * cols / 20, 10 * cols / 20, 11 * cols / 20,
        9 * cols / 20, 10 * cols / 20, 11 * cols / 20
    ], dtype=np.uint32)

    hand_rect_two_x = hand_rect_one_x + 10
    hand_rect_two_y = hand_rect_one_y + 10

    for i in range(total_rectangle):
        cv2.rectangle(frame,
                      (hand_rect_one_y[i], hand_rect_one_x[i]),
                      (hand_rect_two_y[i], hand_rect_two_x[i]),
                      (0, 255, 0), 1)
    return frame

def hand_histogram(frame):
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    roi = np.zeros([90, 10, 3], dtype=hsv_frame.dtype)
    for i in range(total_rectangle):
        roi[i * 10: i * 10 + 10, 0: 10] = hsv_frame[
            hand_rect_one_x[i]:hand_rect_one_x[i] + 10,
            hand_rect_one_y[i]:hand_rect_one_y[i] + 10
        ]
    hand_hist = cv2.calcHist([roi], [0, 1], None, [180, 256], [0, 180, 0, 256])
    return cv2.normalize(hand_hist, hand_hist, 0, 255, cv2.NORM_MINMAX)

def hist_masking(frame, hist):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    dst = cv2.calcBackProject([hsv], [0, 1], hist, [0, 180, 0, 256], 1)
    disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (31, 31))
    cv2.filter2D(dst, -1, disc, dst)
    _, thresh = cv2.threshold(dst, 150, 255, cv2.THRESH_BINARY)
    thresh = cv2.merge((thresh, thresh, thresh))
    return cv2.bitwise_and(frame, thresh)

def centroid(contour):
    M = cv2.moments(contour)
    if M['m00'] != 0:
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        return cx, cy
    return None

def farthest_point(defects, contour, center):
    if defects is not None and center is not None:
        s = defects[:, 0][:, 0]
        cx, cy = center
        x = np.array(contour[s][:, 0][:, 0], dtype=np.float64)
        y = np.array(contour[s][:, 0][:, 1], dtype=np.float64)
        dist = np.sqrt((x - cx) ** 2 + (y - cy) ** 2)
        max_i = np.argmax(dist)
        if max_i < len(s):
            return tuple(contour[s[max_i]][0])
    return None

def draw_circles(frame, points):
    if points is not None:
        for i in range(len(points)):
            cv2.circle(frame, points[i], int(5 - (5 * i * 3) / 100), (0, 255, 255), -1)

def manage_image_opr(frame, hand_hist):
    mask_image = hist_masking(frame, hand_hist)
    mask_image = cv2.erode(mask_image, None, iterations=2)
    mask_image = cv2.dilate(mask_image, None, iterations=2)

    contour_list = contours(mask_image)
    if not contour_list:
        return

    max_cont = max(contour_list, key=cv2.contourArea)
    if max_cont is None:
        return

    center = centroid(max_cont)
    if center:
        cv2.circle(frame, center, 5, (255, 0, 255), -1)

    hull = cv2.convexHull(max_cont, returnPoints=False)
    if hull is not None and len(hull) > 3:
        defects = cv2.convexityDefects(max_cont, hull)
        far_point = farthest_point(defects, max_cont, center)
        if far_point:
            print("Centroid:", center, "Farthest Point:", far_point)
            cv2.circle(frame, far_point, 5, (0, 0, 255), -1)
            if len(traverse_point) < 20:
                traverse_point.append(far_point)
            else:
                traverse_point.pop(0)
                traverse_point.append(far_point)
            draw_circles(frame, traverse_point)

def main():
    global hand_hist
    is_hand_hist_created = False
    cap = cv2.VideoCapture(0)

    cv2.namedWindow("Live Feed", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Live Feed", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    while cap.isOpened():
        pressed_key = cv2.waitKey(1)
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)

        if pressed_key == ord('z'):
            hand_hist = hand_histogram(frame)
            is_hand_hist_created = True

        if is_hand_hist_created:
            manage_image_opr(frame, hand_hist)
        else:
            frame = draw_rect(frame)

        cv2.imshow("Live Feed", frame)

        if pressed_key == 27:  # ESC to exit
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
