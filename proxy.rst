
``proxy.conf.json``


.. code-block:: json

    {
        "/api": {
            "target": "http://localhost:8000",
            "secure": false
        },
        "/static": {
            "target": "http://localhost:8000",
            "secure": false
        }
    }


``package.json``


.. code-block:: json

    {
      "version": "0.0.0",
      ...
      "scripts": {
        "ng": "ng",
        "start": "ng serve --proxy-config proxy.conf.json",
        ...
      }
      ...
    }
