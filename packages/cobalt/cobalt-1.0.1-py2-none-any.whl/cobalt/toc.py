import re
from lxml.html import _collect_string_content


class TOCBuilder(object):
    """ This builds a Table of Contents for an Act.

    A Table of Contents is a tree of :class:`TOCElement` instances, each element
    representing an item of interest in the Table of Contents. Each item
    has attributes useful for presenting a Table of Contents, such as a type
    (chapter, part, etc.), a number, a heading and further child elements.

    The TOC is assembled from certain tags in the document, see ``toc_components``.

    The Table of Contents can also be used to lookup the XML element corresponding
    to an item in the Table of Contents identified by its subcomponent path.
    This is useful when handling URIs such as ``.../eng/main/section/1`` or
    ``.../eng/main/part/C``. See :meth:`cobalt.act.Act.get_subcomponent`.

    Some components can be uniquely identified by their type and number, such as
    ``Section 2``. Others require context, such as ``Part 2 of Chapter 1``. The
    latter are controlled by ``toc_non_unique_elements``.

    The easiest way to build a Table of Contents is with :meth:`cobalt.act.Act.table_of_contents`.
    """
    # elements we include in the table of contents
    toc_components = ['coverpage', 'preface', 'preamble', 'part', 'chapter', 'section', 'conclusions']

    # These TOC elements aren't numbered uniquely throughout the document
    # and will need their parent components for context
    toc_non_unique_components = ['chapter', 'part']

    # eg. schedule1
    component_id_re = re.compile('([^0-9]+)([0-9]+)')

    def table_of_contents(self, act):
        """ Get the table of contents of ``act`` as a list of :class:`TOCElement` instances. """
        interesting = set('{%s}%s' % (act.namespace, s) for s in self.toc_components)

        def generate_toc(component, elements, parent=None):
            items = []
            for e in elements:
                if e.tag in interesting:
                    item = self.element(e, component, parent=parent)
                    item.children = generate_toc(component, e.iterchildren(), parent=item)
                    items.append(item)
                else:
                    items += generate_toc(component, e.iterchildren())
            return items

        toc = []
        for component, element in act.components().iteritems():
            if component != "main":
                # non-main components are items in their own right
                item = self.element(element, component)
                item.children = generate_toc(component, [element])
                toc += [item]
            else:
                toc += generate_toc(component, [element])

        return toc

    def element(self, element, component, parent=None):
        type_ = element.tag.split('}', 1)[-1]
        id_ = element.get('id')

        if type_ == 'doc':
            # component, get the title from the alias
            heading = element.find('./{*}meta//{*}FRBRalias')
            if heading is not None:
                heading = heading.get('value')
            else:
                # eg. schedule1 -> Schedule 1
                m = self.component_id_re.match(component)
                if m:
                    heading = ' '.join(m.groups()).capitalize()
                else:
                    heading = component.capitalize()
        else:
            try:
                heading = _collect_string_content(element.heading)
            except AttributeError:
                heading = None

        try:
            num = element.num
        except AttributeError:
            num = None

        num = num.text if num else None

        if type_ == "doc":
            subcomponent = None
        else:
            # if we have a chapter/part as a child of a chapter/part, we need to include
            # the parent as context because they aren't unique, eg: part/1/chapter/2
            if type_ in self.toc_non_unique_components and parent and parent.type in self.toc_non_unique_components:
                subcomponent = parent.subcomponent + "/"
            else:
                subcomponent = ""

            # eg. 'preamble' or 'chapter/2'
            subcomponent += type_

            if num:
                subcomponent += '/' + num.strip('.()')

        return TOCElement(element, component, type_, heading=heading, id_=id_,
                          num=num, subcomponent=subcomponent, parent=parent)


class TOCElement(object):
    """
    An element in the table of contents of a document, such as a chapter, part or section.

    :ivar children: further TOC elements contained in this one, may be None or empty
    :ivar element: :class:`lxml.objectify.ObjectifiedElement` the XML element of this TOC element
    :ivar heading: heading for this element, excluding the number, may be None
    :ivar id: XML id string of the node in the document, may be None
    :ivar num: number of this element, as a string, may be None
    :ivar component: number of the component that this item is a part of, as a string
    :ivar subcomponent: name of this subcomponent, used by :meth:`cobalt.act.Act.get_subcomponent`, may be None
    :ivar type: element type, one of: ``chapter, part, section`` etc.
    """

    def __init__(self, element, component, type_, heading=None, id_=None, num=None, subcomponent=None, parent=None, children=None):
        self.element = element
        self.component = component
        self.type = type_
        self.heading = heading
        self.id = id_
        self.num = num
        self.children = children
        self.subcomponent = subcomponent
        self.title = self.friendly_title()

    def as_dict(self):
        info = {
            'type': self.type,
            'component': self.component,
            'subcomponent': self.subcomponent,
            'title': self.title,
        }

        if self.heading:
            info['heading'] = self.heading

        if self.num:
            info['num'] = self.num

        if self.id:
            info['id'] = self.id

        if self.children:
            info['children'] = [c.as_dict() for c in self.children]

        return info

    def friendly_title(self):
        """ Build a friendly title for this, based on heading names etc.
        """
        if self.type in ['chapter', 'part']:
            title = self.type.capitalize()
            if self.num:
                title += ' ' + self.num
            if self.heading:
                title += ' - ' + self.heading

        elif self.type == 'section':
            if self.heading:
                title = self.heading
                if self.num:
                    title = self.num + ' ' + title
            else:
                title = 'Section'
                if self.num:
                    title = title + ' ' + self.num

        elif self.heading:
            title = self.heading

        else:
            title = self.type.capitalize()
            if self.num:
                title += u' ' + self.num

        return title
