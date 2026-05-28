# GPUFlow v0.1 — GPU Utilization Intelligence Dashboard

GPUFlow v0.1 is a real-time GPU utilization intelligence dashboard built on AWS.

It collects NVIDIA GPU telemetry from an AWS GPU instance, exposes the metrics through a Python Prometheus exporter, stores them in Prometheus, and visualizes them in Grafana.

## Project Goal

The goal of this project is to understand GPU utilization behavior and detect early signs of underused or idle GPU infrastructure.

Expensive GPU compute is often allocated but not always productively used. GPUFlow v0.1 is the first step toward identifying that waste.

## Architecture

```text
AWS g4dn GPU Instance
        ↓
NVIDIA T4 GPU
        ↓
nvidia-smi
        ↓
Python GPU Exporter
        ↓
Prometheus
        ↓
Grafana
        ↓
GPUFlow Dashboard
