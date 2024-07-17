import sys
import os
from cloudevents.http import from_http
import sys
import os
import re
sys.path.append(os.path.abspath('mindwm-api/neomodel'))
sys.path.append(os.path.abspath('mindwm-api/generated/openapi/python/'))
#sys.path.append(os.path.join(os.path.dirname(__file__), './mindwm-api/generated/openapi/python/MindwWM/models/'))

from parliament import Context, event

import neomodel_data
import MindwWM



@event
def main(context: Context):

    """
    Function template
    The context parameter contains the Flask request object and any
    CloudEvent received with the request.
    """
    event = from_http(context.request.headers, context.request.data)
    print(f'XXX', file=sys.stderr)
    print(f'{event.data}', file=sys.stderr)

    # Add your business logic here

    # The return value here will be applied as the data attribute
    # of a CloudEvent returned to the function invoker
    return context.cloud_event.data
