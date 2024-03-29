# QuickExplain

Quick Explain is a simple tool to explain complex topics.

## Requirements

You can find python requirements in `requirements.txt`.

On Linux `glibc` version 2.32 or later is required.

You'll need at least 16gb of RAM for the default model. More/faster CPUs shoule mean faster response times.

## Run

### GitHub Codespaces

The `postCreateCommand` runs the [`.devcontainer/scripts/postcreate.sh`](https://github.com/marzvrover/QuickExplain/blob/main/.devcontainer/scripts/postcreate.sh) script which installs python dependencies and downloads the default model, so you only need to run the sever.
```shell
./quickexplain.py
```

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/marzvrover/QuickExplain)

### Locally

Install dependencies: `pip install -r requirements.txt`

Download LLM model: `llm -m <model_name> "respond with: success"` with default model: `llm -m wizardlm-13b-v1 "respond with: success"`

Run server: `./quickexplain.py`

```shell
pip install -r requirements.txt
llm -m wizardlm-13b-v1 "respond with: success"
./quickexplain.py
```

## Environment variables

| Variable                   | Description                                     | Default           |
| -------------------------- | ----------------------------------------------- | ----------------- |
| `QUICKEXPLAIN_DEBUG`       | Enable debug mode                               | `False`           |
| `QUICKEXPLAIN_MODEL`       | LLM model name                                  | `wizardlm-13b-v1` |
| `QUICKEXPLAIN_TOKEN_LIMIT` | Maximum number of tokens to ingestible by model | `2048`            |
| `QUICKEXPLAIN_HOST`        | Host to listen on                               | `localhost`       |
| `QUICKEXPLAIN_PORT`        | Port to listen on                               | `8080`            |
