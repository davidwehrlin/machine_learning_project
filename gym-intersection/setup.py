import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gym_intersection",
    version="0.0.1",
    install_requires=['gym'],
    author="David Wehrlin, Derek Foundoulis, Jacob Warcholik",
    author_email="davidwehrlin@my_mail.mines.edu",
    description="An intersection environment for OpenAI Gym",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/davidwehrlin/machine_learning_project/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
