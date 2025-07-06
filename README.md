# HPE CTY 2025 – HPCM Logs with Grafana Loki & VictoriaLogs

This project is developed as part of the **HPE CTY 2025 initiative**, focused on implementing **log observability and visualization** at scale for HPE's massive server infrastructure. Named **HPCM Logs**, the solution is designed to enable efficient collection, processing, aggregation, and querying of logs using open-source observability tools like **Fluent Bit**, **Apache Kafka**, **Logstash**, **Grafana Loki**, **VictoriaLogs**, and **Grafana**.

---

## 🧩 Project Architecture Overview

Logs from various sources are streamed through a pipeline of industry-standard tools to ensure scalability, reliability, and easy visualization:

1. **[Fluent Bit](https://fluentbit.io/)** – Lightweight log collector and forwarder  
2. **[Apache Kafka](https://kafka.apache.org/)** – Message queue for buffering and scalable distribution  
3. **[Logstash](https://www.elastic.co/logstash)** – Optional log processor and modifier  
4. **[Grafana Loki](https://grafana.com/oss/loki/)** / **[VictoriaLogs](https://docs.victoriametrics.com/victorialogs/)** – Log aggregation and storage backends  
5. **[Grafana](https://grafana.com/)** – Dashboard for querying and visualizing logs  

---

## 📁 Folder Structure

```plaintext
.
├── fluentbit/            # Fluent Bit configuration files
├── logstash/             # Logstash pipeline configuration
├── generators/           # Files for generating fake data for testing
└── README.md             # This file





---

## ⚙️ Prerequisites

Ensure the following are installed on any **Linux-based OS**:

- [Fluent Bit](https://fluentbit.io/)
- [Apache Kafka](https://kafka.apache.org/)
- [Logstash](https://www.elastic.co/logstash)
- [Grafana Loki](https://grafana.com/oss/loki/) or [VictoriaLogs](https://docs.victoriametrics.com/victorialogs/)
- [Grafana](https://grafana.com/)

---

## 🚀 Getting Started

> 📝 **Note:**  
> The exact commands may vary depending on where your config files and binaries are stored. Adjust paths accordingly.

Follow this sequence to run the log processing pipeline:

### 1. ✅ Start Fluent Bit

Navigate to the directory where `fluent-bit.conf` is located (e.g., `./fluentbit/`):

```bash
fluent-bit -c ./fluentbit/fluent-bit.conf
