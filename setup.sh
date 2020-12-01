#!/bin/bash

for year in $(seq 2019 "$(date +'%Y')"); do
    for day in $(seq 1 25); do
        if (($(date +'%-d') >= day)) && ((year = $(date +'%Y'))) || ((year != $(date +'%Y'))); then
            mkdir -p "./${year}/${day}"
            if [ ! -f "./${year}/${day}/input.txt" ]; then
                echo "Downloading ${year}/${day}..."
                curl "https://adventofcode.com/${year}/day/${day}/input" \
                    -o "./${year}/${day}/input.txt" \
                    -s \
                    --cookie "session=${AOC_SESSION}"
            fi
        fi
    done
done