from setuptools import setup


def readme_file():
    with open("README.rst", encoding="UTF-8") as f:
        return f.read()

setup(name="zxtestlib", version="1.0.0", description="This is a test lib", packages=["zxtestlib"],
    py_modules=["tool"], author="zx", author_email="870121209@qq.com", long_description=readme_file(),
    url="https://gibhut.com/zhongxi/python_code")
