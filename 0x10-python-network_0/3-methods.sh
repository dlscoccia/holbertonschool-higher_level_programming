#!/bin/bash
# allaword methods
curl -sI "$1" | cut -d' ' -f2- | grep OPTIONS