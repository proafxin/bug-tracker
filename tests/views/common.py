def detail_not_found(error: dict):
    assert isinstance(error, dict)
    assert "detail" in error
    assert isinstance(error["detail"], str)
