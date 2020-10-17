import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="Tarea3",
    version="0.0.1",
    author="9911sofia",
    author_email="9911sofia@gmail.com",
    description="Tarea3RamirezLeeDonatoLopez",
    long_description=long_description,
    url="https://github.com/9911sofia/Tarea3.git",
    install_requires=['Pillow', 'tabulate', 'playsound', 'argparse'],
    packages=setuptools.find_packages(),
    classifiers=[
        ...],
)
    
