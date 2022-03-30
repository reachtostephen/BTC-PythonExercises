class ComplexCourse:

    def __repr__(self):
        return 'Fee : {0.fee} | available_batches: {0.batches}'.format(self)


class Complexcourse(ComplexCourse):

    def Fee(self):
        self.fee = 7000

    def available_batches(self):
        self.batches = 6


def construct_course(cls):
    course = cls()
    course.Fee()
    course.available_batches()

    return course  # return the course object


if __name__ == "__main__":
    complex_course = construct_course(Complexcourse)
    print(complex_course)
