from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
   return LaunchDescription([
       Node(
           package="mavros",           
           executable="mavros_node",           
           parameters=[            
            {"fcu_url": "/dev/ttyACM0:115200"},
            {"gcs_url": ""},
            {"tgt_system": 1},
            {"tgt_component": 1},                
            {"uas_url": "rcraicer"},     
            # {"system_id": "v2.0"},                
            # {"component_id": "v2.0"},                
            # {"target_system_id": "v2.0"},                
            # {"target_component_id": "v2.0"},                
            {"plugin_allowlist": ["imu"]},                
            {"plugin_denylist": ["*"]}                 	
        ]
       )
   ])