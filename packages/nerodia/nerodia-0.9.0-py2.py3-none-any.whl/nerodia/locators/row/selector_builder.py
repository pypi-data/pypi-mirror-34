import logging

from ..element.selector_builder import SelectorBuilder as ElementSelectorBuilder
from ...exception import Error

try:
    from re import Pattern
except ImportError:
    from re import _pattern_type as Pattern


class SelectorBuilder(ElementSelectorBuilder):
    def _build_wd_selector(self, selectors):
        if any(isinstance(val, Pattern) for val in selectors.values()):
            return None

        if not selectors.pop('tag_name', None):
            raise Error('internal error: no tag_name?!')

        tag_name = self.query_scope.tag_name.lower()
        expressions = ['./tr']

        if tag_name not in ['tbody', 'tfoot', 'thead']:
            expressions += ['./tbody/tr', './thead/tr', './tfoot/tr']

        attr_expr = self.xpath_builder.attribute_expression(None, selectors)

        if attr_expr:
            expressions = ['{}[{}]'.format(e, attr_expr) for e in expressions]

        xpath = " | ".join(expressions)

        logging.debug({'build_wd_selector': xpath})

        return ['xpath', xpath]
