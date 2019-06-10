#!/bin/sh

if [ -f ~/.bashrc ]; then
    . ~/.bashrc
fi

((

  echo '         '
  echo '=================================================='
  echo '[[start task]]'
  date +'%Y-%m-%d %X';
  python ./Collect/main.py;

  echo '[[git run]]'
  date +'%Y-%m-%d %X';
  git add .;
  git commit -m "auto git push";
  git push origin master -f;

  echo '[[end task]]'
  date +'%Y-%m-%d %X';

) >> ./log/collect_$(date '+%Y%m%d%H').log 2>&1)
