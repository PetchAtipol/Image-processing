Bike Detector Using OpenCV
  This project demonstrates how to use OpenCV to detect bikes in a video. The script loads a video file, 
  applies a trained classifier to detect bikes, and displays the video with rectangles drawn around the detected bikes.

Requirements:
  Python 3.x
  OpenCV (cv2)

Installation:
  To install the required Python package, you can use pip: pip install opencv-python 

Usage:
  1.Prepare the Video and Classifier:
    Place your video file in the Bike_Detector/Sample/ directory.
    Ensure the bike detection classifier (two_wheeler.xml) is in the Bike_Detector/Classifier/ directory.

  2.Run the Script:
    You can run the script using Python: python bike_detector.py

Explanation
  -Video Capture: The script uses cv2.VideoCapture to load a video file.
  -Grayscale Conversion: The frames are converted to grayscale for better detection performance.
  -Bike Detection: The CascadeClassifier is used to detect bikes in each frame.
  -Display: Detected bikes are highlighted with rectangles and displayed in a window.
  -Exit: The loop exits when the video ends or the user presses the "e" key.
  
Exiting the Program
  The video will continue to play until it ends or you press the e key to exit.
  
Credits
  OpenCV: The core library used for computer vision tasks.
  
License
  This project is licensed under the MIT License - see the LICENSE file for details.
