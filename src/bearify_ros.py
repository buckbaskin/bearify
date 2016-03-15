import rospy

bearing_out = rospy.Publisher('processed_image/bearings', VizScan, queue_size=1)

def image_cb(image):
    pass

image_in = rospy.Subscriber('/camera/image/rgb', ImageMsg, image_cb)


if __name__ == '__main__':
    rospy.init_node('bearify')
    rospy.spin()    