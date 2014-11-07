#!/bin/bash

echo "Run dashboard api server..."
./venv/bin/activate && ./scripts/manage.py runserver&
echo "Run dashboard server..."
cd ../jchm-dashboard && server&
echo "Build javascript application..."
gulp --gulpfile ../jchm-dashboard/master/gulpfile.js&

