import json
import os
import logging
import sys
import traceback

from dm.cloudtrailsdk.client.tracker import Tracker
from dm.cloudtrailsdk.model.event import Event, ExceptionEvent, DependencyEvent

logger = logging.getLogger(__name__)


def configure_tracker(app_name="", app_version="", tracker_environment=None):
    region = os.environ.get("AWS_REGION")
    tracker_environment = os.environ.get("TRACKER_ENVIRONMENT",
                                         "eCloudTrailsStreamQA") if tracker_environment is None else tracker_environment
    tracker = Tracker(
        tracker_environment,
        region=region,
        app_name=app_name,
        app_version=app_version
    )
    return tracker


def send_custom_logger(app_name="", app_version="", tracker_environment=None, **properties):
    try:
        tracker = configure_tracker(app_name=app_name, app_version=app_version,
                                    tracker_environment=tracker_environment)
        custom_event = Event()
        custom_event.Properties.update(properties)
        tracker.track_event(custom_event)
    except Exception as e:
        logger.error(e.message)


def send_exception_logger(app_name="", app_version="", tracker_environment=None, **properties):
    try:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        tracker = configure_tracker(app_name=app_name, app_version=app_version,
                                    tracker_environment=tracker_environment)
        exception_event = ExceptionEvent(exc_value.__str__(), exc_type.__name__, traceback.format_exc(), **properties)
        tracker.track_exception(exception_event)
    except Exception as e:
        logger.error(e.message)


def send_dependency_logger(dependency_name, dependency_duration):
    try:
        tracker = configure_tracker()
        dependency_event = DependencyEvent(dependency_name, dependency_duration)
        tracker.track_dependency(dependency_event)
    except Exception as e:
        logger.error(e.message)
