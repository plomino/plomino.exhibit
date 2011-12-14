# -*- coding: utf-8 -*-

from eea.daviz.converter.browser import DavizPublicSupport

from Products.statusmessages.interfaces import IStatusMessage

from eea.daviz.converter.interfaces import IExhibitJsonConverter
from eea.daviz.events import DavizEnabledEvent
from eea.daviz.interfaces import IDavizConfig
from eea.daviz.subtypes.interfaces import IDavizSubtyper

from zope.component import queryAdapter, queryUtility
from zope.event import notify
from zope.interface import alsoProvides, noLongerProvides, implements

from Products.CMFPlomino.PlominoUtils import asUnicode, asList

from interfaces import IPlominoExhibitJson
    
class PlominoDavizSupport(DavizPublicSupport):
    """ Enable/Disable Exhibit
    """

    @property
    def can_enable(self):
        """ See IDavizSubtyper
        """
        return not self.is_exhibit

    @property
    def can_disable(self):
        """ See IDavizSubtyper
        """
        return self.is_exhibit

    @property
    def is_exhibit(self):
        """ Is exhibit viewable?
        """
        return IPlominoExhibitJson.providedBy(self.context)

    def enable(self):
        """ Enable Exhibit
        """
        columns = self.get_columns()

        if not IPlominoExhibitJson.providedBy(self.context):
            alsoProvides(self.context, IPlominoExhibitJson)

        notify(DavizEnabledEvent(self.context, columns=columns))
        return self._redirect('Enabled Exhibit view')

    def disable(self):
        """ Disable Exhibit
        """
        noLongerProvides(self.context, IPlominoExhibitJson)
        return self._redirect('Removed Exhibit view', to='')

    def get_columns(self):
        columnids = [col.id for col in self.context.getColumns() if not getattr(col, 'HiddenColumn', False)]
        columns = []
        for colid in columnids:
            if '$' in colid:
                (id, type) = colid.split('$')
                columns.append([id, type])
            else:
                columns.append([colid, 'text'])
        return columns 
