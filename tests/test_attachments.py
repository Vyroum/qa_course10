import allure
import json
from allure import attachment_type



def test_attachments():
    allure.attach("Text content", name="Content from text", attachment_type=attachment_type.TEXT)
    allure.attach("<h1>Hello, world</h1>", name="Content from text", attachment_type=attachment_type.HTML)
    allure.attach(json.dumps({"first": 1, "second": 2}), attachment_type=attachment_type.JSON)