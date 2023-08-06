from setuptools import setup, find_packages

setup(
    name="ws_proxy",
    version='0.2.3',
    zip_safe=False,
    platforms='any',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    install_requires=['gevent-websocket', 'netkit'],
    url="https://github.com/dantezhu/ws_proxy",
    license="MIT",
    author="dantezhu",
    author_email="zny2008@gmail.com",
    description="tcp's websocket proxy",
)
