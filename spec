---------|---------|---------|---------|---------|---------|---------|---------|
$ cacli
┌─────────────────────────────┐
│ (C)loud (A)nnotations (CLI) │
│ version 1.1.0               │
└─────────────────────────────┘

Usage: cacli <command>

where <command> is one of:
  init                   Interactively create a config.yaml file
  train                  Start a training run
  list                   List all training runs

  progress <model-id>    Monitor the progress of a training run
  logs <model-id>        Monitor the logs of a training run
  info <model-id>        Get model information, like output path
  cancel <model-id>      Cancel a training run
  deploy <model-id>      Deploy model as an API endpoint
  download <model-id>    Download all available model formats

  bootstrap <path>       Upload annotations to a bucket
  export                 Download annotations

  debug                  Print config information useful for debuging

Options:
  --profile <user>       Source a separate credentials profile 

cacli <cmd> -h    quick help on <cmd>


---------|---------|---------|---------|---------|---------|---------|---------|


cacli init [--config <config>]

cacli train [<training-zip>]
            [--config <config>]
            [--training-bucket <bucket>]
            [--output-bucket <bucket>]
            [--gpu (k80 | k80x2 | v100 | v100x2)]
            [--steps <steps>]
            [--python <version>]
            [(--tensorflow | --keras | --...) <version>]
            [--local | --docker]

cacli list


cacli progress <model-id>

cacli logs <model-id>

cacli info <model-id>

cacli cancel <model-id>

cacli deploy <model-id>

cacli download <model-id> [<output-path>] [--file <file-or-dir>]


cacli bootstrap <path> [--bucket <bucket>]

cacli export [<output-path>] [--bucket <bucket>]


cacli debug [--config <config>]