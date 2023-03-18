import cv2
import numpy as np

video = cv2.VideoCapture(r"rumbleverse all posiitives Good triggers.mp4")


def draw_rect(src, pt1, pt2, text=None, font=cv2.FONT_ITALIC, rect=True, rect_color=(0, 255, 0), rect_thickness=2,
              line=False, line_color=(0, 0, 255), line_thickness=2, line_rect_dst=0, line_length=0.25):
    if rect:
        cv2.rectangle(src, pt1, pt2, rect_color, rect_thickness)
    if text is not None:
        cv2.rectangle(src, (pt1[0], pt2[1]), (pt2[0], pt2[1] + 50), rect_color, cv2.FILLED)
        cv2.putText(src, text, (pt1[0] + 20, pt2[1] + 35), font, 1, (255, 255, 255), 2)

    point1 = (pt1[0] - line_rect_dst, pt1[1] - line_rect_dst)
    point2 = (pt2[0] + line_rect_dst, pt1[1] - line_rect_dst)
    point3 = (pt2[0] + line_rect_dst, pt2[1] + line_rect_dst)
    point4 = (pt1[0] - line_rect_dst, pt2[1] + line_rect_dst)

    dist_pt1_pt2 = point2[0] - point1[0]
    dist_pt1_pt4 = point4[1] - point1[1]

    if line:
        cv2.line(src, point1, (int(point1[0] + dist_pt1_pt2 * line_length), point2[1]), line_color,
                 line_thickness)  # point1 to right
        cv2.line(src, point1, (point4[0], int(point1[1] + dist_pt1_pt4 * line_length)), line_color,
                 line_thickness)  # point1 to bottom

        cv2.line(src, point2, (int(point2[0] - dist_pt1_pt2 * line_length), point2[1]), line_color,
                 line_thickness)  # point2 to left
        cv2.line(src, point2, (point2[0], int(point2[1] + dist_pt1_pt4 * line_length)), line_color,
                 line_thickness)  # point2 to bottom

        cv2.line(src, point3, (int(point3[0] - dist_pt1_pt2 * line_length), point3[1]), line_color,
                 line_thickness)  # point3 to left
        cv2.line(src, point3, (point3[0], int(point3[1] - dist_pt1_pt4 * line_length)), line_color,
                 line_thickness)  # point3 to top

        cv2.line(src, point4, (int(point4[0] + dist_pt1_pt2 * line_length), point4[1]), line_color,
                 line_thickness)  # point4 to right
        cv2.line(src, point4, (point4[0], int(point4[1] - dist_pt1_pt4 * line_length)), line_color,
                 line_thickness)  # point4 to top

    return src


while video.isOpened():
    ret, img = video.read()
    if ret:
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        lower_yellow = np.array([8, 105, 232])
        upper_yellow = np.array([18, 153, 247])

        mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

        result = cv2.bitwise_and(img, img, mask=mask)

        g_result = cv2.GaussianBlur(mask, (7, 7), 5)
        canny = cv2.Canny(g_result, 150, 200, 0)
        cnt = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if len(cnt[0]) > 15:

            for i in cnt[0]:

                for e in i:
                    x = int(np.average(e[0][0]))
                    y = int(np.average(e[0][1]))

            img = draw_rect(img, (x - 100, y), (x + 100, y + 150), "Circle", font=cv2.FONT_ITALIC, line=True,
                            line_color=(0, 0, 255), rect_color=(0, 255, 0), line_rect_dst=15)

        cv2.imshow("Orange Circles", img)

        key = cv2.waitKey(1)
        if key in [13, 27, 32, 113]:
            break
    else:
        break
cv2.destroyAllWindows()
