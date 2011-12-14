# -*- coding: utf-8 -*-

from zope.interface import implements
from eea.daviz.app.interfaces import IDavizConfig
from eea.daviz.app.handler import Configure 
from Products.CMFPlomino.PlominoUtils import asUnicode, asList

class PlominoDavizConfigure(Configure):
    """ Get daviz configuration
    """
    implements(IDavizConfig)
    
    def __init__(self, context):
        self.context = context

    def set_json(self, value):
        """ 
        """
        # we do not allow to set json as it is provided by the PlominoView
        # but we do need to overwrite the set_json provided by Configure
        pass

    def get_json(self):
        """ Return json from the PlominoView content
        """
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
                
        return {'items': data,
                'properties': dict([[col[0], {"valueType": col[1]}] for col in columns])} 

    json = property(get_json, set_json)
