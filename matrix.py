import cv2

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    if not success:
        break

    # Resize for consistency
    frame = cv2.resize(frame, (400, 300))

    # Create mirror variations
    mirror1 = cv2.flip(frame, 1)   # Horizontal flip
    mirror2 = cv2.flip(frame, 0)   # Vertical flip
    mirror3 = cv2.flip(frame, -1)  # Both flips
    mirror4 = frame                # Original frame

    # Create a 2x2 matrix layout
    row1 = cv2.hconcat([mirror1, mirror2])
    row2 = cv2.hconcat([mirror3, mirror4])
    matrix = cv2.vconcat([row1, row2])

    cv2.imshow("Mirror Clone Matrix - Live", matrix)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
