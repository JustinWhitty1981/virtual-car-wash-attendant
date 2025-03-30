import cv2
import time
from datetime import datetime

class VehicleImageCapture:
    def __init__(self, camera_id=0):
        self.camera = cv2.VideoCapture(camera_id)
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
        
    def capture_image(self):
        """Capture image when vehicle detected"""
        ret, frame = self.camera.read()
        if ret:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"vehicle_{timestamp}.jpg"
            cv2.imwrite(f"./captured_images/{filename}", frame)
            return filename
        return None
    
    def close(self):
        self.camera.release()
