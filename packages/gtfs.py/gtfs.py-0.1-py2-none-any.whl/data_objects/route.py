import csv

from gtfspy import transit_data_object
from gtfspy.data_objects.base_object import BaseGtfsObjectCollection
from gtfspy.utils import parse_or_default


class Route:
    def __init__(self, transit_data, route_id, route_short_name, route_long_name, route_type, agency_id,
                 route_desc=None, route_color=None, route_text_color=None, bikes_allowed=None, **kwargs):
        """
        :type transit_data: transit_data_object.TransitData
        :type route_id: str
        :type route_short_name: str
        :type route_long_name: str
        :type route_type: str | int
        :type agency_id: str | int
        :type route_desc: str | None
        :type route_color: str | None
        :type route_text_color: str | None
        :type bikes_allowed: str | int | bool | None
        """

        self.route_id = route_id
        self.route_short_name = route_short_name
        self.route_long_name = route_long_name
        # TODO: create dedicated object to route type
        self.route_type = int(route_type)
        self.agency = transit_data.agencies[int(agency_id)]
        self.route_desc = parse_or_default(route_desc, None, str)
        # TODO: find type for the route color
        self.route_color = parse_or_default(route_color, None, str)
        self.route_text_color = parse_or_default(route_text_color, None, str)
        # TODO: create parser for yes-no-unknown: 0 for unknown, 1 for yes, and 2 for no
        self.bikes_allowed = parse_or_default(bikes_allowed, None, int)

        self.line = self.agency.get_line(self)
        self.trips = []

        assert len(kwargs) == 0

    @property
    def stops(self):
        return None if len(self.trips) == 0 else self.trips[0].stops

    @property
    def first_stop(self):
        return None if len(self.trips) == 0 else self.trips[0].first_stop

    @property
    def last_stop(self):
        return None if len(self.trips) == 0 else self.trips[0].last_stop

    def get_trips_calendar(self, from_date, to_date=None, stop_id=None, sort=True):
        res = ((t, trip)
               for trip in self.trips
               for t in trip.get_trip_calendar(from_date, to_date=to_date, stop_id=stop_id))

        if sort:
            res = list(res)
            res.sort()

        return res

    def get_csv_fields(self):
        return ["route_id", "route_short_name", "route_long_name", "route_type", "agency_id", "route_desc",
                "route_color", "route_text_color", "bikes_allowed"]

    def to_csv_line(self):
        return {"route_id": self.route_id,
                "route_short_name": self.route_short_name,
                "route_long_name": self.route_long_name,
                "route_type": self.route_type,
                "agency_id": self.agency.agency_id,
                "route_desc": self.route_desc,
                "route_color": self.route_color,
                "route_text_color": self.route_text_color,
                "bikes_allowed": 1 if self.bikes_allowed else 0}

    def validate(self, transit_data):
        """
        :type transit_data: transit_data_object.TransitData
        """

        assert transit_data.agencies[self.agency.agency_id] is self.agency
        assert self.route_type in xrange(0, 8)
        assert self.bikes_allowed is None or self.bikes_allowed in xrange(0, 3)


class RouteCollection(BaseGtfsObjectCollection):
    def __init__(self, transit_data, csv_file=None):
        BaseGtfsObjectCollection.__init__(self, transit_data)

        if csv_file is not None:
            self._load_file(csv_file)

    def add_route(self, **kwargs):
        route = Route(transit_data=self._transit_data, **kwargs)

        self._transit_data._changed()

        assert route.route_id not in self._objects
        self._objects[route.route_id] = route
        return route

    def _load_file(self, csv_file):
        if isinstance(csv_file, str):
            with open(csv_file, "rb") as f:
                self._load_file(f)
        else:
            reader = csv.DictReader(csv_file)
            self._objects = {route.route_id: route for route in
                             (Route(transit_data=self._transit_data, **row) for row in reader)}

    def validate(self):
        for i, obj in self._objects.iteritems():
            assert i == obj.route_id
            obj.validate(self._transit_data)