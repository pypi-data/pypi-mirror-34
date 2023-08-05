# Library: nftl-slack-tools

This is a tool for Slack API handling.

Source documentation of api is available [here](https://api.slack.com/)

[PyPI project page](https://pypi.org/project/nftl-slack-tools/)


# Installation

```sh
pip install nftl-slack-tools
```

# Usage

```python
    from nftl_slack_tools.client import SlackClient

    slack = SlackClient(token='xoxp-...')
    channel = slack.get_channels_api().create('new_order')

    if channel:
        print('Yupi!')
```

# Deployment how to

Available [here](https://packaging.python.org/tutorials/packaging-projects/)