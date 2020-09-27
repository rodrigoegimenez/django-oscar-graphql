import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-oscar-graphql",
    version="0.1.0",
    author="Rodrigo E. Gimenez",
    author_email="rodrigog83@gmail.com",
    description="GraphQl API module for django-oscar",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rodrigoegimenez/django-oscar-graphql",
    packages=setuptools.find_packages(),
    install_requires=[
        "django-oscar>=2.0",
        "graphene-django"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Linux",
    ],
    python_requires='>=3.6',
)
