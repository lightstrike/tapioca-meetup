# coding: utf-8

RESOURCE_MAPPING = {
    'api_status': {
        'resource': '/status',
        'docs': 'http://www.meetup.com/meetup_api/docs/status',
    },
    'pro_groups': {
        'resource': '/pro/{group_url}/groups',
        'docs': 'http://www.meetup.com/meetup_api/docs/pro/:urlname/groups',
    },
    'pro_members': {
        'resource': '/pro/{group_url}/members',
        'docs': 'http://www.meetup.com/meetup_api/docs/pro/:urlname/members',
    },
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
    'events_list': {
        'resource': '/2/events',
        'docs': 'http://www.meetup.com/meetup_api/docs/2/events/',
    },
    'create_event': {
        'resource': '/2/event',
        'docs': 'http://www.meetup.com/meetup_api/docs/2/event/',
    },
    'event_attendance': {
        'resource': '/{group_url}/events/{event_id}/attendance',
        'docs': 'http://www.meetup.com/meetup_api/docs/:urlname/events/:id/attendance',
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
        'docs': 'http://www.meetup.com/meetup_api/docs/:urlname/member/approvals/#create',
    },
    'member_block_status': {
        'resource': '/self/blocks/{member_id}',
        'docs': 'http://www.meetup.com/meetup_api/docs/self/blocks/:member_id',
    },
    'report_abuse': {
        'resource': '/self/abuse_reports',
        'docs': 'http://www.meetup.com/meetup_api/docs/self/abuse_reports',
    },
    'report_group_abuse': {
        'resource': '/{group_url}/abuse_reports',
        'docs': 'http://www.meetup.com/meetup_api/docs//:urlname/abuse_reports',
    },
    'batch_request': {
        'resource': '/batch',
        'docs': 'http://www.meetup.com/meetup_api/docs/batch',
    },
    'discussion_boards': {
        'resource': '/{group_url}/boards',
        'docs': 'http://www.meetup.com/meetup_api/docs/:urlname/boards',
    },
    'discussions': {
        'resource': '/{group_url}/boards/{board_id}/discussions',
        'docs': 'http://www.meetup.com/meetup_api/docs/:urlname/boards/:bid/discussions',
    },
    'discussion_posts': {
        'resource': '/{group_url}/boards/{board_id}/discussions/{discussion_id}',
        'docs': 'http://www.meetup.com/meetup_api/docs/:urlname/boards/:bid/discussions/:did',
    },
    'categories': {
        'resource': '/2/categories',
        'docs': 'http://www.meetup.com/meetup_api/docs/2/categories',
    },
    'cities': {
        'resource': '/2/cities',
        'docs': 'http://www.meetup.com/meetup_api/docs/2/cities',
    },
    'dashboard': {
        'resource': '/dashboard',
        'docs': 'http://www.meetup.com/meetup_api/docs/dashboard',
    },
    'member_events': {
        'resource': '/self/events',
        'docs': 'http://www.meetup.com/meetup_api/docs/self/events',
    },
    'event_detail': {
        'resource': '/{group_url}/events/{event_id}',
        'docs': 'http://www.meetup.com/meetup_api/docs/:urlname/events/:id',
    },
    'event_change': {
        'resource': '/2/events/{event_id}',
        'docs': 'http://www.meetup.com/meetup_api/docs/2/events/:id',
    },
    'event_payments': {
        'resource': '/{group_url}/events/{event_id}/payments',
        'docs': 'http://www.meetup.com/meetup_api/docs/:urlname/events/:id/payments',
    },
    'event_watchlist': {
        'resource': '/{group_url}/events/{event_id}/watchlist',
        'docs': 'http://www.meetup.com/meetup_api/docs/:urlname/events/:id/watchlist',
    },
    'event_comments': {
        'resource': '/2/event_comments',
        'docs': 'http://www.meetup.com/meetup_api/docs/2/event_comments',
    },
    'create_event_comment': {
        'resource': '/2/event_comment',
        'docs': 'http://www.meetup.com/meetup_api/docs/2/event_comment',
    },
    'event_comment_detail': {
        'resource': '/2/event_comment/{comment_id}',
        'docs': 'http://www.meetup.com/meetup_api/docs/2/event_comment/:id',
    },
    'flag_event_comment': {
        'resource': '/2/event_comment_flag',
        'docs': 'http://www.meetup.com/meetup_api/docs/2/event_comment_flag',
    },
    'subscribe_to_event_comment': {
        'resource': '/2/event_comment_subscribe/{comment_id}',
        'docs': 'http://www.meetup.com/meetup_api/docs/2/event_comment_subscribe/:id',
    },
    'like_event_comment': {
        'resource': '/2/event_comment_like/{commet_id}',
        'docs': 'http://www.meetup.com/meetup_api/docs/2/event_comment_like/:id',
    },
    'event_comment_likes': {
        'resource': '/2/event_comment_likes',
        'docs': 'http://www.meetup.com/meetup_api/docs/2/event_comment_likes',
    },
    'event_ratings_list': {
        'resource': '/2/event_ratings',
        'docs': 'http://www.meetup.com/meetup_api/docs/2/event_ratings',
    },
    'event_rating_detail': {
        'resource': '/2/event_rating',
        'docs': 'http://www.meetup.com/meetup_api/docs/2/event_rating',
    },
    'concierge': {
        'resource': '/2/concierge',
        'docs': 'http://www.meetup.com/meetup_api/docs/2/concierge',
    },
    'activity_feed': {
        'resource': '/activity',
        'docs': 'http://www.meetup.com/meetup_api/docs/activity',
    },
    'find_groups': {
        'resource': '/find/groups',
        'docs': 'http://www.meetup.com/meetup_api/docs/find/groups',
    },
    'groups_list': {
        'resource': '/2/groups',
        'docs': 'http://www.meetup.com/meetup_api/docs/2/groups',
    },
    'upload_group_photo': {
        'resource': '/2/group_photo',
        'docs': 'http://www.meetup.com/meetup_api/docs/2/group_photo',
    },
    'group_detail': {
        'resource': '/{group_url}',
        'docs': 'http://www.meetup.com/meetup_api/docs/:urlname',
    },
    'group_topics': {
        'resource': '/{group_url}/topics',
        'docs': 'http://www.meetup.com/meetup_api/docs/:urlname/topics',
    },
    'recommended_groups': {
        'resource': '/recommended/groups',
        'docs': 'http://www.meetup.com/meetup_api/docs/recommended/groups',
    },
    'ignore_recommended_group': {
        'resource': '/recommended/groups/ignores/{group_url}',
        'docs': 'http://www.meetup.com/meetup_api/docs/recommended/groups/ignores/:urlname',
    },
    'find_similar_groups': {
        'resource': '/{group_url}/similar_groups',
        'docs': 'http://www.meetup.com/meetup_api/docs/:urlname/similar_groups',
    },
    'group_comments': {
        'resource': '/comments',
        'docs': 'http://www.meetup.com/meetup_api/docs/comments',
    },
    'notifications_list': {
        'resource': '/notifications',
        'docs': 'http://www.meetup.com/meetup_api/docs/notifications',
    },
    'mark_notifications_as_read': {
        'resource': '/notifications/read',
        'docs': 'http://www.meetup.com/meetup_api/docs/notifications/read',
    },
    'group_oembed': {
        'resource': '/oembed',
        'docs': 'http://www.meetup.com/meetup_api/docs/oembed',
    },
    'photo_albums_list': {
        'resource': '/2/photo_albums',
        'docs': 'http://www.meetup.com/meetup_api/docs/2/photo_albums',
    },
    'create_photo_album': {
        'resource': '/2/photo_album',
        'docs': 'http://www.meetup.com/meetup_api/docs/2/photo_album',
    },
    'photo_albums_photos_list': {
        'resource': '/:urlname/photo_albums/:album_id/photos',
        'docs': 'http://www.meetup.com/meetup_api/docs/:urlname/photo_albums/:album_id/photos',
    },
    'photo_album_detail': {
        'resource': '/:urlname/photo_albums/:album_id',
        'docs': 'http://www.meetup.com/meetup_api/docs/:urlname/photo_albums/:album_id',
    },
    'event_photos_list': {
        'resource': '/:urlname/events/:event_id/photos',
        'docs': 'http://www.meetup.com/meetup_api/docs/:urlname/events/:event_id/photos',
    },
    'event_photo_detail': {
        'resource': '/:urlname/events/:event_id/photos/:photo_id',
        'docs': 'http://www.meetup.com/meetup_api/docs/:urlname/events/:event_id/photos/:photo_id',
    },
    'photo_comments_list': {
        'resource': '/2/photo_comments',
        'docs': 'http://www.meetup.com/meetup_api/docs/2/photo_comments',
    },
    'create_photo_comment': {
        'resource': '/2/photo_comment',
        'docs': 'http://www.meetup.com/meetup_api/docs/2/photo_comment',
    },
    'delete_photo_comment': {
        'resource': '/:urlname/events/:event_id/photos/:photo_id/comments/:comment_id',
        'docs': 'http://www.meetup.com/meetup_api/docs/:urlname/events/:event_id/photos/:photo_id/comments/:comment_id',
    },
    'upload_event_photo': {
        'resource': '/2/photo',
        'docs': 'http://www.meetup.com/meetup_api/docs/2/photo',
    },
    'manage_event_photo': {
        'resource': '/2/photo/{photo_id}',
        'docs': 'http://www.meetup.com/meetup_api/docs/2/photo/:id',
    },
}
