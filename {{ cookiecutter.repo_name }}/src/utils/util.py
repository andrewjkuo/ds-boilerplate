import yaml


def yaml2dict(fpath: str) -> dict:
    """Opens yaml file at fpath and returns content as dict"""
    content = yaml.safe_load(open(fpath))
    return content
