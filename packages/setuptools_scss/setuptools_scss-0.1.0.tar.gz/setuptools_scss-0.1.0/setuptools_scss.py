"""Plugin for setuptools providing compilation of scss files."""
import os

from distutils.errors import DistutilsSetupError
from setuptools import Command

__version__ = '0.1.0'


def scss_compile(scss_files):
    """Compile SCSS files."""
    for output, inputs in scss_files.items():
        cmd = ['pyscss', '--output', output]
        cmd += list(inputs)

        os.system(' '.join(cmd))


def validate_scss(dist, attr, value):
    """Validate scss files."""
    for inputs in value.values():
        for scss_file in inputs:
            if not os.path.isfile(scss_file):
                raise DistutilsSetupError('Filename {} does not exist.'.format(scss_file))


class build_scss(Command):
    """Custom command that compiles messages."""

    user_options = [
        ('build-lib=', 'd', "directory to \"build\" (copy) to"),
        ]

    def initialize_options(self):
        self.build_lib = None

    def finalize_options(self):
        self.set_undefined_options('build', ('build_lib', 'build_lib'))

    def run(self):
        if self.distribution.scss_files:
            scss_files = {}
            for output, inputs in self.distribution.scss_files.items():
                outfile = os.path.join(self.build_lib, output)
                self.mkpath(os.path.dirname(outfile))
                infiles = []
                for in_file in inputs:
                    target = os.path.join(self.build_lib, in_file)
                    self.mkpath(os.path.dirname(target))
                    self.copy_file(in_file, target)
                    infiles += [target]
                scss_files[outfile] = infiles
                scss_compile(scss_files)
