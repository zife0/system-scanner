from setuptools import setup, find_packages

setup(
    name="system-scanner",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "scanner=scanner.cli:main",
        ],
    },
)
