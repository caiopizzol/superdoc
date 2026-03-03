import asyncio
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


class _SyncRuntimeStub:
    def invoke(self, operation_id, params, **_kwargs):
        return {"operation_id": operation_id, "params": params}


async def _async_invoke(operation_id, params, **_kwargs):
    return {"operation_id": operation_id, "params": params}


class _AsyncRuntimeStub:
    invoke = staticmethod(_async_invoke)


def test_sync_doc_api_exposes_snake_case_and_camel_aliases():
    from superdoc.generated.client import _SyncDocApi

    doc = _SyncDocApi(_SyncRuntimeStub())

    assert hasattr(doc, "get_markdown")
    assert hasattr(doc, "getMarkdown")
    assert doc.get_markdown({})["operation_id"] == "doc.getMarkdown"
    assert doc.getMarkdown({})["operation_id"] == "doc.getMarkdown"

    assert hasattr(doc, "track_changes")
    assert hasattr(doc, "trackChanges")
    assert doc.track_changes.list({})["operation_id"] == "doc.trackChanges.list"
    assert doc.trackChanges.list({})["operation_id"] == "doc.trackChanges.list"


def test_async_doc_api_exposes_snake_case_and_camel_aliases():
    from superdoc.generated.client import _AsyncDocApi

    doc = _AsyncDocApi(_AsyncRuntimeStub())

    assert hasattr(doc, "get_markdown")
    assert hasattr(doc, "getMarkdown")
    assert asyncio.run(doc.get_markdown({}))["operation_id"] == "doc.getMarkdown"
    assert asyncio.run(doc.getMarkdown({}))["operation_id"] == "doc.getMarkdown"
