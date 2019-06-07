#!/bin/sh

if [ -f ~/.bashrc ]; then
    . ~/.bashrc
fi

((
  cd ./Collect/ && \
  python main.py
) > ./log/collect_$(date '+%Y%m%d').log 2>&1)
