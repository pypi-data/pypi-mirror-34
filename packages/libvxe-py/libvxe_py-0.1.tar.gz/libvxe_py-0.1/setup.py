from setuptools import setup

setup(name='libvxe_py',
      version='0.1',
      description='Py Dev',
      url='https://github.com/vxe/libvxe-py.git',
      author='Vijay Edwin',
      author_email='vedwin.dev@gmail.com',
      license='MIT',
      packages=['libvxe_py'],
      install_requires=[
          'bottle',
      ],
      zip_safe=False)
