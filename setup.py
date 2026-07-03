import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'brickpi3_ros2'

setup(
    name=package_name,
    version='0.0.2',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pi',
    maintainer_email='andreas.persson@oru.se',
    description='BrickPi3 to ROS 2 wrapper',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "color = brickpi3_ros2.color:main",
            "drive = brickpi3_ros2.drive:main",
            "eyes = brickpi3_ros2.eyes:main",
            "gyro = brickpi3_ros2.gyro:main",
            "motor = brickpi3_ros2.motor:main",
            "touch = brickpi3_ros2.touch:main",
            "ultrasonic = brickpi3_ros2.ultrasonic:main"
        ],
    },
)
