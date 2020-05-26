import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="LightTimer", # Replace with your own username
    version="0.0.1",
    author="Mason Landry",
    author_email="mason-landry@outlook.com",
    description="Timer for controlling fluorescent lights",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mason-landry/LightTimer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Raspbian",
    ],
    python_requires='>=2.7',
)