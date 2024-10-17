from setuptools import setup, find_packages

# Inspired by ACIT_GAME_MODULE -> setup.py
setup(
    name="morning_greetings",  # The package name
    version="0.1",
    packages=find_packages(),  # Automatically find all packages in your project
    include_package_data=True,  # Include non-Python files specified in MANIFEST.in (if any)
    description="An automated morning greeting program",
    author="Oskar Ruyter",
    author_email="osruy4770@oslomet.no",
    install_requires=[
        # List your project's dependencies here, if any
    ],
    entry_points={
        'console_scripts': [
            'morning_greetings=mandatory_assignment_2.morning_greetings.main:main',
        ],
    },
)
