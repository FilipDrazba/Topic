#!/bin/bash
docker run -d -p 1883:1883 -p 9001:9001 --name mosquitto eclipse-mosquitto

