# randomify
### Simple python library for generate random words

### Usage:

```python
from randomify import username


if __name__ == "__main__":
    names = [username() for _ in range(100)]
    from json import dumps
    print(dumps(names, indent=4))
```

### Author: [@lord_code](https://t.me/lord_codes)