import torch
import time

print("Starting GPU workload")
print("CUDA available:", torch.cuda.is_available())
print("GPU:", torch.cuda.get_device_name(0))

x = torch.randn(8000, 8000, device="cuda")

for i in range(60):
    y = x @ x
    print(f"Iteration {i+1}/60")
    time.sleep(1)

print("Done")
