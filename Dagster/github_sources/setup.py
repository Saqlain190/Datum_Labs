from setuptools import find_packages, setup

setup(
    name="github_sources",
    packages=find_packages(exclude=["github_sources_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
