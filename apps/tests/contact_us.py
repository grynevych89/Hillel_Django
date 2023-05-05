# from contacts.models import ContactUs


def test_get_contact_us(client):
    response = client.get('/contacts/contact/create/')
    assert response.status_code == 200


def test_post_empty_form_200(client):
    response = client.post('/contacts/contact/create/')
    assert response.status_code == 200


def test_post_empty_form_errors(client):
    response = client.post('/contacts/contact/create/')
    assert response.context_data['form']._errors == {
        'name': ['This field is required.'],
        'email_from': ['This field is required.'],
        'subject': ['This field is required.'],
    }


def test_post_invalid_email_200(client):
    payload = {
        'name': 'Grynevych',
        'email': 'INVALID_EMAIL',
        'subject': 'This field is required.',
        'message': 'This field is required.'
    }
    response = client.post('/contacts/contact/create/', data=payload)
    assert response.status_code == 200


def test_post_invalid_email_error(client):
    payload = {
        'name': 'Mykola',
        'email_from': 'INVALID_EMAIL',
        'subject': 'This field is required.',
        'message': 'This field is required.'
    }
    response = client.post('/contacts/contact/create/', data=payload)
    assert response.context_data['form']._errors == {'email_from': ['Enter a valid email address.']}


# def test_post_valid_data(client, mailoutbox, settings):
#     initial_count = ContactUs.objects.count()
#     payload = {
#         'name': 'Grynevych',
#         'email': 'example@example.com',
#         'subject': 'This field is required.',
#     }
#     response = client.post('/contacts/contact/create/', data=payload)
#     assert response.status_code == 302
#     assert response['location'] == '/'
#     assert ContactUs.objects.count() == initial_count + 1
#     assert len(mailoutbox) == 1
#     assert mailoutbox[0].from_email == settings.DEFAULT_FROM_EMAIL
