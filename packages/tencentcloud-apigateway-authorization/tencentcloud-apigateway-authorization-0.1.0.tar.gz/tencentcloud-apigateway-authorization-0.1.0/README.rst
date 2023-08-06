tencentcloud-apigateway-authorization
--------------------------------------

Generate headers with authorization for the request of TencentCloud Apigateway API.
为腾讯云Api网管服务的AP的请求I生成带有authorization认证信息的header

Install
-------

.. code-block:: shell
    
    pip install tencentcloud-apigateway-authorization

Use
----

.. code-block:: python

    import os

    from apigateway import Auth
    import requests
    
    secretId = os.environ['secretId']
    secretKey = os.environ['secretKey']
    auth = Auth(secretId, secretKey)
    headers = auth.generateHeaders()
    response = requests.get('https://service-{appid}.ap-shanghai.apigateway.myqcloud.com/release/api', headers=headers)
    print(response.json())

Author
-------

Yixian Du