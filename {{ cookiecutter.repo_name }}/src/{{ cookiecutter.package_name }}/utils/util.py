import yaml


def yaml2dict(fpath: str) -> dict:
    """Opens yaml file at fpath and returns content as dict"""
    content = yaml.safe_load(open(fpath))
    return content


def get_conf(fpath: str) -> dict:
    """Return configuration stored in a YAML file"""
    return yaml2dict(fpath)
