# -*- coding: utf-8 -*-

from eea.daviz.converter.browser import DavizPublicSupport

from Products.statusmessages.interfaces import IStatusMessage

from eea.daviz.converter.interfaces import IExhibitJsonConverter
from eea.daviz.events import DavizEnabledEvent
from eea.daviz.interfaces import IDavizConfig, IExhibitJson
from eea.daviz.subtypes.interfaces import IDavizSubtyper

from zope.component import queryAdapter, queryUtility
from zope.event import notify
from zope.interface import alsoProvides, noLongerProvides, implements

from Products.CMFPlomino.PlominoUtils import asUnicode, asList

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
        return IExhibitJson.providedBy(self.context)

    def enable(self):
        """ Enable Exhibit
        """
#        try:
        columns, json = self.extract_data()
#        except Exception, err:
#            return self._redirect(('An error occured while trying to convert '
#                                   'the Plomino view content'), 'view')

        if not IExhibitJson.providedBy(self.context):
            alsoProvides(self.context, IExhibitJson)

        # Update annotations
        mutator = queryAdapter(self.context, IDavizConfig)
        mutator.json = json
        notify(DavizEnabledEvent(self.context, columns=columns))
        return self._redirect('Enabled Exhibit view')

    def disable(self):
        """ Disable Exhibit
        """
        noLongerProvides(self.context, IExhibitJson)
        return self._redirect('Removed Exhibit view', to='')

    def extract_data(self):
        data = []

        columnids = [col.id for col in self.context.getColumns() if not getattr(col, 'HiddenColumn', False)]
        for b in self.context.getAllDocuments(getObject=False):
            row = {'label': b.id}
            for colid in columnids:
                v = getattr(b, self.context.getIndexKey(colid), '')
                if isinstance(v, list):
                    v = [asUnicode(e).encode('utf-8').replace('\r', '') for e in v]
                else:
                    v = asUnicode(v).encode('utf-8').replace('\r', '')
                row[colid.split('$')[0]] = v or ''

            data.append(row)
        
        columns = []
        for colid in columnids:
            if '$' in colid:
                (id, type) = colid.split('$')
                columns.append([id, type])
            else:
                columns.append([colid, 'text'])
        return columns, {'items': data,
                    'properties': dict([[col[0], {"valueType": col[1]}] for col in columns])} 
