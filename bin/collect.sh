#!/bin/sh

if [ -f ~/.bashrc ]; then
    . ~/.bashrc
fi

((
  python ./Collect/main.py;
  date +'%Y-%m-%d %X';
#  git add .;
#  git commit -m "update";
#  git push;
  date +'%Y-%m-%d %X';
) > ./log/collect_$(date '+%Y%m%d%H%M%S').log 2>&1)
