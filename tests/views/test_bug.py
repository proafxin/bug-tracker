import pytest
from httpx import AsyncClient

from tests.views.common import detail_not_found


class TestStory:
    async def __test_bug(self, bug: dict):
        assert isinstance(bug, dict)
        assert "id" in bug
        assert isinstance(bug["id"], int)
        assert bug["id"] == 1
        assert "story" in bug

    @pytest.mark.asyncio
    async def test_create(self, client: AsyncClient) -> None:
        json = {"name": "Test Story"}
        await client.post("/stories/", json=json)
        json = {
            "title": "Test Bug",
            "description": "Description of Test Bug",
            "story_id": 1,
        }
        response = await client.post(url="/bugs/", json=json)
        assert response.status_code == 200
        bug = response.json()
        await self.__test_bug(bug=bug)

    @pytest.mark.asyncio
    async def test_get(self, client: AsyncClient) -> None:
        response = await client.get(url="/bugs/")
        assert response.status_code == 200

        bugs = response.json()
        assert isinstance(bugs, list)
        assert len(bugs) == 1
        await self.__test_bug(bug=bugs[0])

    @pytest.mark.asyncio
    async def test_get_by_id(self, client: AsyncClient) -> None:
        response = await client.get(url="/bugs/1")
        assert response.status_code == 200
        bug = response.json()
        await self.__test_bug(bug=bug)

    @pytest.mark.asyncio
    async def test_get_not_found(self, client: AsyncClient) -> None:
        response = await client.get(url="/bugs/2")
        assert response.status_code == 404
        error = response.json()
        detail_not_found(error=error)
