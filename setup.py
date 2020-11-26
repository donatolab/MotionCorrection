import os

from setuptools import find_packages, setup

install_requires = [
    line.rstrip()
    for line in open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
]

setup(
    name="MotionCorrection",
    install_requires=install_requires,
    version="0.0.1",
    description="Improving motion correction for calcium imaging. Project for programming course",
    url="https://github.com/donatolab/MotionCorrection",
    license="MIT",
    packages=find_packages(),
    zip_safe=False,
)
