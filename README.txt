==============================
``edem.group.member.info``
==============================
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Customization of the Group Membership viewlets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Author: `Bill Bushey`_
:Contact: Bill Bushey <bill.bushey@e-democracy.org>
:Date: 2014-03-15
:Organization: `E-Democracy.org`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 3.0 License`_
  by `E-Democracy.org`_.

Introduction
===========

This product customizes parts of the Group Membership viewlets provided by
`gs.group.member.info`_. Currently, it defines the **E-Democracy Policies Info
Content Provider** and this content provider to the Logged-In Member, Public
Group, and Private Group membership viewlets.

E-Democracy Policies Info Group Content Provider
================================================

A simple group content provider named **edem.PoliciesInfo** that produces two
unordered lists:

- The first list provides (if applicable) information about who the manager of
  the group is, how to contact the forum manager, and how many times in a 24
  hour period members can post
  
  - The email address displayed for the forum manager is defined by the 
    **fm_email_address** property of the group. If this property is not set,
    no email address will be displayed.

- The second list provides links to the policy documents of the group and site

To add this content provider to a view, place the following into the view's
template:

  <div tal:replace="structure provider:edem.PoliciesInfo"/>

Resources
=========

- Code repository: https://github.com/e-democracy/edem.group.member.info 
- Questions and comments to http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/edem

.. _GroupServer: http://groupserver.org/
.. _E-Democracy.org: http://e-democracy.org/
.. _Bill Bushey: http://groupserver.org/p/wbushey
.. _Creative Commons Attribution-Share Alike 3.0 License:
   http://creativecommons.org/licenses/by-sa/3.0/
.. _gs.group.member.info:
   https://source.iopen.net/groupserver/gs.group.member.info/summary
