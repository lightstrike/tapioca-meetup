# coding: utf-8

"""
TODO: Add the following to mapping:
    * /pro
    * /photos
    * /oembed
    * /notifcations
    * /status
    * /comments
    * v2 & v3 groups
    * /activity
    * v2 & v3 events
    * /dashboard
    * /2/cities
    * /2/categories
    * boards
    * batch
    * abuse
"""

RESOURCE_MAPPING = {
    'venues_list': {
        'resource': '/2/venues',
        'docs': 'http://www.meetup.com/meetup_api/docs/2/venues',
    },
    'open_venues': {
        'resource': '/2/open_venues',
        'docs': 'http://www.meetup.com/meetup_api/docs/2/open_venues',
    },
    'recommended_venues': {
        'resource': '/recommended/venues',
        'docs': 'http://www.meetup.com/meetup_api/docs/recommended/venues',
    },
    'group_venues': {
        'resource': '/{group_url}/venues',
        'docs': 'http://www.meetup.com/meetup_api/docs/:urlname/venues',
    },
    'topics': {
        'resource': '/topics',
        'docs': 'http://www.meetup.com/meetup_api/docs/topics',
    },
    'topic_categories': {
        'resource': '/2/topic_categories',
        'docs': 'http://www.meetup.com/meetup_api/docs/2/topic_categories',
    },
    'recommended_topics': {
        'resource': '/recommended/group_topics',
        'docs': 'http://www.meetup.com/meetup_api/docs/recommended/group_topics',
    },
    'open_events': {
        'resource': '/2/open_events',
        'docs': 'http://www.meetup.com/meetup_api/docs/2/open_events/',
    },
    'rsvps_list': {
        'resource': '/2/rsvps',
        'docs': 'http://www.meetup.com/meetup_api/docs/2/rsvps/',
    },
    'rsvp_detail': {
        'resource': '/rsvp/{id}',
        'docs': 'http://www.meetup.com/meetup_api/docs/rsvp/:id',
    },
    'profiles_list': {
        'resource': '/2/profiles',
        'docs': 'http://www.meetup.com/meetup_api/docs/2/profiles',
    },
    'create_profile': {
        'resource': '/2/profile',
        'docs': 'http://www.meetup.com/meetup_api/docs/2/profile',
    },
    'profile_detail': {
        'resource': '/2/profile/{group_id}/{member_id}',
        'docs': 'http://www.meetup.com/meetup_api/docs/:gid/:mid',
    },
    'members_list': {
        'resource': '/2/members',
        'docs': 'http://www.meetup.com/meetup_api/docs/2/members',
    },
    'member_detail': {
        'resource': '/2/member/{id}',
        'docs': 'http://www.meetup.com/meetup_api/docs/2/member/:id',
    },
    'upload_member_photo': {
        'resource': '/2/member_photo',
        'docs': 'http://www.meetup.com/meetup_api/docs/2/member_photo',
    },
    'delete_member_photo': {
        'resource': '/2/member_photo/{id}',
        'docs': 'http://www.meetup.com/meetup_api/docs/2/member_photo/:id',
    },
    'member_profile': {
        'resource': '/members/{member_id}',
        'docs': 'http://www.meetup.com/meetup_api/docs/members/:member_id',
    },
    'group_member_profile': {
        'resource': '/{group_url}/members/{member_id}',
        'docs': 'http://www.meetup.com/meetup_api/docs/:urlname/members/:member_id',
    },
    'member_approval': {
        'resource': '/{group_url}/member/approvals',
        'docs': 'http://www.meetup.com/meetup_api/docs/:urlname/member/approvals',
    },
    '': {
        'resource': '/',
        'docs': 'http://www.meetup.com/meetup_api/docs/',
    },
}
