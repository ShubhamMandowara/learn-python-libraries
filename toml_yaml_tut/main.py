import toml
import yaml

if __name__ == "__main__":
    with open("config_toml.toml", "r") as config:
        config_details = toml.load(config)
        print(config_details)

    with open("config_yaml.yaml", "r") as config:
        config_details = yaml.safe_load(config)
        print(config_details)
