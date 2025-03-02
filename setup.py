from setuptools import setup, find_packages

setup(
    name="fireviz",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A quick and elegant visualization package for data analysis.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/fireviz",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "matplotlib",
        "seaborn",
        "plotly",
        "networkx",
        "squarify",
        "numpy",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
