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
    packages=['T3'],
    install_requires=['Pillow', 'tabulate', 'playsound', 'argparse'],
    package_data={  # Archivos extras a los paquetes
        'T3': ['meca.jpg', 'Texto_ejemplo.txt', 'Hello.mp3'],
    },
    package_dir={'T3': 'T3'},  # especifica el directorio de los paquetes
    python_requires='>=3.3',  # Versión de Python compatible
    scripts=['T3/lector_texto.py', 'T3/presentador_de_audio.py', 'T3/Presentador_de_imágenes.py'] 
    packages=setuptools.find_packages(where='T3'),
    classifiers=[
        ...],
)

    
   
   
    
