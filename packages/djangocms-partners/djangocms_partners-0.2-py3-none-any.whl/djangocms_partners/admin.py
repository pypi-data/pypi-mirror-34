# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin, messages
from django.utils.translation import ugettext as _
from .models import Partner

admin.site.register(Partner)