import attr


@attr.s()
class Argument:
    c_type = attr.ib()
    name = attr.ib()
    info = attr.ib()
    comment = attr.ib()

    @classmethod
    def list_of(cls, data):
        return [cls(*args) for args in data]


@attr.s()
class Function:
    c_return_type = attr.ib()
    name = attr.ib()
    comment = attr.ib()
    argument_list = attr.ib(convert=attr.converters.optional(Argument.list_of))
