import psutil

def collect_ram_metrics() -> dict:
    """Extracts memory allocation and availability breakdown."""
    ram = psutil.virtual_memory()
    return {
        "total_bytes": ram.total,
        "used_bytes": ram.used,
        "available_bytes": ram.available,
        "utilization_percent": ram.percent,
        "available_mb": round(ram.available / (1024 * 1024), 2),
    }