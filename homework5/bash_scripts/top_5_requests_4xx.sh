#!/bin/bash
RESULT=$(awk '$9 ~ /^[4]/ { print$1, $7, $9, $10}' access.log | sort -k 4n | tail -5); echo -e "Топ 5 самых больших запросов которые заврешились клиентской (4xx) ошибкой:\n$RESULT" >> results_bash.txt;
