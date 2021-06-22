from django.urls.base import reverse
import pytest
from pytest_django.asserts import assertContains
from django.urls import reverse


@pytest.fixture
def resp_home(client, db):
    resp = client.get(reverse('home'))
    return resp


def test_status_code(resp_home):
    assert resp_home.status_code == 200


def test_titulo(resp_home):
    assertContains(resp_home, '<title>Django Boards</title>')


def test_home_link(resp_home):
    assertContains(resp_home, f'href="{reverse("home")}">Django Boards</a>')


def test_botao_login_disponivel(resp_home):
    assertContains(resp_home, 'Log in')


def test_botao_signup_disponivel(resp_home):
    assertContains(resp_home, 'Sign up')
