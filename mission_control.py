import os
import json
import time
from datetime import datetime

# --- CONFIG ---
MISSION_START = datetime(2026, 5, 1)
WORKSPACE_DIR = os.getcwd()

def calculate_mission_day():
    now = datetime.now()
    delta = now - MISSION_START
    return delta.days + 1

def generate_report():
    print("="*40)
    print("🚀 DNYANESHWAR'S MISSION CONTROL REPORT")
    print("="*40)
    print(f"Current Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Mission Day : {calculate_mission_day()}")
    
    # Simple check for the index.html
    if os.path.exists("index.html"):
        print("✅ Command Dashboard: READY (index.html)")
    else:
        print("❌ Command Dashboard: MISSING")

    print("\n⚡ ELECTRICITY CYCLE STATUS:")
    # Reference Monday for cycle calculation: April 27, 2026
    ref_monday = datetime(2026, 4, 27)
    weeks_passed = (datetime.now() - ref_monday).days // 7
    cycle = (weeks_passed % 3) + 1
    
    shifts = {
        1: "NIGHT WARRIOR (10 PM - 6 AM Double Fuse)",
        2: "MORNING BURST (6 AM - 12 PM Double Fuse)",
        3: "AFTERNOON POWER (12 PM - 6 PM Double Fuse)"
    }
    print(f"Current Cycle: Week {cycle}")
    print(f"Active Shift : {shifts.get(cycle)}")
    print("="*40)

if __name__ == "__main__":
    generate_report()
    print("\n[PRO-TIP] Open index.html in Chrome/Edge to start your execution.")
