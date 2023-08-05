```python
url = 'http://archive.ubuntu.com/ubuntu'
components = ['main', 'universe', 'multiverse', 'restricted']
sources = APTSources([
    APTRepository(url, 'xenial', components),
    APTRepository(url, 'xenial-updates', components),
    APTRepository(url, 'xenial-backports', components),
    APTRepository(url, 'xenial-proposed', components)
])

print([(package.package, package.version) for package in sources.get_packages_by_name('docker.io')])
[('docker.io', '1.10.3-0ubuntu6'), ('docker.io', '1.13.1-0ubuntu1~16.04.2'), ('docker.io', '17.03.2-0ubuntu2~16.04.1')]
```