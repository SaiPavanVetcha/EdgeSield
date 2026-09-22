import glob
import os
import psutil

def _read_sysfs_int(path: str):
    """Safely reads integer nodes from Linux sysfs."""
    try:
        with open(path, "r") as f:
            return int(f.read().strip())
    except (FileNotFoundError, ValueError, PermissionError):
        return None

def collect_battery_metrics() -> dict:
    """Extracts power status, charge levels, and degradation health."""
    battery_info = {
        "present": False,
        "percent": None,
        "power_plugged": None,
        "design_capacity_raw": None,
        "full_charge_capacity_raw": None,
        "health_percentage": None,
    }

    # 1. Fallback via psutil
    sensors_battery = psutil.sensors_battery()
    if sensors_battery is not None:
        battery_info["present"] = True
        battery_info["percent"] = round(sensors_battery.percent, 2)
        battery_info["power_plugged"] = sensors_battery.power_plugged

    # 2. Sysfs inspection
    bat_nodes = glob.glob("/sys/class/power_supply/BAT*") + glob.glob("/sys/class/power_supply/battery")
    if bat_nodes:
        bat_path = bat_nodes[0]
        battery_info["present"] = True

        # Try all common Linux kernel sysfs attribute names
        energy_design = _read_sysfs_int(os.path.join(bat_path, "energy_full_design"))
        energy_full = _read_sysfs_int(os.path.join(bat_path, "energy_full"))
        charge_design = _read_sysfs_int(os.path.join(bat_path, "charge_full_design"))
        charge_full = _read_sysfs_int(os.path.join(bat_path, "charge_full"))
        
        # Fallbacks for embedded Linux systems
        alm_design = _read_sysfs_int(os.path.join(bat_path, "design_capacity"))
        alm_full = _read_sysfs_int(os.path.join(bat_path, "full_charge_capacity"))

        design_val = energy_design or charge_design or alm_design
        full_val = energy_full or charge_full or alm_full

        if design_val and full_val and design_val > 0:
            health = round((full_val / design_val) * 100, 2)
            battery_info["design_capacity_raw"] = int(design_val)
            battery_info["full_charge_capacity_raw"] = int(full_val)
            battery_info["health_percentage"] = float(min(health, 100.0))
            
    # 3. Default fallback values for AC-powered/Virtual machines without a battery
    if not battery_info["present"]:
        battery_info["design_capacity_raw"] = 0
        battery_info["full_charge_capacity_raw"] = 0
        battery_info["health_percentage"] = 100.0

    return battery_info