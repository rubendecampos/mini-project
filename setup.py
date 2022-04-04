import setuptools 


setuptools.setup(name='saru',
      version='0.6',
      long_description=open("README.rst").read(),
      url='https://github.com/rubendecampos/mini-project',
      author='Ruben De CAMPOS and Samuel MICHEL',
      author_email='saru@example.com',
      license='LICENSE.txt',
      packages=setuptools.find_packages(),
      zip_safe=False,
      entry_points={  
        'console_scripts': ['saru-run=saru.run:main',],
        },
      python_requires=">=3.8, <3.10",
      install_requires=["numpy==1.20.3","pandas==1.3.4","scikit-learn==0.24.2"],
      package_data={
        # If any package contains *.txt files, include them:
        "saru": ["Datasets/*"],
    }
    )