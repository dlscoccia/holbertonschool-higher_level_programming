#!/bin/bash
# script that takes in a URL as an argumenta and sends a GET
curl -sX GET -H "X-HolbertonSchool-User-Id: 98" "$1"
