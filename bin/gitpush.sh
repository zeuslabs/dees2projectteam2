#!/bin/sh

if [ -f ~/.bashrc ]; then
    . ~/.bashrc
fi

((
  date +'%Y-%m-%d %X';
  git add .;
  git commit -m "auto git push";
  git push origin master -f;
) >> ./log/collect_$(date '+%Y%m%d').log 2>&1)
