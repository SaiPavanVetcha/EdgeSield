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

    sensors_battery = psutil.sensors_battery()
    if sensors_battery is not None:
        battery_info["present"] = True
        battery_info["percent"] = round(sensors_battery.percent, 2)
        battery_info["power_plugged"] = sensors_battery.power_plugged

    bat_nodes = glob.glob("/sys/class/power_supply/BAT*")
    if bat_nodes:
        bat_path = bat_nodes[0]
        battery_info["present"] = True

        energy_design = _read_sysfs_int(os.path.join(bat_path, "energy_full_design"))
        energy_full = _read_sysfs_int(os.path.join(bat_path, "energy_full"))
        charge_design = _read_sysfs_int(os.path.join(bat_path, "charge_full_design"))
        charge_full = _read_sysfs_int(os.path.join(bat_path, "charge_full"))

        design_val = energy_design if energy_design is not None else charge_design
        full_val = energy_full if energy_full is not None else charge_full

        if design_val and full_val and design_val > 0:
            health = round((full_val / design_val) * 100, 2)
            battery_info["design_capacity_raw"] = design_val
            battery_info["full_charge_capacity_raw"] = full_val
            battery_info["health_percentage"] = min(health, 100.0)

    return battery_info