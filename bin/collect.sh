#!/bin/sh

if [ -f ~/.bashrc ]; then
    . ~/.bashrc
fi

((

  echo 'start run'
  python ./Collect/main.py;
  date +'%Y-%m-%d %X';

  git add .;
  git commit -m "auto git push";
  git push origin master -f;
  date +'%Y-%m-%d %X';

) >> ./log/collect_$(date '+%Y%m%d%H').log 2>&1)
