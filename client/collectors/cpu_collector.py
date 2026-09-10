import psutil

def collect_cpu_metrics() -> dict:
    """Extracts CPU utilization, core metrics, and clock speed."""
    cpu_freq = psutil.cpu_freq()
    return {
        "utilization_percent": psutil.cpu_percent(interval=1.0),
        "core_utilization_percent": psutil.cpu_percent(percpu=True),
        "logical_cores": psutil.cpu_count(logical=True),
        "physical_cores": psutil.cpu_count(logical=False),
        "frequency_current_mhz": round(cpu_freq.current, 2) if cpu_freq else None,
        "frequency_max_mhz": round(cpu_freq.max, 2) if cpu_freq else None,
    }