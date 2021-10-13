.. ref-communityproviders:

Community Providers
===================

Here's a list of Providers written by the community:

+---------------+--------------------------+----------------------------------+
| Provider name | Description              | URL                              |
+===============+==========================+==================================+
| Airtravel     | Airport names, airport   | `randum_airtravel`_               |
|               | codes, and flights.      |                                  |
+---------------+--------------------------+----------------------------------+
| Credit Score  | Fake credit score data   | `randum_credit_score`_            |
|               | for testing purposes     |                                  |
+---------------+--------------------------+----------------------------------+
| Microservice  | Fake microservice names  | `randum_microservice`_            |
+---------------+--------------------------+----------------------------------+
| Music         | Music genres, subgenres, | `randum_music`_                   |
|               | and instruments.         |                                  |
+---------------+--------------------------+----------------------------------+
| Posts         | Fake posts in markdown   | `mdgen`_                         |
|               | format                   |                                  |
+---------------+--------------------------+----------------------------------+
| Vehicle       | Fake vehicle information | `randum_vehicle`_                 |
|               | includes Year Make Model |                                  |
+---------------+--------------------------+----------------------------------+
| WebProvider   | Web-related data such as | `randum_web`_                     +
|               | mime-type and web server |                                  +
|               | versions.                |                                  +
+---------------+--------------------------+----------------------------------+
| Wi-Fi ESSID   | Fake Wi-Fi ESSIDs.       | `randum_wifi_essid`_              +
+---------------+--------------------------+----------------------------------+
| Optional      | Wrap over other          | `randum_optional`_                |
|               | providers to return      |                                  |
|               | their value or `None`.   |                                  |
+---------------+--------------------------+----------------------------------+

If you want to add your own provider to this list, please submit a Pull Request to our `repo`_.

In order to be inlcuded, your provider must satisfy these requirement:

* it must have tests.
* it must be published on PyPI.
* it must have an `OSI-Approved`_ License.
* it must not duplicate any functionality already present in ``Randum``.
* it must not contain any profanity, either in code or in documentation.
* it must not contain any malicious nor any kind of telemetry code.

.. _repo: https://github.com/joke2k/randum/
.. _OSI-Approved: https://opensource.org/licenses/alphabetical
.. _randum_airtravel: https://pypi.org/project/randum_airtravel/
.. _randum_credit_score: https://pypi.org/project/randum-credit-score/
.. _randum_microservice: https://pypi.org/project/randum-microservice/
.. _randum_music: https://pypi.org/project/randum_music/
.. _mdgen: https://pypi.org/project/mdgen/
.. _randum_vehicle: https://pypi.org/project/randum-vehicle/
.. _randum_web: https://pypi.org/project/randum_web/
.. _randum_wifi_essid: https://pypi.org/project/randum-wifi-essid/
.. _randum_optional: https://pypi.org/project/randum-optional
