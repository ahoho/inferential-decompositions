from datetime import datetime
from pathlib import Path
import os 
import yaml
from jinja2 import Environment, StrictUndefined

def try_read_key(key):
    if Path(key).expanduser().exists():
        return Path(key).expanduser().read_text().strip()
    return key


def update(d, u, dict_params=[]):
    """
    Recursive update the "base" dictionary `d` with values from `u`
    Modified from 
    https://stackoverflow.com/a/3233356/5712749
    """
    for k, v in u.items():
        if k not in d:
            raise KeyError(f"parameter {k} not in `_default.yaml`")
        if isinstance(v, dict) and k not in dict_params:
            d[k] = update(d[k], v, dict_params)
        else:
            d[k] = v
    return d


def load_config(user_fpath=None, default_fpath="configs/_propositions-gpt3.yaml"):
    """
    Load the configuration YAML into a dictionary. 

    `default_fpath` is a file where all settings are specified.
    """
    with open(default_fpath) as infile:
        config = yaml.safe_load(infile)
    if user_fpath is not None:  
        with open(user_fpath) as infile:
            user = yaml.safe_load(infile)
        config = update(config, user, dict_params=["label_map", "generation_kwargs"])

    config["llm"]["openai_api_key"] = os.environ["OPENAI_API_KEY"]
    config = format_results_dir(config)
    return config


def save_config(config, fpath):
    """
    Save config as a yaml file
    """
    with open(fpath, "w") as outfile:
        yaml.safe_dump(config, outfile, indent=2)


def format_results_dir(config):
    """Format results directory with jinja2"""
    if config["main"]["results_dir_template"] is not None:
        if config["main"].get("results_dir") is not None:
            raise ValueError("Specify one of `results_dir` or `results_dir_template`")
        
        # add dates to config
        now = datetime.now()
        config["main"]["date"] = now.strftime("%Y-%m-%d %H:%M")
        if config["main"]["experiment_name"] is None:
            # set experiment name to current date and time
            config["main"]["experiment_name"] = now.strftime("%Y.%m.%d_%H.%M")
        
        # render the template; bit hacky way to avoid `/` in keys
        env = Environment(undefined=StrictUndefined)
        template_parts = config["main"]["results_dir_template"].split("/")
        rendered_parts = [
            env.from_string(part).render(**config).replace("/", "_")
            for part in template_parts
        ]
        config["main"]["results_dir"] = "/".join(rendered_parts)
    return config


if __name__ == "__main__":
    config = load_config("configs/_default.toml")
    print(config)