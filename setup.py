from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="peg",
    version="0.0.1",
    description="PEG - Pyautogui Extension with GUI - GUI helper for creating pyautogui scripts.",
    py_modules=[
        "peg",
    ],
    packages=find_packages(),
    package_dir={"peg": "peg"},
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    license="MIT License",
    entry_points=dict(console_scripts=[
        "peg = peg.__main__:main",
    ]),
    url="https://github.com/NavpreetDevpuri/peg",
    author="Navpreet Devpuri",
    author_email="NavpreetDevpuri@gmail.com",
    install_requires=[
        "pyautogui",
        "opencv-python"
    ],
    extras_require={
        "dev": [
            "",
            "",
            "",
        ],
    },
)
