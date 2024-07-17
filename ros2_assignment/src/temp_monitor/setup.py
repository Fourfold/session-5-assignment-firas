from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'temp_monitor'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='fourfold',
    maintainer_email='fourfold164@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "temperature_sensor = temp_monitor.temperature_publisher:main",
            "temperature_alert = temp_monitor.threshold_subscriber:main",
            "alert = temp_monitor.alert_publisher:main",
            "temperature_logger = temp_monitor.temperature_logger:main",
        ],
    },
)
