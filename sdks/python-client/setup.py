from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="zerix-client",
    version="0.1.10",
    author="Zerix",
    author_email="hello@zerix.ai",
    description="A package for interacting with the Zerix Service-API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zerix-ai/zerix-sdk-python",
    license='MIT',
    packages=['zerix_client'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "requests"
    ],
    keywords='zerix nlp ai language-processing',
    include_package_data=True,
)
