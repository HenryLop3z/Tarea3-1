import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="Tarea3",
    version="0.0.1",
    author="9911sofia, HenryLop3z, LuigiDonato, LazySloth26",
    author_email="9911sofia@gmail.com",
    description="Tarea3RamirezLeeDonatoLopez",
    url="https://github.com/9911sofia/Tarea3.git",
    packages=['T3'],
    install_requires=['pillow', 'tabulate', 'playsound', 'argparse'],
    package_data={  # Archivos extras a los paquetes
        'T3': ['meca.jpg', 'Texto_ejemplo.txt', 'Hello.mp3'],
    },
    package_dir={'T3': 'T3'},  # especifica el directorio de los paquetes
    python_requires='>=3.7',  # Versión de Python compatible
    scripts=['T3/lector_texto', 'T3/presentador_de_audio', 'T3/Presentador_de_imágenes'], 
    #packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    zip_safe=False 
)

    
   
   
    
