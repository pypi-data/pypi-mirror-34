import csv
import sys


class BaseGtfsObject:
    def __init__(self, optional_arguments, **kwargs):
        pass


class BaseGtfsObjectCollection(object):
    def __init__(self, transit_data):
        self._transit_data = transit_data
        self._objects = {}

    def save(self, csv_file):
        if isinstance(csv_file, str):
            with open(csv_file, "wb") as f:
                self.save(f)
        else:
            fields = []
            for obj in self:
                fields += (field for field in obj.get_csv_fields() if field not in fields)

            writer = csv.DictWriter(csv_file, fieldnames=fields, restval=None)
            writer.writeheader()
            writer.writerows(obj.to_csv_line() for obj in self)

    def __len__(self):
        return len(self._objects)

    def __getitem__(self, key):
        return self._objects[key]

    def __iter__(self):
        return self._objects.itervalues()

    def __contains__(self, item):
        return item in self._objects

    def __sizeof__(self):
        size = object.__sizeof__(self)
        for k, v in self.__dict__.iteritems():
            # TODO: change it to check if it's not a weak reference
            if k not in ["_transit_data"]:
                size += sys.getsizeof(v)
        return size
