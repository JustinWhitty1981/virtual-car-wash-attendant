import requests
import base64
import json
import os
from openai import OpenAI

class VehicleAnalyzer:
    def __init__(self, api_key=os.environ.get("OPENAI_API_KEY")):
        self.client = OpenAI(api_key=api_key)
        
    def analyze_vehicle(self, image_path):
        """Use multi-modal LLM to analyze vehicle image"""
        with open(image_path, "rb") as image_file:
            base64_image = base64.b64encode(image_file.read()).decode('utf-8')
        
        response = self.client.chat.completions.create(
            model="gpt-4-vision-preview",  # Use the appropriate multi-modal model
            messages=[
                {
                    "role": "system",
                    "content": """You are a car wash safety and compatibility analyzer. 
                    Assess if vehicles should be allowed into the car wash based on:
                    1. Size (too tall/wide vehicles not allowed)
                    2. Modifications (lifted trucks, extra-wide vehicles not allowed)
                    3. Visible damage or loose parts that might be worsened by washing
                    4. Convertibles with soft tops (need special handling)
                    5. Vehicles with roof attachments like bike racks or cargo boxes (not allowed)
                    
                    Provide a clear YES/NO decision with reasoning."""
                },
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Analyze this vehicle and determine if it should be allowed into the automatic car wash."},
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                    ]
                }
            ],
            max_tokens=300
        )
        
        analysis = response.choices[0].message.content
        decision = self._extract_decision(analysis)
        
        return {
            "analysis": analysis,
            "decision": decision,
            "timestamp": time.time()
        }
    
    def _extract_decision(self, analysis):
        """Extract YES/NO decision from analysis text"""
        analysis_lower = analysis.lower()
        
        # Simple decision extraction - could be improved with more robust parsing
        if "not allowed" in analysis_lower or "should not be allowed" in analysis_lower or "no, " in analysis_lower:
            return "DENY"
        elif "can be allowed" in analysis_lower or "should be allowed" in analysis_lower or "yes, " in analysis_lower:
            return "ALLOW"
        else:
            # Default to requiring human review if unclear
            return "REVIEW"
