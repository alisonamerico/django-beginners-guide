import pytest
from model_bakery import baker


@pytest.fixture
def usuario_logado(db, django_user_model):
    usuario_modelo = baker.make(django_user_model, username='morfeu', email='morfeu@email.com')
    return usuario_modelo


def client_com_usuario_logado(usuario_logado, client):
    client.force_login(usuario_logado)
    return client
