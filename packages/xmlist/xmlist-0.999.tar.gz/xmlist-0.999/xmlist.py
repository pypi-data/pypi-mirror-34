
from __future__ import unicode_literals

import warnings
import sys

if sys.version_info[0] == 3: # pragma: no cover
    unicode = str
    long = int

dtd = {
    u'HTML 4.01 Strict':    u'<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">',
    u'HTML 4.01 Loose':     u'<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">',
    u'HTML 4.01 Frameset':  u'<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Frameset//EN" "http://www.w3.org/TR/html4/frameset.dtd">',
    u'HTML 5':              u'<!DOCTYPE html>',
    u'XHTML 1.0 Strict':    u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">',
    u'XHTML 1.0 Loose':     u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">',
    u'XHTML 1.0 Frameset':  u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Frameset//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-frameset.dtd">',
    u'XHTML 1.1':           u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">'
}

def PROCINS(mode, L):
    return u'<?%s?>' % u' '.join(serialize_ex(n, mode) for n in L)

def PROCINC(mode, L):
    warnings.warn('xmlist.PROCINC is deprecated; use xmlist.PROCINS instead')
    return PROCINS(mode, L)

def CDATA(mode, L):
    return u'<![CDATA[%s]]>' % u''.join(L)

def COMMENT(mode, L):
    return u'<!--%s-->' % u''.join(L)

def FRAGMENT(mode, L):
    return u''.join(serialize_ex(n, mode) for n in L)

def DOCTYPE(mode, L):
    return dtd[L[0]] + u'\n'

MODE_HTML = object()
MODE_XML = object()

MODE = MODE_XML

HTMLEMPTY = u'base link meta hr br embed param area col input'.split(' ')

# insert_ws(node, level=0)
#   if is_element(node) and has_1_child and child[0] is text:
#       return
#   for child in node[1:]:
#       prepend level+1 tabs
#   append level tabs
#   for child in child[1:]:
#       if is_element(child):
#           insert_ws(child, level+1)

def insert_ws(node, level=0, char='\t'):
    is_text = lambda n: isinstance(n, str) or isinstance(n, unicode) or \
                        isinstance(n, int) or isinstance(n, long)
    is_elem = lambda n: isinstance(n, list) and is_text(n[0])
    is_attr = lambda n: isinstance(n, tuple)
    is_frag = lambda n: isinstance(n, list) and (n[0] == FRAGMENT)
    is_procins = lambda n: isinstance(n, list) and (n[0] in [PROCINC, PROCINS])
    is_empty = lambda n: is_elem(n) and all(is_attr(ch) for ch in n[1:])
    node_no_attr = [ch for ch in node if not is_attr(ch)]
    if is_procins(node):
        return
    if is_elem(node) and len(node_no_attr) == 2 and is_text(node_no_attr[1]):
        return
    if is_frag(node):
        for n in node[1:]:
            insert_ws(n, level, char)
        return
    for i in range(len(node)-1, 0, -1):
        if not is_attr(node[i]):
            node.insert(i, u'\n' + char * (level + 1))
    if not is_empty(node):
        node.append(u'\n' + char * level)
    for i in range(len(node)-1, 0, -1):
        if is_elem(node[i]):
            insert_ws(node[i], level + 1, char)

def serialize_xml(node):
    return serialize_ex(node, MODE_XML)

def serialize_html(node):
    return serialize_ex(node, MODE_HTML)

def serialize(node): # pragma: no cover
    warnings.warn("xmlist.serialize is deprecated, please use serialize_xml or serialize_html instead")
    return serialize_ex(node, MODE)

