from jsl.scope import ResolutionScope


def test_scope():
    scope = ResolutionScope()
    id, scope = scope.alter('q')
    assert id == 'q'
    id, scope = scope.alter('w')
    assert id == 'w'

    assert scope._base == ''
    assert scope._current == 'w'
    assert scope._output == 'w'

    scope = ResolutionScope(base='http://example.com/#garbage')
    assert scope.create_ref('a') == {'$ref': '#/definitions/a'}
    id, scope = scope.alter('schema/')
    assert id == 'http://example.com/schema/'
    assert scope.create_ref('a') == {'$ref': 'http://example.com/#/definitions/a'}
    id, scope = scope.alter('subschema.json')
    assert id == 'subschema.json'
    id, scope = scope.alter('#hash')
    assert id == '#hash'

    assert scope._base == 'http://example.com/'
    assert scope._current == scope._output == 'http://example.com/schema/subschema.json'
