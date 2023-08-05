import setuptools

setuptools.setup(
    name="tap_news_utils",
    version="0.0.5.2",
    author="Yitong Wu",
    author_email="yw4004@nyu.edu",
    description="A small utility package for tap-news project",
    packages=setuptools.find_packages(),
    install_requires=[
          'pika',
          'requests',
          'pymongo'
      ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
