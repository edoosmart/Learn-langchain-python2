from setuptools import setup, find_packages

setup(
    name="learn-langchain",
    version="1.0",
    description="Learn langchain package python",
    packages=find_packages(),
    install_requires=[
        "python-dotenv",
        "colorama",
        "langchain",
        "openai",
    ],
)
