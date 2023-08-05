import setuptools

with open("README.md", "r",encoding="utf8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wechat_auto",
    version="0.7.0",
    author="Qinluo",
    author_email="shi12li12@gmail.com",
    description="A wechat chatroom auto reply and sent message robot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/true1023/wechat_auto",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)