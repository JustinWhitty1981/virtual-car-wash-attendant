class BarrierControl:
    def __init__(self, port="/dev/ttyUSB0"):
        self.port = port
        # In a real system, you would initialize hardware connection here
        self.status = "CLOSED"
        
    def open_barrier(self):
        """Open the entry barrier"""
        # In a real system, send command to physical barrier
        print("Opening barrier...")
        self.status = "OPEN"
        # After a few seconds, close it
        self._schedule_close()
        
    def close_barrier(self):
        """Close the entry barrier"""
        # In a real system, send command to physical barrier
        print("Closing barrier...")
        self.status = "CLOSED"
        
    def _schedule_close(self):
        """Schedule automatic barrier closure after delay"""
        # In a real implementation, use a proper timer or thread
        import threading
        threading.Timer(10.0, self.close_barrier).start()
