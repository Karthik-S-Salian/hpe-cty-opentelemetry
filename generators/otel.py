import time
import random
import logging
from datetime import datetime
from opentelemetry import _logs as logs
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.exporter.otlp.proto.grpc._log_exporter import OTLPLogExporter
from opentelemetry.sdk.resources import Resource, SERVICE_NAME

# ------------------- OTEL Logger Setup -------------------
resource = Resource(attributes={
    SERVICE_NAME: "stateful-log-simulator",
    "service.version": "1.0.0",
    "deployment.environment": "dev",
    "cloud.region": "ap-south-1",
    "cloud.zone": "zone-3",
    "host.name": "sim-host-01",
    "team": "observability",
    "component": "state-machine",
    "application": "monitoring-suite",
})

provider = LoggerProvider(resource=resource)
logs.set_logger_provider(provider)

exporter = OTLPLogExporter(endpoint="localhost:4318", insecure=True)
processor = BatchLogRecordProcessor(exporter)
provider.add_log_record_processor(processor)

otel_handler = LoggingHandler(level=logging.NOTSET, logger_provider=provider)
logger = logging.getLogger("state-logger")
logger.setLevel(logging.INFO)
logger.addHandler(otel_handler)

# ------------------- State Simulation -------------------
states = ["INITIALIZING", "RUNNING", "DEGRADED", "ERROR", "RECOVERING"]
services = ["auth-service", "payment-gateway", "inventory-api", "notification-engine"]
state_transitions = {
    "INITIALIZING": ["RUNNING", "ERROR"],
    "RUNNING": ["RUNNING", "DEGRADED", "ERROR"],
    "DEGRADED": ["RUNNING", "ERROR", "RECOVERING"],
    "ERROR": ["RECOVERING", "INITIALIZING"],
    "RECOVERING": ["RUNNING", "DEGRADED"]
}
severity_map = {
    "INITIALIZING": logging.INFO,
    "RUNNING": logging.INFO,
    "DEGRADED": logging.WARNING,
    "ERROR": logging.ERROR,
    "RECOVERING": logging.INFO
}

def simulate_state_transition(current_state):
    return random.choice(state_transitions.get(current_state, ["RUNNING"]))

# ------------------- HTTP Request Simulation -------------------
route_method_map = {
    "/api/login": ["POST"],
    "/api/logout": ["POST"],
    "/api/products": ["GET", "POST"],
    # "/api/products/{id}": ["GET", "PUT", "DELETE"],
    "/api/orders": ["GET", "POST"],
    # "/api/orders/{id}": ["GET", "PATCH", "DELETE"],
    "/api/users": ["GET", "POST"],
    # "/api/users/{id}": ["GET", "PUT", "DELETE"],
    "/api/cart": ["GET", "POST", "DELETE"],
    "/api/reviews": ["GET", "POST"],
    # "/api/reviews/{id}": ["GET", "PUT", "DELETE"],
    "/health": ["GET"],
    "/metrics": ["GET"],
    "/api/admin/stats": ["GET"],
    "/api/admin/feature-toggle": ["GET", "POST"]
}

status_codes = [200, 201, 204, 400, 401, 403, 404, 500, 503]
user_agents = [
    "curl/7.68.0", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "PostmanRuntime/7.29.0", "okhttp/4.9.3", "python-requests/2.27.1"
]

def fill_path_params(path):
    if "{id}" in path:
        return path.replace("{id}", str(random.randint(1, 999)))
    return path

def simulate_http_log(i):
    route_template = random.choice(list(route_method_map.keys()))
    route = fill_path_params(route_template)
    method = random.choice(route_method_map[route_template])
    status = random.choices(status_codes, weights=[50, 10, 5, 10, 5, 3, 5, 5, 7])[0]
    latency = round(random.uniform(10, 800), 2)
    size = random.randint(128, 8192)
    timestamp = datetime.utcnow().isoformat() + "Z"
    user_agent = random.choice(user_agents)
    ip = f"192.168.{random.randint(1, 255)}.{random.randint(1, 255)}"
    trace_id = f"{random.randint(100000, 999999)}-trace"

    severity = logging.INFO if status < 400 else (
        logging.WARNING if status < 500 else logging.ERROR
    )

    logger.log(
        severity,
        f"[{timestamp}] {method} {route} -> {status}",
        extra={
            "iteration": i,
            "http.method": method,
            "http.route": route,
            "http.status_code": status,
            "http.response_size": size,
            "http.latency_ms": latency,
            "http.user_agent": user_agent,
            "client.ip": ip,
            "timestamp": timestamp,
            "trace_id": trace_id,
            "log_type": "http-request",
            "host_ip": "192.168.1.20",
            "env": "dev"
        }
    )

# ------------------- Run Simulation Loop -------------------
if __name__ == "__main__":
    current_state = "INITIALIZING"
    i = 0
    while True:
        i += 1

        # Log a service state
        timestamp = datetime.utcnow().isoformat() + "Z"
        current_service = random.choice(services)
        log_message = f"[{timestamp}] {current_service} state: {current_state}"

        logger.log(
            severity_map[current_state],
            log_message,
            extra={
                "iteration": i,
                "service": current_service,
                "state": current_state,
                "timestamp": timestamp,
                "instance_id": f"{current_service}-{random.randint(1000,9999)}",
                "cpu_usage": round(random.uniform(10.0, 95.0), 2),
                "memory_usage": round(random.uniform(100.0, 1600.0), 2),
                "request_count": random.randint(0, 200),
                "uptime_seconds": i,
                "log_type": "state-transition",
                "host_ip": "192.168.1.10",
                "team": "observability",
                "env": "dev"
            }
        )

        # Log an HTTP request
        simulate_http_log(i)

        # Transition to the next state
        current_state = simulate_state_transition(current_state)
        print(f"sent {i}")
        time.sleep(1)
