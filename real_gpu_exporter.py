from prometheus_client import start_http_server, Gauge
import subprocess
import time

gpu_util = Gauge("gpuflow_gpu_utilization_percent", "GPU utilization percent")
mem_used = Gauge("gpuflow_gpu_memory_used_mb", "GPU memory used in MB")
mem_total = Gauge("gpuflow_gpu_memory_total_mb", "GPU memory total in MB")
gpu_temp = Gauge("gpuflow_gpu_temperature_celsius", "GPU temperature Celsius")
power_draw = Gauge("gpuflow_gpu_power_draw_watts", "GPU power draw watts")
idle_alert = Gauge("gpuflow_idle_gpu_alert", "1 if GPU utilization is below 20 percent")

def read_gpu():
    cmd = [
        "nvidia-smi",
        "--query-gpu=utilization.gpu,memory.used,memory.total,temperature.gpu,power.draw",
        "--format=csv,noheader,nounits"
    ]

    output = subprocess.check_output(cmd).decode("utf-8").strip()
    first_gpu = output.splitlines()[0]

    util, used, total, temp, power = [x.strip() for x in first_gpu.split(",")]

    util = float(util)
    used = float(used)
    total = float(total)
    temp = float(temp)
    power = float(power)

    gpu_util.set(util)
    mem_used.set(used)
    mem_total.set(total)
    gpu_temp.set(temp)
    power_draw.set(power)
    idle_alert.set(1 if util < 20 else 0)

if __name__ == "__main__":
    start_http_server(8000)
    print("GPUFlow real GPU exporter running on port 8000")

    while True:
        try:
            read_gpu()
        except Exception as e:
            print(f"Error reading GPU: {e}")
        time.sleep(5)
