# distutils_twine

Lets you use Twine for a `setup.py release`.

```python
import setuptools
from distutils_twine import UploadCommand

setuptools.setup(cmdclass={"release": UploadCommand})
```
