import setuptools

setuptools.setup(
    name='cartoongan',
    version='0.0.1',
    description='CartoonGAN style transfer for Hayao style.',
    author='Filip Andersson, Simon Arvidsson',
    packages=[
        'cartoongan',
        'cartoongan.utils',
        'cartoongan.models'
        ],
    package_dir={
        'cartoongan': '.',
        'cartoongan.utils': 'utils',
        'cartoongan.models': 'models',
        },
    license='MIT'
    )
