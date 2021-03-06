# This file auto-generated by `generate_schema_interface.py`.
# Do not modify this file directly.

import traitlets as T


class NiceTime(T.Enum):
    """One of ['second', 'minute', 'hour', 'day', 'week', 'month', 'year']"""
    def __init__(self, default_value=T.Undefined, **metadata):
        super(NiceTime, self).__init__(['second', 'minute', 'hour', 'day', 'week', 'month', 'year'],
                                    default_value=default_value,
                                    **metadata)