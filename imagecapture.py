import cv2
import time
import os
import shutil
from datetime import datetime

class VehicleImageCapture:
    def __init__(self, camera_id=0):
        self.camera = None
        self.use_sample_images = True
        self.sample_images = [
            "vehicle_20250330_161543.jpg",
            "vehicle_20250330_162116.jpg"
        ]
        self.current_sample_index = 0
        
        # Try to initialize camera, but fall back to sample images if it fails
        try:
            self.camera = cv2.VideoCapture(camera_id)
            if self.camera.isOpened():
                self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
                self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
                # Test if we can actually read from the camera
                ret, frame = self.camera.read()
                if ret:
                    self.use_sample_images = False
                    print("Camera initialized successfully")
                else:
                    print("Camera opened but cannot read frames, using sample images")
                    self.camera.release()
                    self.camera = None
            else:
                print("Cannot open camera, using sample images")
                self.camera = None
        except Exception as e:
            print(f"Camera initialization failed: {e}, using sample images")
            self.camera = None
        
    def capture_image(self):
        """Capture image when vehicle detected"""
        if not self.use_sample_images and self.camera:
            # Use real camera
            ret, frame = self.camera.read()
            if ret:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"vehicle_{timestamp}.jpg"
                cv2.imwrite(f"./captured_images/{filename}", frame)
                return filename
        
        # Use sample images for demonstration
        if self.sample_images:
            # Copy one of the existing sample images with a new timestamp
            source_file = self.sample_images[self.current_sample_index]
            source_path = f"./captured_images/{source_file}"
            
            if os.path.exists(source_path):
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"vehicle_{timestamp}.jpg"
                dest_path = f"./captured_images/{filename}"
                
                # Copy the sample image with new filename
                shutil.copy2(source_path, dest_path)
                
                # Cycle through sample images
                self.current_sample_index = (self.current_sample_index + 1) % len(self.sample_images)
                
                return filename
        
        return None
    
    def close(self):
        if self.camera:
            self.camera.release()
