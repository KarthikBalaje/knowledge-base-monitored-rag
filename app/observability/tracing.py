from __future__ import annotations

from functools import lru_cache

from opentelemetry import trace
from opentelemetry.sdk.resources import Resource

from phoenix.otel import TracerProvider
from phoenix.otel import SimpleSpanProcessor
from phoenix.otel import HTTPSpanExporter


PHOENIX_ENDPOINT = "http://127.0.0.1:6006/v1/traces"
PHOENIX_PROJECT = "knowledge-base-monitored-rag"


@lru_cache(maxsize=1)
def setup_tracing():
    resource = Resource.create(
        {
            "openinference.project.name": PHOENIX_PROJECT,
        }
    )

    provider = TracerProvider(
        resource=resource,
        verbose=False,
    )

    exporter = HTTPSpanExporter(
        endpoint=PHOENIX_ENDPOINT,
    )

    provider.add_span_processor(
        SimpleSpanProcessor(exporter)
    )

    trace.set_tracer_provider(provider)

    return provider


def get_tracer():
    provider = setup_tracing()
    return provider.get_tracer("knowledge-base-monitored-rag")