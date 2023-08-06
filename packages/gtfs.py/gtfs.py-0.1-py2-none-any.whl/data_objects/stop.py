import csv

from gtfspy import transit_data_object
from gtfspy.data_objects.base_object import BaseGtfsObjectCollection
from gtfspy.utils import parse_or_default, str_to_bool


class Stop:
    def __init__(self, transit_data, stop_id, stop_name, stop_lat, stop_lon, stop_code=None, stop_desc=None,
                 zone_id=None, stop_url=None, location_type=None, parent_station=None, stop_timezone=None,
                 wheelchair_boarding=None, **kwargs):
        """
        :type transit_data: transit_data_object.TransitData
        :type stop_id: str | int
        :type stop_name: str
        :type stop_lat: str | float
        :type stop_lon: str | float
        :type stop_code: str | None
        :type stop_desc: str | None
        :type zone_id: str | int | None
        :type stop_url: str | None
        :type location_type: str | bool | None
        :type parent_station: str | int | None
        :type stop_timezone: str | None
        :type wheelchair_boarding: str | int | None
        """

        self.stop_id = int(stop_id)
        self.stop_name = stop_name
        self.stop_lat = float(stop_lat)
        self.stop_lon = float(stop_lon)
        self.stop_code = parse_or_default(stop_code, None, str)
        self.stop_desc = parse_or_default(stop_desc, None, str)
        self.zone_id = parse_or_default(zone_id, None, int)
        self.stop_url = parse_or_default(stop_url, None, str)
        self.is_central_station = parse_or_default(location_type, False, str_to_bool)
        self.parent_station = parse_or_default(parent_station, None, int)
        # self.parent_station = None if parent_station == '' else transit_data.stops[parent_station]
        self.stop_timezone = parse_or_default(stop_timezone, None, str)
        self.wheelchair_boarding = parse_or_default(wheelchair_boarding, None, int)

        self.stop_times = []

        assert len(kwargs) == 0

    def get_csv_fields(self):
        return ["stop_id", "stop_name", "stop_lat", "stop_lon", "stop_code", "stop_desc", "zone_id", "stop_url",
                "location_type", "parent_station", "stop_timezone", "wheelchair_boarding"]

    def to_csv_line(self):
        return {"stop_id": self.stop_id,
                "stop_name": self.stop_name,
                "stop_lat": self.stop_lat,
                "stop_lon": self.stop_lon,
                "stop_code": self.stop_code,
                "stop_desc": self.stop_desc,
                "zone_id": self.zone_id,
                "stop_url": self.stop_url,
                "location_type": 1 if self.is_central_station else 0,
                "parent_station": self.parent_station,
                "stop_timezone": self.stop_timezone,
                "wheelchair_boarding": self.wheelchair_boarding}

    def validate(self, transit_data):
        """
        :type transit_data: transit_data_object.TransitData
        """

        assert self.parent_station is None or self.parent_station in transit_data.stops
        assert self.wheelchair_boarding is None or self.wheelchair_boarding in xrange(0, 3)


class StopCollection(BaseGtfsObjectCollection):
    def __init__(self, transit_data, csv_file=None):
        BaseGtfsObjectCollection.__init__(self, transit_data)

        if csv_file is not None:
            self._load_file(csv_file)

    def add_stop(self, **kwargs):
        stop = Stop(transit_data=self._transit_data, **kwargs)

        self._transit_data._changed()

        assert stop.stop_id not in self._objects
        self._objects[stop.stop_id] = stop
        return stop

    def _load_file(self, csv_file):
        if isinstance(csv_file, str):
            with open(csv_file, "rb") as f:
                self._load_file(f)
        else:
            reader = csv.DictReader(csv_file)
            self._objects = {stop.stop_id: stop for stop in
                             (Stop(transit_data=self._transit_data, **row) for row in reader)}

    def validate(self):
        for i, obj in self._objects.iteritems():
            assert i == obj.stop_id
            obj.validate(self._transit_data)