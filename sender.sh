#!/bin/bash

read commit_message -p "Commit message: "
git add -A && git commit -m "Commit message: " && git push
