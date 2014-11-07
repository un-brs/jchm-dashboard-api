#!/bin/bash

echo "Run dashboard api server..."
. venv/bin/activate
./scripts/manage.py runserver --noreload