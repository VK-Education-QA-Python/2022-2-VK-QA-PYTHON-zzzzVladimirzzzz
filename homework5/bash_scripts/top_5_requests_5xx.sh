#!/bin/bash
RESULT=$(awk '$9 ~ /^[5]/{print$1}' access.log | uniq -c | sort -k1 | tail -5);echo -e "Топ 5 пользователей по количеству запросов,которые завершились серверной (5xx) ошибкой:\n$RESULT" >> results_bash.txt;
