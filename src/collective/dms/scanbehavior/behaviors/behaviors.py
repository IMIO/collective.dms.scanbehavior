from zope.interface import alsoProvides
from zope import schema
from Products.CMFPlone.utils import base_hasattr
from plone.autoform.interfaces import IFormFieldProvider
from plone.indexer import indexer
from plone.supermodel import model
from collective.dms.scanbehavior import _


class IScanFields(model.Schema):

    model.fieldset(
        'scan',
        label=_(u'Scan'),
        fields=(
            'scan_id',
            'pages_number',
            'scan_date',
            'scan_user',
            'scanner',
        ),
    )

    scan_id = schema.TextLine(
        title=_(
            u'scan_id',
            default=u'Scan id',
        ),
        required=False,
    )

    pages_number = schema.Int(
        title=_(
            u'pages_number',
            default=u'Pages numbers',
        ),
        required=False,
    )

    scan_date = schema.Datetime(
        title=_(
            u'scan_date',
            default=u'Scan date',
        ),
        required=False,
    )

    scan_user = schema.TextLine(
        title=_(
            u'scan_user',
            default=u'Scan user',
        ),
        required=False,
    )

    scanner = schema.TextLine(
        title=_(
            u'scanner',
            default=u'scanner',
        ),
        required=False,
    )

alsoProvides(IScanFields, IFormFieldProvider)


@indexer(IScanFields)
def scan_id_indexer(obj):
    """
        indexer method
    """
    if base_hasattr(obj, 'scan_id'):
        return obj.scan_id
