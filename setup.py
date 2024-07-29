import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="debug_infrastructure",
    version="0.0.1",

    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="CyberCX",

    package_dir={"": "debug_infrastructure"},
    packages=setuptools.find_packages(where="debug_infrastructure"),

    python_requires=">=3.9",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.9",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
