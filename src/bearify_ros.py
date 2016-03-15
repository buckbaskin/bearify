import rospy

from viz_feature_sim.msg import VizScan, Blob
from sensor_msgs.msg import Image

bearing_out = rospy.Publisher('processed_image/bearings', VizScan, queue_size=1)

def image_cb(image_msg):
    header = image_msg.header
    h = image_msg.height
    w = image_msg.width
    encoding = image_msg.encoding
    is_bigendian = image_msg.is_bigendian
    uint32 step = image_msg.step
    image_data = image_msg.data

    cv_image = bridge.imgmsg_to_cv2(image_msg, desired_encoding='passthrough')

image_in = rospy.Subscriber('/camera/image/rgb', Image, image_cb)


if __name__ == '__main__':
    rospy.init_node('bearify')
    rospy.spin()    