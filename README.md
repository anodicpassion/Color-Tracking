# Color-Tracking!

## Breif

<div align = "center">
<img alt="Screenshot 2023-03-18 at 6 42 26 PM" src="https://user-images.githubusercontent.com/117884284/226115124-94a7f756-c29b-4100-9397-acea197a5c45.png" width=375 height=224 align="center" />
<img alt="Screenshot 2023-03-18 at 6 41 45 PM" src="https://user-images.githubusercontent.com/117884284/226115151-d3d22f4e-8612-4c78-b3c6-546e4fae43b3.png" width=375 height=224  align="center"/>
</div>
<h4 align="center">
This project tracks the orange circles in the video using color tracking and contours detections.
</h4>

## Installation

You can simply install the project with the help of `requirements.txt` included. <br>Just use the following commands:
<br><br>
1] `https://github.com/pratik-suhas-pawar/Color-Tracking.git`
<br>
2] `pip install -r requirements.txt`

## How does it works

The main aim is to detect orange circles in the given video. To begin with, we will detect the color orange.
<br>
*Step 1]* Converting video frame into HSV Color space.
<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;`cv2.cvtColor(src, cv2.COLOR_BGR2HSV)`
<br>
*Step 2]* Getting the desired color and creating its mask.
<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;`cv2.inRange(src, lower, upper)`
<br>
<br>
Nextly, we will detect the edges and find the contors.
<br>
*Step 3]* Bluring the video frame
<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;`cv2.GaussianBlur(src, kernel, sigmaX)`
<br>
*Step 4]* Finding the edges
<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;`cv2.Canny(src, thresh_1, thresh_2, edges)`
<br>
<br>
Averaging x and y coordinates and draw rectangle
<br>
*Step 5]* Drewing the rectangle
<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;`cv2.rectangle(src, pt_1, pt_2, color, thickness)`

