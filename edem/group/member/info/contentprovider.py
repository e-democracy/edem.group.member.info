# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from zope.cachedescriptors.property import Lazy
from zope.component import createObject
from zope.contentprovider.interfaces import UpdateNotCalled
from zope.pagetemplate.pagetemplatefile import PageTemplateFile
from Products.XWFCore.XWFUtils import get_user
from Products.CustomUserFolder.interfaces import IGSUserInfo
from gs.group.base import GroupContentProvider


class PoliciesInfoContentProvider(GroupContentProvider):
    '''Provides methods to access group policy information'''

    pageTemplateFileName = "browser/templates/policiesInfoContentProvider.pt"

    def __init__(self, context, request, view):
        super(PoliciesInfoContentProvider, self).__init__(context, request,
                                                          view)
        self.updated = False

    @Lazy
    def forumManager(self):
        uid = getattr(self.context, 'ptn_coach_id', '')
        userInfo = None

        if uid:
            user = get_user(self.context, uid)
            if user:
                userInfo = IGSUserInfo(user)

        return userInfo

    @Lazy
    def mailingList(self):
        retval = createObject('groupserver.MailingListInfo', self.context)
        assert retval
        return retval

    @Lazy
    def postRateLimit(self):
        groupList = self.mailingList.mlist
        senderlimit = groupList.getProperty('senderlimit')
        senderinterval = groupList.getProperty('senderinterval', 86400)

        if senderlimit is not None:
            # convert 'old' system to posts per second, then per day (rounded)
            postsPerSecond = float(senderlimit)/float(senderinterval)
            postsPerDay = int(postsPerSecond*86400)
        else:
            postsPerDay = None

        return postsPerDay

    def update(self):
        self.updated = True
        self.pageTemplate = PageTemplateFile(self.pageTemplateFileName)

    def render(self):
        if not self.updated:
            raise UpdateNotCalled
        return self.pageTemplate(view=self)
