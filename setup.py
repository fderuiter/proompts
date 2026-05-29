from setuptools import setup, find_packages

setup(
    name="promptops",
    version="0.1.0",
    description="Enterprise PromptOps Toolkit",
    packages=find_packages(include=["promptops", "promptops.*"]),
    install_requires=[
        "PyYAML",
        "pydantic>=2.0.0",
        "jinja2",
    ],
    entry_points={
        "console_scripts": [
            "promptops=promptops.cli:main",
        ],
    },
)
