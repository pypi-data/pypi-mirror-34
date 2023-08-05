=====
Usage
=====

To use the command line interface open your terminal
in the target repository directory then run

    pull_webhook .

The complete command is following:

    pull_webhook --remote <remote-name> --branch <branch-name> --port <port-number> "repository directory path"

By default the following parameters are used:

    pull_webhook --remote origin --branch master --port 8888

To use Pull Webhook in a project::

    import pull_webhook
