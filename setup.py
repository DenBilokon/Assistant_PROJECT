from setuptools import setup, find_packages

setup(name='Help_Assistant',
    version='0.0.2',
    description= 'Addressbook, notebook, clean folder',
    url='https://github.com/DenBilokon/Assistant_PROJECT',
    author='Denis Bilokon, Kirill Sheremeta, Denys Zaycev, Dmytro Marchenko, Maria Palona',
    author_email='greenjuiced@gmail.com',
    license='MIT',
    packages=find_packages(),
    entry_points= {'console_scripts': ['assistant = assistant.menu:menu']}
          )