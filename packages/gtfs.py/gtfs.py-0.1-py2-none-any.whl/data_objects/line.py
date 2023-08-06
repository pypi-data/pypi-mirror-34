import itertools

from gtfspy.data_objects.base_object import BaseGtfsObjectCollection


class Line:
    def __init__(self, agency, line_number):
        """
        :type agency: data_objects.agency.Agency
        :type line_number: str
        """

        self.agency = agency
        self.line_number = line_number

        self.routes = {}

    def add_route(self, route):
        # TODO: check if the route id exists
        self.routes[route.route_id] = route

    def get_trips_calendar(self, from_date, to_date=None, sort=True):
        res = itertools.chain.from_iterable(route.get_trips_calendar(from_date, to_date=to_date, sort=False)
                                            for route in self.routes.itervalues())

        if sort:
            res = list(res)
            res.sort()

        return res

    def validate(self, transit_data):
        """
        :type transit_data: transit_data_object.TransitData
        """

        assert transit_data.agencies[self.agency.agency_id] is self.agency


class LineCollection(BaseGtfsObjectCollection):
    def __init__(self, transit_data, agency):
        BaseGtfsObjectCollection.__init__(self, transit_data)
        self._agency = agency

    def get_line(self, route):
        line_number = route.route_short_name

        self._transit_data._changed()

        if line_number not in self:
            line = gtfspy.data_objects.line.Line(self._agency, line_number)
            self._objects[line_number] = line
        else:
            line = self[line_number]

        line.add_route(route)

        return line

    def add_line(self, **kwargs):
        line = Line(**kwargs)

        assert line.line_number not in self._objects
        self._objects[line.line_number] = line
        return line

    def validate(self):
        for i, obj in self._objects.iteritems():
            assert i == obj.line_number
            obj.validate(self._transit_data)