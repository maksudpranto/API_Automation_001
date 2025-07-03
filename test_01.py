from playwright.sync_api import sync_playwright

def test_api_001():
    with sync_playwright() as p:
        request = p.request.new_context()
        response = request.get("https://reqres.in/api/users?page=2")
        assert response.status == 200

