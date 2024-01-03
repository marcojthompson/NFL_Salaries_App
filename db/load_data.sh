#!/bin/bash

folder_path=""
table_name="player_cap_hits"

for file in "$folder_path"/*.csv; do
    mysql -u admin -p********** --local-infile=1 -e "
        USE NFL_PLAYER_SALARY_DATA;
        LOAD DATA LOCAL INFILE '$file'
        INTO TABLE $table_name
        FIELDS TERMINATED BY ','
        ENCLOSED BY '\"'
        LINES TERMINATED BY '\n'
        IGNORE 1 ROWS;
    "
done