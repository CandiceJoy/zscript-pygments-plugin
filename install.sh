#!/bin/bash
PYTHON=$(command -v python3)

if [ -z "$PYTHON" ]; then
	PYTHON=$(command -v python)
fi

if [ -z "$PYTHON" ]; then
	echo "Cannot find Python"
	exit
else
	echo "Python found at $PYTHON"
fi

sudo "$PYTHON" setup.py build
sudo "$PYTHON" setup.py install
