import time

# In-memory metrics
metrics = {
    "meal_plans_generated": 0,
    "avg_response_time": 0.0,
    "failed_requests": 0
}


def record_metrics(success: bool, duration: float):
    """
    Update metrics after each pipeline run.
    - success: True if pipeline completed without exception
    - duration: runtime in seconds
    """
    global metrics

    # Update counter only if successful
    if success:
        metrics["meal_plans_generated"] += 1

        # Recalculate running average of response time
        n = metrics["meal_plans_generated"]
        old_avg = metrics["avg_response_time"]
        metrics["avg_response_time"] = (old_avg * (n - 1) + duration) / n
    else:
        metrics["failed_requests"] += 1


def get_metrics():
    """
    Return current metrics as JSON-serializable dict.
    """
    return metrics
