# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class RoomRecordingList(ListResource):
    """  """

    def __init__(self, version, room_sid):
        """
        Initialize the RoomRecordingList

        :param Version version: Version that contains the resource
        :param room_sid: The room_sid

        :returns: twilio.rest.video.v1.room.recording.RoomRecordingList
        :rtype: twilio.rest.video.v1.room.recording.RoomRecordingList
        """
        super(RoomRecordingList, self).__init__(version)

        # Path Solution
        self._solution = {'room_sid': room_sid, }
        self._uri = '/Rooms/{room_sid}/Recordings'.format(**self._solution)

    def stream(self, status=values.unset, source_sid=values.unset,
               date_created_after=values.unset, date_created_before=values.unset,
               limit=None, page_size=None):
        """
        Streams RoomRecordingInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param RoomRecordingInstance.Status status: The status
        :param unicode source_sid: The source_sid
        :param datetime date_created_after: The date_created_after
        :param datetime date_created_before: The date_created_before
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.video.v1.room.recording.RoomRecordingInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(
            status=status,
            source_sid=source_sid,
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, status=values.unset, source_sid=values.unset,
             date_created_after=values.unset, date_created_before=values.unset,
             limit=None, page_size=None):
        """
        Lists RoomRecordingInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param RoomRecordingInstance.Status status: The status
        :param unicode source_sid: The source_sid
        :param datetime date_created_after: The date_created_after
        :param datetime date_created_before: The date_created_before
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.video.v1.room.recording.RoomRecordingInstance]
        """
        return list(self.stream(
            status=status,
            source_sid=source_sid,
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, status=values.unset, source_sid=values.unset,
             date_created_after=values.unset, date_created_before=values.unset,
             page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of RoomRecordingInstance records from the API.
        Request is executed immediately

        :param RoomRecordingInstance.Status status: The status
        :param unicode source_sid: The source_sid
        :param datetime date_created_after: The date_created_after
        :param datetime date_created_before: The date_created_before
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of RoomRecordingInstance
        :rtype: twilio.rest.video.v1.room.recording.RoomRecordingPage
        """
        params = values.of({
            'Status': status,
            'SourceSid': source_sid,
            'DateCreatedAfter': serialize.iso8601_datetime(date_created_after),
            'DateCreatedBefore': serialize.iso8601_datetime(date_created_before),
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return RoomRecordingPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of RoomRecordingInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of RoomRecordingInstance
        :rtype: twilio.rest.video.v1.room.recording.RoomRecordingPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return RoomRecordingPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a RoomRecordingContext

        :param sid: The sid

        :returns: twilio.rest.video.v1.room.recording.RoomRecordingContext
        :rtype: twilio.rest.video.v1.room.recording.RoomRecordingContext
        """
        return RoomRecordingContext(self._version, room_sid=self._solution['room_sid'], sid=sid, )

    def __call__(self, sid):
        """
        Constructs a RoomRecordingContext

        :param sid: The sid

        :returns: twilio.rest.video.v1.room.recording.RoomRecordingContext
        :rtype: twilio.rest.video.v1.room.recording.RoomRecordingContext
        """
        return RoomRecordingContext(self._version, room_sid=self._solution['room_sid'], sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Video.V1.RoomRecordingList>'


class RoomRecordingPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the RoomRecordingPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param room_sid: The room_sid

        :returns: twilio.rest.video.v1.room.recording.RoomRecordingPage
        :rtype: twilio.rest.video.v1.room.recording.RoomRecordingPage
        """
        super(RoomRecordingPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of RoomRecordingInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.video.v1.room.recording.RoomRecordingInstance
        :rtype: twilio.rest.video.v1.room.recording.RoomRecordingInstance
        """
        return RoomRecordingInstance(self._version, payload, room_sid=self._solution['room_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Video.V1.RoomRecordingPage>'


class RoomRecordingContext(InstanceContext):
    """  """

    def __init__(self, version, room_sid, sid):
        """
        Initialize the RoomRecordingContext

        :param Version version: Version that contains the resource
        :param room_sid: The room_sid
        :param sid: The sid

        :returns: twilio.rest.video.v1.room.recording.RoomRecordingContext
        :rtype: twilio.rest.video.v1.room.recording.RoomRecordingContext
        """
        super(RoomRecordingContext, self).__init__(version)

        # Path Solution
        self._solution = {'room_sid': room_sid, 'sid': sid, }
        self._uri = '/Rooms/{room_sid}/Recordings/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a RoomRecordingInstance

        :returns: Fetched RoomRecordingInstance
        :rtype: twilio.rest.video.v1.room.recording.RoomRecordingInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return RoomRecordingInstance(
            self._version,
            payload,
            room_sid=self._solution['room_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the RoomRecordingInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Video.V1.RoomRecordingContext {}>'.format(context)


class RoomRecordingInstance(InstanceResource):
    """  """

    class Status(object):
        PROCESSING = "processing"
        COMPLETED = "completed"
        DELETED = "deleted"
        FAILED = "failed"

    class Type(object):
        AUDIO = "audio"
        VIDEO = "video"
        DATA = "data"

    class Format(object):
        MKA = "mka"
        MKV = "mkv"

    class Codec(object):
        VP8 = "VP8"
        H264 = "H264"
        OPUS = "OPUS"
        PCMU = "PCMU"

    def __init__(self, version, payload, room_sid, sid=None):
        """
        Initialize the RoomRecordingInstance

        :returns: twilio.rest.video.v1.room.recording.RoomRecordingInstance
        :rtype: twilio.rest.video.v1.room.recording.RoomRecordingInstance
        """
        super(RoomRecordingInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'status': payload['status'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'sid': payload['sid'],
            'source_sid': payload['source_sid'],
            'size': deserialize.integer(payload['size']),
            'url': payload['url'],
            'type': payload['type'],
            'duration': deserialize.integer(payload['duration']),
            'container_format': payload['container_format'],
            'codec': payload['codec'],
            'grouping_sids': payload['grouping_sids'],
            'track_name': payload['track_name'],
            'room_sid': payload['room_sid'],
            'links': payload['links'],
        }

        # Context
        self._context = None
        self._solution = {'room_sid': room_sid, 'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: RoomRecordingContext for this RoomRecordingInstance
        :rtype: twilio.rest.video.v1.room.recording.RoomRecordingContext
        """
        if self._context is None:
            self._context = RoomRecordingContext(
                self._version,
                room_sid=self._solution['room_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def status(self):
        """
        :returns: The status
        :rtype: RoomRecordingInstance.Status
        """
        return self._properties['status']

    @property
    def date_created(self):
        """
        :returns: The date_created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def sid(self):
        """
        :returns: The sid
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def source_sid(self):
        """
        :returns: The source_sid
        :rtype: unicode
        """
        return self._properties['source_sid']

    @property
    def size(self):
        """
        :returns: The size
        :rtype: unicode
        """
        return self._properties['size']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def type(self):
        """
        :returns: The type
        :rtype: RoomRecordingInstance.Type
        """
        return self._properties['type']

    @property
    def duration(self):
        """
        :returns: The duration
        :rtype: unicode
        """
        return self._properties['duration']

    @property
    def container_format(self):
        """
        :returns: The container_format
        :rtype: RoomRecordingInstance.Format
        """
        return self._properties['container_format']

    @property
    def codec(self):
        """
        :returns: The codec
        :rtype: RoomRecordingInstance.Codec
        """
        return self._properties['codec']

    @property
    def grouping_sids(self):
        """
        :returns: The grouping_sids
        :rtype: dict
        """
        return self._properties['grouping_sids']

    @property
    def track_name(self):
        """
        :returns: The track_name
        :rtype: unicode
        """
        return self._properties['track_name']

    @property
    def room_sid(self):
        """
        :returns: The room_sid
        :rtype: unicode
        """
        return self._properties['room_sid']

    @property
    def links(self):
        """
        :returns: The links
        :rtype: unicode
        """
        return self._properties['links']

    def fetch(self):
        """
        Fetch a RoomRecordingInstance

        :returns: Fetched RoomRecordingInstance
        :rtype: twilio.rest.video.v1.room.recording.RoomRecordingInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the RoomRecordingInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Video.V1.RoomRecordingInstance {}>'.format(context)
