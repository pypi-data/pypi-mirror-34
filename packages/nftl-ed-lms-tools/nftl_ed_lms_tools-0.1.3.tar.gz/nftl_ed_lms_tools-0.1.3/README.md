# Library: nftl-ed-lms-tools

This is a tool for Ed LMS API handling.

Source documentation of api is available [here](http://developer.edapp.com/)

[PyPI project page](https://pypi.org/project/nftl-ed-lms-tools/)


# Installation

```sh
pip install nftl-ed-lms-tools
```

# Usage

```python
    from nftl_ed_lms_tools.client import EdClient

    ed = EdClient(token='xoxp-...')
    users = ed.get_users_api().get_users()

    if users:
        print('Yupi!')
```

# Deployment how to

Available [here](https://packaging.python.org/tutorials/packaging-projects/)