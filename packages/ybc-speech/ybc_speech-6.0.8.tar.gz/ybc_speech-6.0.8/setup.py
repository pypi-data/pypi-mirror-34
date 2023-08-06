from distutils.core import setup
setup(
  name = 'ybc_speech',
  packages = ['ybc_speech'],
  version = '6.0.8',
  description = 'Speech Recognition',
  long_description='Speech Recognition,voice2text,text2voice',
  author = 'KingHS',
  author_email = '382771946@qq.com',
  keywords = ['pip3', 'speech', 'python3','python','Speech Recognition'],
  license='MIT',
  install_requires=[
        'pyaudio',
        'wave',
        'requests'
    ],
)
