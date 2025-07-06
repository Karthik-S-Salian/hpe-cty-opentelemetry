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


🚀 Getting Started
📝 Note:
The exact commands may vary depending on where your config files and binaries are stored. Adjust paths accordingly.

Follow this sequence to run the log processing pipeline:

1.Start Fluent Bit
Navigate to the directory where fluent-bit.conf is located (e.g., ./fluentbit/):

bash
Copy
Edit
fluent-bit -c ./fluentbit/fluent-bit.conf
This collects logs and pushes them into Kafka topics as defined in the configuration.

2.Start Apache Kafka
Start Zookeeper first, then Kafka:

bash
Copy
Edit
# Start Zookeeper
bin/zookeeper-server-start.sh config/zookeeper.properties

# Start Kafka
bin/kafka-server-start.sh config/server.properties
Replace bin/ and config/ with your local Kafka installation paths if different.

3. ✅ Start Logstash (Optional)
Start Logstash with the provided configuration:

bash
Copy
Edit
logstash -f ./logstash/logstash.conf
Logstash is optional but helpful for parsing, modifying, or enriching logs before storing.

4. ✅ Start Log Aggregator
Choose one of the following options depending on your preferred backend:

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
5. ✅ Start Grafana
Launch Grafana in your browser (typically at http://localhost:3000).

Add Loki or VictoriaLogs as a data source

Import or create dashboards from the /dashboards folder

