#!/bin/bash
GET_RESULT=$(awk '{print$6}' access.log | grep -c 'GET'); echo -e "Общее количество GET запросов:\n$GET_RESULT" >> results_bash.txt;
POST_RESULT=$(awk '{print$6}' access.log | grep -c 'POST'); echo -e "Общее количество POST запросов:\n$POST_RESULT" >> results_bash.txt;
PUT_RESULT=$(awk '{print$6}' access.log | grep -c 'PUT'); echo -e "Общее количество PUT запросов:\n$PUT_RESULT" >> results_bash.txt;
HEAD_RESULT=$(awk '{print$6}' access.log | grep -c 'HEAD'); echo -e "Общее количество HEAD запросов:\n$HEAD_RESULT" >> results_bash.txt;
DELETE_RESULT=$(awk '{print$6}' access.log | grep -c 'DELETE'); echo -e "Общее количество DELETE запросов:\n$DELETE_RESULT" >> results_bash.txt;
CONNECT_RESULT=$(awk '{print$6}' access.log | grep -c 'CONNECT'); echo -e "Общее количество CONNECT запросов:\n$CONNECT_RESULT" >> results_bash.txt;
OPTIONS_RESULT=$(awk '{print$6}' access.log | grep -c 'OPTIONS'); echo -e "Общее количество OPTIONS запросов:\n$OPTIONS_RESULT" >> results_bash.txt;
TRACE_RESULT=$(awk '{print$6}' access.log | grep -c 'TRACE'); echo -e "Общее количество TRACE запросов:\n$TRACE_RESULT" >> results_bash.txt;
PATCH_RESULT=$(awk '{print$6}' access.log | grep -c 'PATCH'); echo -e "Общее количество PATCH запросов:\n$PATCH_RESULT" >> results_bash.txt;