def serialize_ex(node, mode):
    entities = u'&amp "quot <lt >gt' \
               if MODE == MODE_HTML \
               else u'&amp "quot \'apos <lt >gt'

    # text node
    if isinstance(node, str) or isinstance(node, unicode): 
        for r in entities.split(u' '):
            node = node.replace(r[0], u'&'+r[1:]+u';')
        return node

    # text node
    elif isinstance(node, long) or isinstance(node, int): 
        return str(node)

    # attribute node
    elif isinstance(node, tuple): 
        return u'%s="%s"' % (node[0], serialize_ex(node[1], mode))

    # element node
    if isinstance(node, list) and (isinstance(node[0], str) or isinstance(node[0], unicode)):
        name = node[0]
        nodes = [ (isinstance(n, tuple), serialize_ex(n, mode)) for n in node[1:] if n ]
        attrs = u' '.join(n for (isattr, n) in nodes if isattr)
        elems =  u''.join(n for (isattr, n) in nodes if not isattr)
        space = u' ' if attrs else u''

        if mode == MODE_HTML:
            if name in HTMLEMPTY:
                if elems:
                    raise ValueError(u'%s not empty' % name)
                return u'<%s%s%s>' % (name, space, attrs)
            else:
                return u'<%s%s%s>%s</%s>' % (name, space, attrs, elems, name)

        elif mode == MODE_XML:
            if elems:
                return u'<%s%s%s>%s</%s>' % (name, space, attrs, elems, name)
            else:
                return u'<%s%s%s/>' % (name, space, attrs)

        else:
            raise ValueError(u'mode %r not recognized' % mode)

    # some crazy other type of node like doctype, processing instruction or comment
    elif isinstance(node, list) and callable(node[0]):
        return node[0](mode, node[1:])

    # aah! wtf are you doing
    else:
        raise ValueError(repr(node))

def serialize_ws_xml(node, indent='\t'):
    return serialize_ws_ex(node, MODE_XML, indent)

def serialize_ws_html(node, indent='\t'):
    return serialize_ws_ex(node, MODE_HTML, indent)

def serialize_ws(node, indent='\t'): # pragma: no cover
    warnings.warn("xmlist.serialize_ws is deprecated, please use serialize_ws_xml or serialize_ws_html instead")
    return serialize_ws_ex(node, MODE, indent)

def serialize_ws_ex(node, mode, indent='\t'):
    insert_ws(node, char=indent)
    return serialize_ex(node, mode)

# <?procinc attr="?>"?>     PROCINC_START NAME WS NAME WS EQ DQ PROCINC_END
# <![CDATA[<text>]]>        CDATA_START CDATA
# <!--comment<foo>-->       COMMENT_START COMMENT COMMENT_END
# <elem/>                   LB NAME CRB
# <elem attr="/>"/>         LB NAME WS ATTRNAME EQUALS ATTRVALUE CRB
# <elem attr=">">foo &amp; bar</elem>
# <elem></elem>             LB NAME CB CLB NAME CRB
# foo &amp; bar             TEXT

#def parse(xml):
#    def parse(text, *rules):
#        for expr, tokenize in rules:
#            match = re.match(expr, xml, re.MULTILINE | re.DOTALL)
#            if match:
#                return tokenize(match.groups())
#
#    parse_elem = lambda xml: []
#    parse_node = lambda xml: parse(xml,
#                                   ('^<\?(.+?)\?>(.*)',          lambda m: [PROCINC] + parse_elem(m[0])),
#                                   ('^<!\[CDATA\[(.*?)]]>(.*)',  lambda m: [CDATA, m[0]]),
#                                   ('^<!--(.*?)-->(.*)',         lambda m: [COMMENT, m[0]]))
#
#    return parse_node(xml)

#if __name__ == '__main__':
#    doc = ['html',
#           ['head',
#            ['title', 'test document'],
#          ['link', ('rel', 'stylesheet'), ('type', 'text/css'), ('href', 'style.css')]],
#           ['body',
#            ['h1', 'test document'],
#            ['p', 'hi there', ['br'], 'this is a test'],
#            ['ul',
#             ['li', ['a', ('href', '/item1'), 'item 1']],
#             ['li', 'item 2'],
#             ['li', 'item 3']]]]
#    doc = ['html',
#           ['head'],
#           ['body',
#            ['div', ('id', 'Menu'),
#             [FRAGMENT,
#              ['h1', 'menu'],
#              ['ul', ('id', 'MenuList'),
#               ['li', ['a', ('href', '/release'), 'Releases']],
#               ['li', ['a', ('href', '/artist'), 'Artists']]]]]]]
#    doc = [FRAGMENT, [DOCTYPE, 'HTML 5'], doc]
#    MODE = MODE_HTML
#    print serialize(doc)
#    print
#    MODE = MODE_XML
#    print serialize(doc)
#    print
#    insert_ws(doc[2])
#    MODE = MODE_HTML
#    print serialize(doc)
#    print
#    MODE = MODE_XML
#    print serialize(doc)
#    print
