#!/bin/bash
ARCHIVE="zscript-plugin.tar.gz"

if [ -e "$ARCHIVE" ]; then
	rm "$ARCHIVE"
fi

tar --exclude="venv" --exclude="build" --exclude="dist" --exclude="ZScriptPlugin.egg-info" --exclude="*.tar.gz" --exclude=".idea" -czvf "$ARCHIVE" .
