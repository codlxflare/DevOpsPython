#!/bin/bash
echo "Building the application..."
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest tests/
