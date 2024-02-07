import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError

try:
    client = MailchimpMarketing.Client()
    client.set_config({
        "api_key": "YOUR_API_KEY",
        "server": "YOUR_SERVER_PREFIX"
    })
    response = client.ping.get()
    print(response)
except ApiClientError as error:
    print(error)