from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control custom-input', 'placeholder': 'Nome'}),
        error_messages={'required': 'Por favor, insira seu nome.'}
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control custom-input', 'placeholder': 'Email'}),
        error_messages={
            'required': 'Por favor, insira seu e-mail.',
            'invalid': 'Por favor, insira um e-mail válido.'
        }
    )
    phone = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control custom-input', 'placeholder': 'Telefone'}),
        error_messages={'required': 'Por favor, insira seu telefone.'}
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control custom-textarea', 'placeholder': 'Mensagem'}),
        error_messages={'required': 'Por favor, insira sua mensagem.'}
    )

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        phone = cleaned_data.get('phone')
        message = cleaned_data.get('message')

        # Custom validation if needed
        if not (name and email and phone and message):
            raise forms.ValidationError('Todos os campos devem ser preenchidos.')

        return cleaned_data
