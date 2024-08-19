import cv2

# Open the video file
cap = cv2.VideoCapture("Bike_Detector/Sample/two_wheeler2.mp4")

# Load the Haar Cascade for bike detection
bike_cascade = cv2.CascadeClassifier("Bike_Detector/Classifier/two_wheeler.xml")

# Parameters for processing
scaleFactor = 1.1
minNeighbors = 0
resize_factor = 0.5  # Resize factor to speed up processing
frame_skip = 2  # Skip every n frames

frame_count = 0

# Process and display the video
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1
    if frame_count % frame_skip != 0:
        continue

    # Resize the frame to speed up processing
    small_frame = cv2.resize(frame, None, fx=resize_factor, fy=resize_factor)
    
    # Convert to grayscale
    gray_img = cv2.cvtColor(small_frame, cv2.COLOR_BGR2GRAY)
    
    # Detect bikes
    bike_detect = bike_cascade.detectMultiScale(gray_img, scaleFactor=scaleFactor, minNeighbors=minNeighbors)
    
    # Draw rectangles around detected bikes
    for (x, y, w, h) in bike_detect:
        x = int(x / resize_factor)
        y = int(y / resize_factor)
        w = int(w / resize_factor)
        h = int(h / resize_factor)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness=5)
    
    # Display the frame
    cv2.imshow("Output", frame)
    
    if cv2.waitKey(48) & 0xFF == ord("e"):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
