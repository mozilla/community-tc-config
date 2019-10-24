from setuptools import setup, find_packages

setup(
    name="community-tc-config",
    version="1.0.0",
    description="Configuration for Taskcluster at https://community-tc.services.mozilla.com/",
    author="Dustin Mitchell",
    author_email="dustin@mozilla.com",
    url="https://github.com/djmitche/community-tc-config",
    packages=find_packages("."),
    install_requires=[
        "tc-admin~=2.1.0",
        "json-e~=3.0.0",
    ],
    setup_requires=["pytest-runner", "flake8"],
    tests_require=["pytest-mock", "pytest-asyncio", "flake8"],
    classifiers=("Programming Language :: Python :: 3",),
)
