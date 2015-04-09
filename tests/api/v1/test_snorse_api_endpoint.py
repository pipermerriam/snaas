from django.core.urlresolvers import reverse

import snorse


def test_snorsing_some_text(api_client):
    url = reverse('v1:snorse')

    in_text = 'abc 123'
    expected_out = snorse.snorse(in_text)

    response = api_client.post(url, data=in_text, content_type='application/json')
    assert response.data == expected_out


def test_desnorsing_some_text(api_client):
    url = reverse('v1:desnorse')

    expected_text = 'abc 123'
    snorsed_text = snorse.snorse(expected_text)

    response = api_client.post(url, data=snorsed_text, content_type='application/json')
    assert response.data == expected_text
