#!/bin/sh

if [ -f ~/.bashrc ]; then
    . ~/.bashrc
fi

((
  ./Collect/python main.py;
  git add .;
  git commit -m "update";
  git push
) > ./log/collect_$(date '+%Y%m%d%H%M%S').log 2>&1)
