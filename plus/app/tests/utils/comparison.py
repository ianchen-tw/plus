from typing import Dict


def filter_dict(template: Dict, src: Dict):
    """
    filter `src` with only fields contains in `template`
    """
    return {k: v for k, v in src.items() if k in template.keys()}
