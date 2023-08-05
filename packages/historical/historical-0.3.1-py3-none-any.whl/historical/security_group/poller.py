"""
.. module: historical.security_group.poller
    :platform: Unix
    :copyright: (c) 2017 by Netflix Inc., see AUTHORS for more
    :license: Apache, see LICENSE for more details.
.. author:: Kevin Glisson <kglisson@netflix.com>
"""
import os
import logging

from botocore.exceptions import ClientError

from raven_python_lambda import RavenLambdaWrapper
from cloudaux.aws.ec2 import describe_security_groups

from historical.common.sqs import get_queue_url, produce_events
from historical.constants import POLL_REGIONS, HISTORICAL_ROLE
from historical.security_group.models import security_group_polling_schema
from historical.common.accounts import get_historical_accounts

logging.basicConfig()
log = logging.getLogger("historical")
log.setLevel(logging.INFO)


@RavenLambdaWrapper()
def handler(event, context):
    """
    Historical Security Group Poller.

    This Poller is run at a set interval in order to ensure that changes do not go undetected by historical.

    Historical pollers generate `polling events` which simulate changes. These polling events contain configuration
    data such as the account/region defining where the collector should attempt to gather data from.
    """
    log.debug('Running poller. Configuration: {}'.format(event))

    queue_url = get_queue_url(os.environ.get('POLLER_QUEUE_NAME', 'HistoricalSecurityGroupPoller'))

    for account in get_historical_accounts():
        for region in POLL_REGIONS:
            try:
                groups = describe_security_groups(
                    account_number=account['id'],
                    assume_role=HISTORICAL_ROLE,
                    region=region
                )
                events = [security_group_polling_schema.serialize(account['id'], g) for g in groups['SecurityGroups']]
                produce_events(events, queue_url)

                log.debug('Finished generating polling events. Account: {}/{} '
                          'Events Created: {}'.format(account['id'], region, len(events)))
            except ClientError as e:
                log.warning('Unable to generate events for account/region. Account Id/Region: {account_id}/{region}'
                            ' Reason: {reason}'.format(account_id=account['id'], region=region, reason=e))
