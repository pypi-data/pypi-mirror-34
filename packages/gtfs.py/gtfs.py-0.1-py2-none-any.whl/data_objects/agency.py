import csv
import sys

from gtfspy.data_objects.base_object import BaseGtfsObjectCollection
from gtfspy.data_objects.line import LineCollection
from gtfspy.utils import parse_or_default


class Agency:
    def __init__(self, transit_data, agency_id, agency_name, agency_url, agency_timezone, agency_lang=None,
                 agency_phone=None, agency_email=None, agency_fare_url=None, **kwargs):
        """
        :type agency_id: str | int
        :type agency_name: str
        :type agency_url: str
        :type agency_timezone: str
        :type agency_lang: str | None
        :type agency_phone: str | None
        :type agency_email: str | None
        :type agency_fare_url: str | None
        """

        self.agency_id = int(agency_id)
        self.agency_name = agency_name
        self.agency_url = agency_url
        self.agency_timezone = agency_timezone
        self.agency_lang = parse_or_default(agency_lang, None, str)
        self.agency_phone = parse_or_default(agency_phone, None, str)
        self.agency_email = parse_or_default(agency_email, None, str)
        self.agency_fare_url = parse_or_default(agency_fare_url, None, str)

        self.lines = LineCollection(transit_data, self)

        assert len(kwargs) == 0

    def get_line(self, route):
        return self.lines.get_line(route)

    def get_csv_fields(self):
        return ["agency_id", "agency_name", "agency_url", "agency_timezone", "agency_lang", "agency_phone",
                "agency_email", "agency_fare_url"]

    def to_csv_line(self):
        return {"agency_id": self.agency_id,
                "agency_name": self.agency_name,
                "agency_url": self.agency_url,
                "agency_timezone": self.agency_timezone,
                "agency_lang": self.agency_lang,
                "agency_phone": self.agency_phone,
                "agency_email": self.agency_email,
                "agency_fare_url": self.agency_fare_url}

    def validate(self, transit_data):
        """
        :type transit_data: transit_data_object.TransitData
        """

        self.lines.validate()

    def __sizeof__(self):
        size = object.__sizeof__(self)
        for k, v in self.__dict__.iteritems():
            # TODO: change it to check if it's not a weak reference
            size += sys.getsizeof(v)
        return size


class AgencyCollection(BaseGtfsObjectCollection):
    def __init__(self, transit_data, csv_file=None):
        BaseGtfsObjectCollection.__init__(self, transit_data)

        if csv_file is not None:
            self._load_file(csv_file)

    def add_agency(self, **kwargs):
        agency = Agency(transit_data=self._transit_data, **kwargs)

        self._transit_data._changed()

        assert agency.agency_id not in self._objects
        self._objects[agency.agency_id] = agency
        return agency

    def _load_file(self, csv_file):
        if isinstance(csv_file, str):
            with open(csv_file, "rb") as f:
                self._load_file(f)
        else:
            reader = csv.DictReader(csv_file)
            self._objects = {agency.agency_id: agency for agency in
                             (Agency(transit_data=self._transit_data, **row) for row in reader)}

    def validate(self):
        for i, obj in self._objects.iteritems():
            assert i == obj.agency_id
            obj.validate(self._transit_data)
