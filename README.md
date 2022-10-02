# events_in_progress

# Intorduction

A Solution to "Events in progress" problem is implemented in python. It reads the data (startTime, endTime) from a json file, called data.json.

# Implementation overview

The solution is a containerized Python application which reads a set of data from a Json file in the following format:

{"VideoPlay":[
    {
        "startTime":"2022‑09‑01 17:45:30.005",
        "endTime":"2022‑09‑01 18:15:30.005"
    }
]
}

# Prerequisites

To install and deploy, you need to have Docker Desktop.

# Configuration steps

Navigate to the root of the project and run the following command to build a docker image:

`docker build -t events_in_progress .`

run the image using the following command:

`docker run  -it -p 8080:8080 -v $(pwd)/:/app events_in_progress:latest`

# Notes

The solution is implemented in python by finding the maximum overlaps between a number of ranges. This will give us an acceptable performance considering the complexity of the solution is O(N Log N) which N is the number of (startTime, endTime) pairs.

# Development considerations

The implementation to find the maximum overlaps is inspired from: https://www.geeksforgeeks.org/maximum-number-of-overlapping-intervals/
