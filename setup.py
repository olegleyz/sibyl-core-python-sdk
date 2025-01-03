from setuptools import setup, find_packages

setup(
    name="sibyl-core-python-sdk",
    version="0.1.0",
    description="Python SDK for Sibyl Core APIs",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/olegleyz/sibyl-core-python-sdk.git",
    author="Oleg Leizerov",
    license="Proprietary",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.12",
    ],
    keywords="sibyl api sdk",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests>=2.31.0",
        "urllib3>=2.0.0",
    ],
    python_requires=">=3.12",
    include_package_data=True,
    package_data={
        "sibyl_core_python_sdk": ["*.yaml"],
    },
    zip_safe=False,
)
