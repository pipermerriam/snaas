from django.core.urlresolvers import reverse

import snorse


def test_snorsing_some_text(client):
    url = reverse('snorse')

    in_text = 'abc 123'
    expected_out = snorse.snorse(in_text)

    response = client.post(
        url,
        data=in_text,
        content_type='application/octet-stream',
        HTTP_ACCEPT='application/vnd.snorse+txt; version=1.0.0',
    )
    assert unicode(response.content, encoding='utf8') == expected_out


def test_desnorsing_some_text(client):
    url = reverse('desnorse')

    expected_text = 'abc 123'
    snorsed_text = snorse.snorse(expected_text)

    response = client.post(
        url,
        data=snorsed_text,
        content_type='application/octet-stream',
        HTTP_ACCEPT='application/vnd.snorse+txt; version=1.0.0',
    )
    assert response.content == expected_text


def test_snorsing_some_text_with_missing_version(client):
    url = reverse('snorse')

    in_text = 'abc 123'
    expected_out = snorse.snorse(in_text)

    response = client.post(
        url,
        data=in_text,
        content_type='application/octet-stream',
        HTTP_ACCEPT='application/vnd.snorse+txt',
    )
    assert unicode(response.content, encoding='utf8') == expected_out


def test_snorsing_some_text_with_bad_version(client):
    url = reverse('snorse')

    in_text = 'abc 123'

    response = client.post(
        url,
        data=in_text,
        content_type='application/octet-stream',
        HTTP_ACCEPT='application/vnd.snorse+txt; version=0.1.0',
    )
    assert response.status_code == 406
