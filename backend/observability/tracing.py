import logging
import uuid

# A simple in-memory trace store
_traces = {}

def init_tracing():
    """
    Initialize tracing system (local mode).
    """
    logging.info("ℹ️ Tracing initialized (local mode, no JSON formatter).")

def start_trace(name: str):
    """
    Start a new trace with a unique ID.
    """
    trace_id = str(uuid.uuid4())
    _traces[trace_id] = {"name": name, "events": []}
    logging.info(f"▶️ Trace started: {name} ({trace_id})")
    return trace_id

def log_event(trace_id: str, message: str):
    """
    Log an event to a given trace.
    """
    if trace_id in _traces:
        _traces[trace_id]["events"].append(message)
    logging.info(f"📝 Trace {trace_id} event: {message}")

def end_trace(trace_id: str):
    """
    End a trace and flush events.
    """
    if trace_id in _traces:
        logging.info(f"⏹️ Trace ended: {_traces[trace_id]['name']} ({trace_id})")
        for event in _traces[trace_id]["events"]:
            logging.info(f"   └─ {event}")
        del _traces[trace_id]

