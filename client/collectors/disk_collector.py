import os
import psutil

def collect_disk_metrics() -> dict:
    """Extracts storage capacity and cumulative I/O stats."""
    disk_path = "C:\\" if os.name == "nt" else "/"
    disk = psutil.disk_usage(disk_path)
    disk_io = psutil.disk_io_counters()

    return {
        "mount_point": disk_path,
        "total_bytes": disk.total,
        "used_bytes": disk.used,
        "free_bytes": disk.free,
        "free_gb": round(disk.free / (1024 * 1024 * 1024), 2),
        "utilization_percent": disk.percent,
        "read_bytes": disk_io.read_bytes if disk_io else None,
        "write_bytes": disk_io.write_bytes if disk_io else None,
    }