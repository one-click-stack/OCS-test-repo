from setuptools import setup

setup(
    name="my_flask_app",
    version="0.0.1",
    description="Python web app running Flask",
    author="OneClickStack",
    license="unlicense",
    packages=["app"],
    install_requires=["flask"],
    zip_safe=False,
)