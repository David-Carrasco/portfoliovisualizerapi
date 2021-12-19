from typing import Dict, Union


def validate_input_keys(conf: Dict[str, Union[str, float]],
                        naming_keys: Dict[str, str]) -> bool:
    """
    verify each key in the config dict is defined in the naming keys
    """
    return set(conf.keys()).issubset(set(naming_keys.keys()))


def validate_input_values(conf: Dict[str, Union[str, float]],
                          naming_values: Dict[str, Dict[str, Union[str, float]]]) -> bool:
    """
    verify each string value in the config dict is defined in the naming values
    """

    str_conf_dict = {key:value for (key,value) in conf.items() if isinstance(value, str)}

    return all(conf.get(key) in naming_values.get(key).keys()
               for key, _ in str_conf_dict.items())


def apply_naming_keys(conf: Dict[str, Union[str, float]],
                      naming_keys: Dict[str, str]) -> Dict:
    """
    create conf with naming keys
    """
    output_conf = {}

    for key, value in conf.items():
        output_conf.update({naming_keys.get(key): value})

    return output_conf


def apply_naming_values(conf: Dict[str, Union[str, float]],
                        naming_values: Dict[str, Dict[str, Union[str, float]]]) -> Dict:
    """
    update conf values according to the naming values
    """
    for key, value in conf.items():
        if isinstance(value, str):
            conf.update({key: naming_values.get(key).get(value)})

    return conf
