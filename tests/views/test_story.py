import pytest
from httpx import AsyncClient

from tests.views.common import detail_not_found


class TestStory:
    async def __test_story(self, story: dict):
        assert isinstance(story, dict)
        assert "id" in story
        assert isinstance(story["id"], int)
        assert story["id"] == 1

    @pytest.mark.asyncio
    async def test_create(self, client: AsyncClient) -> None:
        json = {"name": "Test Story"}
        response = await client.post(url="/stories/", json=json)
        assert response.status_code == 200
        story = response.json()
        await self.__test_story(story=story)

    @pytest.mark.asyncio
    async def test_get(self, client: AsyncClient) -> None:
        response = await client.get(url="/stories/")
        assert response.status_code == 200

        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 1
        assert isinstance(data[0], dict)

    @pytest.mark.asyncio
    async def test_get_by_id(self, client: AsyncClient) -> None:
        response = await client.get(url="/stories/1")
        assert response.status_code == 200
        story = response.json()
        await self.__test_story(story=story)

    @pytest.mark.asyncio
    async def test_get_not_found(self, client: AsyncClient) -> None:
        response = await client.get(url="/stories/2")
        assert response.status_code == 404
        error = response.json()
        detail_not_found(error=error)
