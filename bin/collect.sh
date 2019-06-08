#!/bin/sh

if [ -f ~/.bashrc ]; then
    . ~/.bashrc
fi

((
  python ./Collect/main.py;
  git add .;
  git commit -m "update";
  git push
) > ./log/collect_$(date '+%Y%m%d%H%M%S').log 2>&1)
