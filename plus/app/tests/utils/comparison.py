from typing import Dict


# TODO: move this function to testutil
def filter_dict(template: Dict, src: Dict):
    """
    filter `src` with only fields contains in `template`
    """
    return {k: v for k, v in src.items() if k in template.keys()}
