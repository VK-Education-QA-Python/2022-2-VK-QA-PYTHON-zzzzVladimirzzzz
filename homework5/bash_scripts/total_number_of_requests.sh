#!/bin/bash
RESULT=$(awk '{print$6}' access.log | grep -c 'POST\|GET\|DELETE\|PATCH\|PUT\|HEAD\|CONNECT\|OPTIONS\|TRACE'); echo -e "Общее количество запросов:\n$RESULT" >> results_bash.txt
