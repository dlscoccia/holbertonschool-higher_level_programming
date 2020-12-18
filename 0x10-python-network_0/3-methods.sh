#!/bin/bash
# allaword methods
curl -sI "$1" | grep "Allow: " | sed 's/Allow: //'
