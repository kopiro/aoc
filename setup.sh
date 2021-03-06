#!/bin/bash

if [ -z "$AOC_SESSION" ]; then
    echo "Please provide your cookie as AOC_SESSION"
    exit 1
fi

if [ -z "$1" ]; then
    echo "Please provide your year"
    exit 1
fi

if [ -z "$2" ]; then
    echo "Please provide your day"
    exit 1
fi

year=$1
day=$2

download_input() {
    year=$1
    day=$2
    mkdir -p "./${year}/${day}"
    if [ ! -f "./${year}/${day}/input.html" ]; then
        echo "Downloading HTML input ${year}/${day}..."
        curl -s "https://adventofcode.com/${year}/day/${day}" \
            -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36" \
            -o "./${year}/${day}/input.html"
    fi
    if [ ! -f "./${year}/${day}/input.txt" ]; then
        echo "Downloading TXT input ${year}/${day}..."
        curl -s "https://adventofcode.com/${year}/day/${day}/input" \
            -o "./${year}/${day}/input.txt" \
            --cookie "session=${AOC_SESSION}"
    fi
    cp ./template/solution.py "./${year}/${day}/solution.py"
}

download_input $year $day