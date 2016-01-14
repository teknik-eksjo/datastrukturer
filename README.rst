Övningar: Datastrukturer och algoritmer
=======================================

Detta repository innehåller övningar som behandlar datastrukturer och
algoritmer.


Övningarna
----------
Övningarna finns i moduler i paketet exercises.
Förväntad funktion finns i de docstrings som hör ihop med funktionerna.

För att köra linter och enhetstester kan du använda följande kommandon.

.. code-block::

  python manage.py lint
  python manage.py test

För vissa övningar förväntas du själv skriva enhetstester. Detta görs med
fördel i testfiler med beskrivande namn. (De måste ha formen :code:`test_*.py`.)

.. code-block::

  python manage.py test --coverage

Kör testerna med code coverage-analys. Används med fördel för att få en
uppfattning om vilken kod du har kvar att skriva tester till. En HTML-rapport
skapas på sökvägen :code:`./tmp/coverage/index.html`.

Innan du börjar
---------------
Skapa den virtuella körmiljön med de paket som behövs.

.. code-block::

  pyvenv venv

Aktivera den virtella körmiljön:

.. code-block::

  . venv/bin/activate

Om du använder Windows:

.. code-block::

  venv/Script/activate.bat

Installera de paket som behövs för uppgiften:

.. code-block::

  pip install -r requirements.txt
