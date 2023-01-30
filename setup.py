from setuptools import setup, find_packages

setup(name='help-assistant',
    version='0.0.6',
    description= 'Addressbook, notebook, clean folder',
    url='https://github.com/DenBilokon/Assistant_PROJECT',
    author='Denis Bilokon, Kirill Sheremeta, Denys Zaycev, Dmytro Marchenko, Maria Palona',
    author_email='greenjuiced@gmail.com',
    license='MIT',
    packages=find_packages(),
    entry_points= {'console_scripts': ['assistant = assistant.menu:menu']}
          )