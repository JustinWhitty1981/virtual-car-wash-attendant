class EntryDecisionSystem:
    def __init__(self, analyzer, log_file="car_wash_entries.log"):
        self.analyzer = analyzer
        self.log_file = log_file
        
    def process_vehicle(self, image_path):
        """Process a vehicle and decide whether to allow entry"""
        # Analyze the vehicle
        result = self.analyzer.analyze_vehicle(image_path)
        
        # Log the decision
        self._log_decision(image_path, result)
        
        return result
    
    def _log_decision(self, image_path, result):
        """Log the decision for auditing purposes"""
        with open(self.log_file, "a") as f:
            log_entry = {
                "image": image_path,
                "timestamp": result["timestamp"],
                "decision": result["decision"],
                "analysis": result["analysis"]
            }
            f.write(json.dumps(log_entry) + "\n")
            
    def override_decision(self, image_path, new_decision, reason, operator_id):
        """Allow manual override by operator"""
        with open(self.log_file, "a") as f:
            log_entry = {
                "image": image_path,
                "timestamp": time.time(),
                "decision": new_decision,
                "analysis": f"MANUAL OVERRIDE by {operator_id}: {reason}",
                "override": True
            }
            f.write(json.dumps(log_entry) + "\n")
        
        return new_decision
