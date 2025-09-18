import os
import logging
from langfuse import Langfuse

logger = logging.getLogger(__name__)



class DummyTrace:
    """Fallback trace if Langfuse is not configured."""

    def log_event(self, name, payload=None):
        logger.info(f"[DummyTrace] {name}: {payload}")

    def event(self, name, input=None, output=None):
        logger.info(f"[DummyTrace Event] {name}: input={input}, output={output}")

    def end(self):
        logger.info("[DummyTrace] Trace ended")


def start_trace(name: str):
    """
    Start a Langfuse trace if keys are present, otherwise return DummyTrace.
    """
    public_key = os.getenv("LANGFUSE_PUBLIC_KEY")
    secret_key = os.getenv("LANGFUSE_SECRET_KEY")
    host = os.getenv("LANGFUSE_HOST", "https://cloud.langfuse.com")

    if not public_key or not secret_key:
        logger.warning("⚠️ Langfuse keys not found. Using DummyTrace.")
        return DummyTrace()

    try:
        client = Langfuse(
            public_key=public_key,
            secret_key=secret_key,
            host=host,
        )
        trace = client.trace(name=name)

        # --- Shim: add log_event for backwards compatibility ---
        if not hasattr(trace, "log_event"):
            def log_event(event_name, payload=None):
                trace.event(name=event_name, input=payload or {})
            trace.log_event = log_event

        # --- Shim: add end() so pipeline doesn't crash ---
        if not hasattr(trace, "end"):
            def end():
                logger.info("[LangfuseTrace] end() called (no-op for StatefulTraceClient)")
            trace.end = end

        logger.info("✅ Tracing initialized with Langfuse")
        return trace

    except Exception as e:
        logger.error(f"❌ Failed to initialize Langfuse tracing: {e}")
        return DummyTrace()

