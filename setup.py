from setuptools import setup, find_packages

requirements = [l.strip() for l in open('requirements.txt').readlines()]

setup(
     name='polls',
     version='0.1',
     install_requires = requirements,
     packages = find_packages(),
     include_package_data = True,
     author = 'Phong Dep Zai',
     author_email = 'phongkhonghoang@gmail.com',
     description = ' Django',
     license = 'MIT License',
     keywords = 'django evercookie',
     url='https://github.com/phonghoangkhong/test213',
     )