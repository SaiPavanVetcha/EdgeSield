import os
import socket
from datetime import datetime, timezone
import psutil

def collect_system_info() -> dict:
    """Extracts host environment runtime metadata."""
    return {
        "hostname": socket.gethostname(),
        "platform": os.name,
        "boot_time_utc": datetime.fromtimestamp(psutil.boot_time(), tz=timezone.utc).isoformat(),
    }