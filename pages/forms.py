from django import forms


class ContactForm(forms.Form):
	name = forms.CharField(max_length=100, required=True)
	email = forms.EmailField()
	subject = forms.CharField(max_length=50)
	message = forms.CharField(widget=forms.Textarea)

	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)

		for x, y in self.fields.items():
			y.widget.attrs.update({'class': 'input'})

	def get_details(self):
		"""
		Method that returns formatted
		information :return: subject, message
		"""

		clean_data = super().clean()

		name = clean_data.get('name').strip()
		from_email = clean_data.get('email')
		subject = clean_data.get('subject')

		msg = f'{name} with email {from_email} said:'
		msg += f'\n"{subject}"\n\n'
		msg += clean_data.get('message')

		return subject, msg
