from pathlib import Path
from setuptools import setup, find_packages


def find_version() -> str:
    version = "0.0.1"
    extension_yaml_path = Path(__file__).parent / "extension" / "extension.yaml"
    try:
        with open(extension_yaml_path, encoding="utf-8") as f:
            for line in f:
                if line.startswith("version"):
                    version = line.split(" ")[-1].strip("\"")
                    break
    except Exception:
        pass
    return version


setup(name="storage_insights_extension",
      version=find_version(),
      description="Storage_insights_extension python EF2 extension",
      author="Dynatrace",
      packages=find_packages(),
      python_requires=">=3.10",
      include_package_data=True,
      install_requires=["dt-extensions-sdk", "requests"],
      extras_require={"dev": ["dt-extensions-sdk[cli]"]},
      )
