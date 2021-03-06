""" Setup and configuration; installation of pip deps """
from setuptools import setup
setup(name='typecat',
      version='0.01',
      description='Sort, categorize, and find the right font',
      url='http://github.com/LordPharaoh/typecat',
      author='Varun Iyer and Timothy Kanarsky',
      author_email='vi.mail@protonmail.ch',
      license='MIT',
      packages=['typecat', 'typecat.display'],
      install_requires=['pillow', 'tensorflow', 'numpy'],
      keywords='font typography sort categorize search',
      include_package_data=True,
      zip_safe=False)

print("ACTION REQUIRED: Install GTK+ and PyGObject before use; these can be found at"
      "https://www.gtk.org/download/ and "
      "https://pygobject.readthedocs.io/en/latest/getting_started.html respectively.")
