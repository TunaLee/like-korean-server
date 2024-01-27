# Python
from urllib.parse import urljoin

# Django
from django.conf import settings

# Local
from template.bases.modules.gateways import Gateway as BaseGateway


class Gateway(BaseGateway):
    def __init__(self):
        super().__init__(base_url=urljoin(settings.PAYMENT_API_URL, "/"))

    def add_payment(self, Authorization: str, paymentPrepareId: str, impUid: str):
        path = 'api/payments'

        body = {
            "paymentPrepareId": paymentPrepareId,
            "impUid": impUid
        }

        headers = {
            'Authorization': Authorization,
        }

        print('body : ', body)
        print('headers : ', headers)

        return self.request(method="POST", path=path, headers=headers, json=body)


gateway = Gateway()
