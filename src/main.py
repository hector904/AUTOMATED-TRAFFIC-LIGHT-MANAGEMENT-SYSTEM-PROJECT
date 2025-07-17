import detection
import lights
import mobile
import logging

logging.basicConfig(filename='logs/output.log', level=logging.INFO)

def main():
    lights.setup()
    while True:
        vehicle_count = detection.detect_vehicles()
        logging.info(f"Detected {vehicle_count} toy cars")
        lights.adjust_lights(vehicle_count)
        mobile.send_alert(vehicle_count)

if __name__ == "__main__":
    main()
  
