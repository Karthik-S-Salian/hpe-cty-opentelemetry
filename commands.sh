#!/bin/bash

gnome-terminal -- bash -c "./app/logstash-9.1.2/bin/logstash -f ./logstash/logstash.conf --path.settings ./app/logstash-9.1.2/config/logstash.yml  --path.data ./logstash/data/ --path.logs ./logstash/logs/; exec bash"

gnome-terminal -- bash -c "./app/kafka/bin/kafka-server-start.sh ./app/kafka/config/server.properties; exec bash"

gnome-terminal -- bash -c "fluent-bit -c ./fluentbit/fluentbit.conf; exec bash"

gnome-terminal -- bash -c "/bin/python3 ./generators/fake_logs.py; exec bash"

gnome-terminal -- bash -c "./app/victoria-logs-prod -storageDataPath=victoria-logs-data"


./app/logstash-9.1.2/bin/logstash \
  -f /home/karthikssalian/work/hpe-cty-opentelemetry/logstash/logstash.conf \
  --path.settings /home/karthikssalian/work/hpe-cty-opentelemetry/app/logstash-9.1.2/config \
  --path.data ./logstash/data \
  --path.logs ./logstash/logs