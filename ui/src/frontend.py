import requests


from pages.allOrder import AllOrders

from services.sidebar import SideBarOptionMenuService

from requests import Session
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

retry_strategy = Retry(
    total=10,
    status_forcelist=[404, 429, 500, 502, 503, 504],
    method_whitelist=["POST", "HEAD", "GET", "PUT", "DELETE", "OPTIONS", "TRACE"],
    backoff_factor=5
)
adapter = HTTPAdapter(max_retries=retry_strategy)
session = Session()
session.mount("https://", adapter)

optionMenuService = SideBarOptionMenuService()

# Add Option Page here
optionMenuService.add(AllOrders(session))

#########################################################

optionMenuService.show()