import psutil
import datetime
import json
import uvicorn
from fastapi import FastAPI

app = FastAPI(title="Server Check Update API")

def get_server_status():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')
    uptime = datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time())

    return {
        "cpu_usage": cpu_usage,
        "memory_total": memory_info.total,
        "memory_used": memory_info.used,
        "memory_percent": memory_info.percent,
        "disk_total": disk_info.total,
        "disk_used": disk_info.used,
        "disk_percent": disk_info.percent,
        "uptime_seconds": uptime.total_seconds()
    }

@app.get("/")
def read_root():
    return {"message": "Welcome to the Server Check Update API"}

@app.get("/status")
def read_status():
    status = get_server_status()
    return status

@app.get("/metrics")   # <---- ဒီမှာ / ထည့်ပြီး
def read_metrics():
    status = get_server_status()
    metrics = {
        "cpu_usage": status["cpu_usage"],
        "memory_percent": status["memory_percent"],
        "disk_percent": status["disk_percent"],
        "uptime_seconds": status["uptime_seconds"]
    }
    return metrics
