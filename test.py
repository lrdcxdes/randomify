from randomify import username


if __name__ == "__main__":
    names = [username() for _ in range(100)]
    from json import dumps

    assert names

    print(dumps(names, indent=4))
