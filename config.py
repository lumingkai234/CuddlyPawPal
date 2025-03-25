import yaml
import os


def read_config():
    """读取config.yaml配置文件"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(current_dir, "config.yaml")
    try:
        with open(config_path, "r", encoding="utf-8") as file:
            config = yaml.safe_load(file)
            return config
    except FileNotFoundError:
        print(f"配置文件 {config_path} 未找到")
        return {}
    except yaml.YAMLError as e:
        print(f"解析YAML文件出错: {e}")
        return {}


config_data = read_config()
