import setuptools
import os
from subprocess import check_output

command = "git describe --tags --dirty"
version_format = ("{tag}.dev{commitcount}+{gitsha}",)


def format_version(version, fmt):
    parts = version.split("-")
    assert len(parts) in (3, 4)
    dirty = len(parts) == 4
    tag, count, sha = parts[:3]
    if count == "0" and not dirty:
        return tag
    return fmt.format(tag=tag, commitcount=count, gitsha=sha.lstrip("g"))


version = check_output(command.split()).decode("utf-8").strip()


with open("README.rst", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    install_requires = fh.read().split("\n")

setuptools.setup(
    name="jinjamator-plugin-output-apic",
    version=version,
    author="Wilhelm Putz",
    author_email="jinjamator@aci.guru",
    description="Cisco ACI output plugin for jinjamator",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/jinjamator/jinjamator-plugin-output-apic",
    include_package_data=True,
    packages=["jinjamator.plugins.output.apic"],
    install_requires=install_requires,
    license="ASL V2",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.8",
        "Topic :: System :: Installation/Setup",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
    ],
    python_requires=">=3.8",
    zip_safe=False,
)
