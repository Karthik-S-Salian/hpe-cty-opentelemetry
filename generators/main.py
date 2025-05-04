from fastapi import FastAPI
from random import randint
import logging

from opentelemetry import metrics, trace
from opentelemetry import _logs as logs
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry.exporter.otlp.proto.grpc._log_exporter import OTLPLogExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource


# --- OpenTelemetry setup ---
resource = Resource(attributes={SERVICE_NAME: "python-opentel-sim"})

# Logging (OTLP gRPC Exporter for Logs)
logs.set_logger_provider(LoggerProvider(resource=resource))
logger_provider = logs.get_logger_provider()
log_exporter = OTLPLogExporter(endpoint="localhost:4317", insecure=True)  # gRPC Endpoint
logger_provider.add_log_record_processor(BatchLogRecordProcessor(log_exporter))

log_handler = LoggingHandler(level=logging.INFO, logger_provider=logger_provider)
logging.getLogger().addHandler(log_handler)
logger = logging.getLogger("opentel-logger")

# Metrics (OTLP gRPC Exporter for Metrics)
metric_exporter = OTLPMetricExporter(endpoint="localhost:4317", insecure=True)  # gRPC Endpoint
metric_reader = PeriodicExportingMetricReader(metric_exporter)
metrics.set_meter_provider(MeterProvider(resource=resource, metric_readers=[metric_reader]))
meter = metrics.get_meter("python-opentel-sim")
request_counter = meter.create_counter("http_requests_total", description="Total HTTP requests")

# --- FastAPI App ---
app = FastAPI(
    title="OpenTelemetry Python Demo",
    description="Generates OpenTelemetry logs and metrics. View logs in Grafana via Loki, and metrics via VictoriaMetrics.",
    version="1.0.0"
)

@app.get("/", tags=["Basic"])
def home():
    request_counter.add(1, {"endpoint": "/"})
    logger.info("Visited home page")
    return {"message": "Welcome to OpenTelemetry Python App!"}

@app.get("/error", tags=["Simulation"])
def error():
    request_counter.add(1, {"endpoint": "/error"})
    logger.error("Simulated error occurred")
    return {"error": "Something went wrong!"}, 500

@app.get("/random", tags=["Simulation"])
def random():
    request_counter.add(1, {"endpoint": "/random"})
    val = randint(0, 100)
    if val > 80:
        logger.warning(f"High value generated: {val}")
    else:
        logger.info(f"Value generated: {val}")
    return {"value": val}

@app.get("/health", tags=["Basic"])
def health():
    request_counter.add(1, {"endpoint": "/health"})
    logger.info("Health check OK")
    return {"status": "healthy"}
