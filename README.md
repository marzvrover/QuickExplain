# QuickExplain

Quick Explain is a simple tool explain complex topics.

## Requirements

You can find python requirements in `requirements.txt`.

On Linux `glibc` version 2.32 or later is required.

You'll need at least 16gb of RAM for the default model.

## Run

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/marzvrover/QuickExplain)

Install dependencies: `pip install -r requirements.txt`
Download LLM model: `llm -m <model_name> "respond with: success"` with default model: `llm -m wizardlm-13b-v1 "respond with: success"`
Run server: `./quickexplain.py`
