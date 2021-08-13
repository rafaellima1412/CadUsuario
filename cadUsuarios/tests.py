from cadUsuarios.models import Usuario
from django.test import TestCase

class UsuarioListTestCase(TestCase):
    def test_page_not_found(self):
        response = self.client.get('me')
        self.assertEquals(response.status_code, 404)

class UsuarioModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Usuario.objects.create(first_name="Pepperoni",  last_name = "Cheese" , email="Bestpizzaever@clearly.com", password = "abc123")

    def test_first_name_label(self):
        usuario = Usuario.objects.get(id=1)
        field_label = usuario._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')

    def test_first_name_max_length(self):
        usuario = Usuario.objects.get(id=1)
        max_length = usuario._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 30)

    def test_object_name_is_last_name_comma_first_name(self):
        usuario = Usuario.objects.get(id=1)
        expected_object_name = f'{usuario.first_name} {usuario.last_name}'
        self.assertEquals(expected_object_name, str(usuario))


