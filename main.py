from dotenv import load_dotenv
# Load environment variables from .env file
import os
import time
from flask import Flask, render_template, request, jsonify
from imagecapture import VehicleImageCapture
from mmllm import VehicleAnalyzer
from decision import EntryDecisionSystem
from barriercontrol import BarrierControl

app = Flask(__name__)

# Initialize components
camera = VehicleImageCapture(camera_id=0)
analyzer = VehicleAnalyzer()
decision_system = EntryDecisionSystem(analyzer)
barrier = BarrierControl()

# Ensure directory exists
os.makedirs("./captured_images", exist_ok=True)

@app.route('/')
def index():
    """Main interface page"""
    return render_template('index.html')

@app.route('/capture', methods=['POST'])
def capture_and_analyze():
    """Endpoint to trigger capture and analysis"""
    # Capture image
    image_path = camera.capture_image()
    if not image_path:
        return jsonify({"error": "Failed to capture image"}), 500
    
    full_path = os.path.join("./captured_images", image_path)
    
    # Process the image
    result = decision_system.process_vehicle(full_path)
    
    # Control barrier based on decision
    if result["decision"] == "ALLOW":
        barrier.open_barrier()
    
    return jsonify({
        "image": image_path,
        "decision": result["decision"],
        "analysis": result["analysis"]
    })

@app.route('/override', methods=['POST'])
def override():
    """Endpoint for manual override"""
    data = request.json
    
    result = decision_system.override_decision(
        data["image_path"],
        data["decision"],
        data["reason"],
        data["operator_id"]
    )
    
    if data["decision"] == "ALLOW":
        barrier.open_barrier()
    
    return jsonify({"status": "success", "decision": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
