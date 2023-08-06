# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _
# from autoslug import AutoSlugField
from filer.fields.image import FilerImageField
from djangocms_text_ckeditor.fields import HTMLField

class Partner(models.Model):
    #Partners"
    order = models.IntegerField(_('Order'), default=0)
    name = models.CharField(_('Name'), max_length=200)# (requis)
    logo = FilerImageField(related_name="parnter_logo", null=True,blank=True, verbose_name=_("logo"))
    link = models.URLField(_("Website link"), null=True, blank=True)

    class Meta:
        verbose_name = _("Partner")
        verbose_name_plural = _("Partners")

    def __unicode__(self):
        return self.__str__(self)

    def __str__(self):
        return self.name