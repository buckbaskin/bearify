Reading = namedtuple('Reading', ['bearing', 'size', 'r', 'g', 'b', 'a'])

def one_click_process(opencv_image):
    # TODO(buckbaskin): do something smart here
    list_of_readings = []
    list_of_readings.append(Reading())
    return list_of_readings