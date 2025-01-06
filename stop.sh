#!/bin/bash

kill -9 $(ps aux | grep '[c]elery' | awk '{print $2}')

kill -9 $(ps aux | grep '[f]lask' | awk '{print $2}')
