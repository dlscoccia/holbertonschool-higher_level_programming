#!/bin/bash
# allaword methods
curl -si $1 | grep 'Allow:' | cut -d ' ' -f 2-4