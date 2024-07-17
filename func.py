import os
import sys
import re
sys.path.append(os.path.abspath('mindwm-api/neomodel'))
sys.path.append(os.path.abspath('mindwm-api/generated/openapi/python/'))

from parliament import Context, event

import neomodel_data
import MindWM
import pprint

from cloudevents.http import from_http
from cloudevents import abstract, conversion



@event
def main(context: Context):

    event = from_http(context.request.headers, context.request.data)
    pprint.pprint(conversion.to_json(event), stream=sys.stderr)
    clipboard = MindWM.Clipboard.from_json(conversion.to_json(event))
    pprint.pprint(event, stream=sys.stderr)
    print(clipboard.to_str(), file=sys.stderr)

    
    _, username, hostname, _ = clipboard.source.split(".")

    mindwmUser = neomodel_data.MindwmUser.nodes.get(username = username)
    mindwmHost = mindwmUser.host.get(hostname = hostname)

    clipboardNode = neomodel_data.ClipBoard(data = clipboard.data.data, uuid = clipboard.id).save()
    clipboardNode.host.connect(mindwmHost)


    return context.cloud_event.data
