from setuptools import setup

setup(name='gdelt_process_tone',
      version='0.0.5',
      description='Returns tone and location json files',
      url='',
      author='Development Seed',
      author_email='aimee@developmentseed.org',
      license='MIT',
      py_modules=['gdelt_process_tone'],
      include_package_data=True,
      data_files=[('', ['v2_events_schema.csv'])],
      depends=['numpy', 'pandas'])
