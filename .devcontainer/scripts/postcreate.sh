#!/usr/bin/env bash
pip install -r requirements.txt
# download model
llm -m $QUICKEXPLAIN_MODEL "respond with: success"
