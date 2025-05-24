#!/bin/bash

gnome-terminal -- bash -c "/usr/share/logstash/bin/logstash -f /home/karthikssalian/work/hpe/logstash/logstash.conf --path.settings /etc/logstash --path.data /home/karthikssalian/work/hpe/logstash/data/ --path.logs /home/karthikssalian/work/hpe/logstash/logs/; exec bash"

gnome-terminal -- bash -c "/usr/local/kafka/bin/kafka-server-start.sh /usr/local/kafka/config/server.properties; exec bash"

gnome-terminal -- bash -c "/opt/fluent-bit/bin/fluent-bit -c ~/work/hpe/fluentbit/fluentbit.conf; exec bash"

gnome-terminal -- bash -c "/bin/python3 /home/karthikssalian/work/hpe/generators/fake_logs.py; exec bash"