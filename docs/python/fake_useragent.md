# FAKE_USERAGENT

## install

```bash
pip install fake-useragent
```

## basic usage

```python
from fake_useragent import UserAgent
ua = UserAgent()

ua.ie
ua.random

```

## use local file

```python

import fake_useragent

# I am STRONGLY!!! recommend to use version suffix
location = '/home/user/fake_useragent%s.json' % fake_useragent.VERSION

ua = fake_useragent.UserAgent(path=location)
ua.random

```

