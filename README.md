# HPE CTY 2025 – HPCM Logs with Grafana Loki & VictoriaLogs

This project is developed as part of the **HPE CTY 2025 initiative**, focused on implementing **log observability and visualization** at scale for HPE's massive server infrastructure. Named **HPCM Logs**, the solution is designed to enable efficient collection, processing, aggregation, and querying of logs using open-source observability tools like **Fluent Bit**, **Apache Kafka**, **Logstash**, **Grafana Loki**, **VictoriaLogs**, and **Grafana**.

---

## 🧩 Project Architecture Overview

Logs from various sources are streamed through a pipeline of industry-standard tools to ensure scalability, reliability, and easy visualization:

1. **Fluent Bit** – Lightweight log collector
2. **Apache Kafka** – Message queue for buffering & scalable distribution
3. **Logstash** – Optional log processor/modifier
4. **Grafana Loki / VictoriaLogs** – Log aggregation and storage backends
5. **Grafana** – Dashboard for querying and visualizing logs

---

## 📁 Folder Structure

```plaintext
.
├── fluentbit/            # Fluent Bit configuration files
├── logstash/             # Logstash pipeline configuration
├── generators/           # Fiels for creating fake data
└── README.md             # This file


Before running the pipeline, ensure the following are installed:

Linux-based OS (any distribution)

Fluent Bit – lightweight log collector and forwarder (official site) 
github.com
docs.aws.amazon.com
+7
fluentbit.io
+7
github.com
+7

Apache Kafka – scalable message queue

Logstash – optional log processor for transforming and enriching logs

Choose one:

Grafana Loki – log aggregation compatible with Prometheus-like queries

or

VictoriaLogs – efficient, high-performance log storage solution 
youtube.com
+10
docs.victoriametrics.com
+10
reddit.com
+10

Grafana – dashboards and log query interface
