"""
.. module: historical.commom.util
    :platform: Unix
    :copyright: (c) 2018 by Netflix Inc., see AUTHORS for more
    :license: Apache, see LICENSE for more details.
.. author:: Mike Grima <mgrima@netflix.com>
"""
import json


def deserialize_records(records):
    """
    This properly deserializes records depending on where they came from:
        - SQS
        - SNS
    """
    native_records = []
    for r in records:
        parsed = json.loads(r['body'])

        # Is this from SNS (cross-region request -- SNS messages wrapped in SQS message)?
        if parsed.get('Type') == 'Notification' and parsed.get('Message'):
            native_records.append(json.loads(parsed['Message']))

        else:
            native_records.append(parsed)

    return native_records
