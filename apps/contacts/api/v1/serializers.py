from rest_framework import serializers

from contacts.models import ContactUs


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = (
            'subject',
            'name',
            'email_from',
            'message',
        )

    def _send_mail(self, validated_data):
        subject = 'User ContactUs'
        message = f'''
                Request from: {validated_data['name']},
                Reply to: {validated_data['email']},
                Subject: {validated_data['subject']},
                Message: {validated_data['message']},
                '''
        from contacts.tasks import send_mail
        send_mail.delay(subject, message)

    def create(self, validated_data):
        self._send_mail(validated_data)
        return ContactUs.objects.create(**validated_data)
