# Copyright (C) 2015 tCell.io, Inc. - All Rights Reserved

from __future__ import unicode_literals

from tcell_agent.sensor_events.base_event import SensorEvent

# Use this to cause the event queue to flush if you don't need
# to send an actual event (ie, metrics get too big)


class FlushDummyEvent(SensorEvent):
    def __init__(self):
        super(FlushDummyEvent, self).__init__("dummy", flush_right_away=True, send_event=False)
