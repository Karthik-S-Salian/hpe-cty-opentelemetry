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


⚙️ Prerequisites
Before running the pipeline, ensure the following are installed:

Any Linux-based OS

Fluent Bit

Apache Kafka

Logstash

Grafana Loki / VictoriaLogs

Grafana


🚀 Getting Started
📝 Note:
The exact commands may vary depending on where your config files and binaries are stored. Adjust file paths accordingly when running each service.

Follow this sequence to start the full log pipeline:

1. Start Fluent Bit
Navigate to the folder where fluent-bit.conf is located (see /fluentbit).

This config defines which logs to collect and the Kafka topics to send them to.

bash
Copy
Edit
fluent-bit -c ./fluentbit/fluent-bit.conf
2. Start Apache Kafka
Make sure Zookeeper is running before Kafka.

bash
Copy
Edit
# Example for Zookeeper
bin/zookeeper-server-start.sh config/zookeeper.properties

# Example for Kafka
bin/kafka-server-start.sh config/server.properties
⚠️ Replace bin/ and config/ with your local paths if different.

3. Start Logstash
The pipeline config (logstash.conf) is available under /logstash.

This step is optional but useful for transforming or enriching logs before storage.

bash
Copy
Edit
logstash -f ./logstash/logstash.conf
4. Start Log Aggregator
Choose one backend below:

Option A: Grafana Loki
bash
Copy
Edit
./loki -config.file=./loki/loki-config.yaml
Option B: VictoriaLogs
bash
Copy
Edit
./vmlogs-prod -config=./vmlogs/vmlogs.yaml
5. Start Grafana
Log in via browser (typically at http://localhost:3000)

Add Loki or VictoriaLogs as a data source

Use or import dashboards from the /dashboards folder
