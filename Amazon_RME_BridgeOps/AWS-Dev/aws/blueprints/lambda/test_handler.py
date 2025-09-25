import handler

def test_post_item(monkeypatch):
    class Table:
        def put_item(self, Item): self.last = Item
    handler.items_table = Table()
    event = {
        "resource": "/session/xyz/item",
        "httpMethod": "POST",
        "pathParameters": {"id": "xyz"},
        "body": '{"equipment_id":"Drive-1","component":"fiducial","action":"replaced","result":"restored"}'
    }
    resp = handler.lambda_handler(event, None)
    assert resp["statusCode"] == 200
    assert "item_id" in resp["body"]

def test_get_render(monkeypatch):
    class Table:
        def query(self, **kwargs): return {"Items": [
            {"equipment_id":"Drive-1","component":"fiducial","action":"replaced","result":"restored"}
        ]}
    handler.items_table = Table()
    event = {
        "resource": "/session/xyz/render",
        "httpMethod": "GET",
        "pathParameters": {"id": "xyz"}
    }
    resp = handler.lambda_handler(event, None)
    assert resp["statusCode"] == 200
    assert "fiducial" in resp["body"]