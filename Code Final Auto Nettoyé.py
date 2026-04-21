from niryo_robot_python_ros_wrapper.ros_wrapper import *
import rospy

rospy.init_node('niryo_blockly_interpreted_code')
n = NiryoRosWrapper()

n.calibrate_auto()

for count in range(2):
    n.control_conveyor(ConveyorID.ID_1, True, 100, ConveyorDirection.BACKWARD)

    while True:
        if not n.digital_read('DI5'):
            n.control_conveyor(ConveyorID.ID_1, False, 0, 1)
            break
        else:
            n.control_conveyor(ConveyorID.ID_1, True, 100, ConveyorDirection.BACKWARD)

    n.move_joints(*[0.075, 0.122, -0.431, 0.009, -0.861, 0.034])
    n.release_with_tool()
    n.execute_registered_trajectory("trajet_tapis")
    n.grasp_with_tool()
    n.execute_registered_trajectory("trajet_BBlue")
    n.release_with_tool()
    n.move_joints(*[0.075, 0.122, -0.431, 0.009, -0.861, 0.034])

    n.control_conveyor(ConveyorID.ID_1, True, 100, ConveyorDirection.BACKWARD)

    while True:
        if not n.digital_read('DI5'):
            n.control_conveyor(ConveyorID.ID_1, False, 0, 1)
            break
        else:
            n.control_conveyor(ConveyorID.ID_1, True, 100, ConveyorDirection.BACKWARD)

    n.move_joints(*[0.075, 0.122, -0.431, 0.009, -0.861, 0.034])
    n.release_with_tool()
    n.execute_registered_trajectory("trajet_tapis")
    n.grasp_with_tool()
    n.execute_registered_trajectory("trajet_BVert")
    n.release_with_tool()
    n.move_joints(*[0.075, 0.122, -0.431, 0.009, -0.861, 0.034])