contas_orama
======================================

|build-status-image| |pypi-version|

Descrição
-------------

Sistema de controles de finanças pessoais.
Usuário pode criar uma conta e fazer lançamentos na mesma.

Usuário poderá ver o extrato e consultar o saldo em períodos e
datas arbitrárias.

Requerimentos
--------------

-  Python
-  Django
-  Django REST Framework

Instalação
------------

Instalação usa ``pip``\ …

.. code:: bash

    $ pip install contas_orama

Utilização
----------

1. Em settings.py adicione "contas_orama" e "rest_framework" em INSTALLED_APPS:

.. code:: bash

    INSTALLED_APPS = [
      ...
      'rest_framework',
      'contas_orama',
    ]

  Ainda em settings.py adicione o seguinte bloco de comando:

.. code:: bash

    REST_FRAMEWORK = {
      'DEFAULT_PAGINATION_CLASS':
      'rest_framework.pagination.PageNumberPagination',
      'PAGE_SIZE': 20
    }

  O código acima se refere a [paginação](http://www.django-rest-framework.org/api-guide/pagination/#pagination).

  Dessa forma, em views onde ocorrem listagens de objetos, só serão listados
  20 contas e/ou 20 lançamentos.

  Mudar o parâmetro 'PAGE_SIZE' se desejar um número diferente.


2. Inclua a URL no urls.py do seu projeto.

.. code:: bash

    url('^contas_orama/', include('contas_orama.urls')),

3. Crie os modelos ...

.. code:: bash

      $ python manage.py migrate

4. Crie novos usuários (não é permitido acessar as contas sem login) ...

... code:: bash

      $ python manage.py createsuperusers

5. Visitar http://127.0.0.1:8000/contas/ para gerir as contas.


Testando
--------

Para executar os testes:

.. code:: bash

    $ python manage.py test contas_orama
