from os import getenv

from app.utils.core import read_yaml

DEFAULT_SETTINGS_FILE_PATH = "app/configs/settings.yaml"
DEFAULT_MAX_REQUESTED_BYTE_SUPPORTED = 50000000
DEFAULT_PORT = 8000
DEFAULT_WORKERS = 1
DEFAULT_LOG_FORMAT = "%(asctime)s | %(levelname)s | %(message)s"
PROD_ENV = "prod"
ERROR_LOG_LEVEL = "ERROR"

def load_config():
    """
    Load configuration with environment variables 
    taking precedence over the YAML file.
    """

    # Load config from yaml 
    file_config = read_yaml(DEFAULT_SETTINGS_FILE_PATH)

    # Check if env is prod
    is_prod = getenv("APP_ENV", file_config.get("app",{}).get("env", PROD_ENV)) == PROD_ENV

    # Enforce logging level to ERROR if its prod env
    log_level = ERROR_LOG_LEVEL if is_prod else getenv("LOG_LEVEL", file_config.get("logging", {}).get("level", ERROR_LOG_LEVEL))

    # Evaluate the max_request_byte supported
    MAX_REQUESTED_BYTES = min(
        int(getenv("MAX_REQUEST_BYTES", file_config.get("app", {}).get("max_request_bytes", DEFAULT_MAX_REQUESTED_BYTE_SUPPORTED))),
        DEFAULT_MAX_REQUESTED_BYTE_SUPPORTED
    )
    
    # Create config with higher precedence to env vars
    config = {
        "logging": {
            "level": log_level,
            "format": getenv("LOG_FORMAT", file_config.get("logging", {}).get("format", DEFAULT_LOG_FORMAT)),
        },
        "app": {
            "port": int(getenv("APP_PORT", file_config.get("app", {}).get("port", DEFAULT_PORT))),
            "workers": int(getenv("APP_WORKERS", file_config.get("app", {}).get("workers", DEFAULT_WORKERS))),
            "reload": not is_prod,
            "max_request_bytes": MAX_REQUESTED_BYTES,
        }
    }
    print(f"Initializing app with : [{config}] config")
    return config
