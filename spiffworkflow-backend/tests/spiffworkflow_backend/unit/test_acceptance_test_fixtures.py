"""Test_acceptance_test_fixtures."""
from flask.app import Flask
import os
from spiffworkflow_backend.models.process_group import ProcessGroup

from spiffworkflow_backend.services.acceptance_test_fixtures import (
    load_acceptance_test_fixtures,
)
from spiffworkflow_backend.services.process_model_service import ProcessModelService


def test_start_dates_are_one_hour_apart(app: Flask) -> None:
    """Test_start_dates_are_one_hour_apart."""
    process_model_identifier = 'misc/acceptance-tests-group-one/acceptance-tests-model-1'
    group_identifier = os.path.dirname(process_model_identifier)
    parent_group_identifier = os.path.dirname(group_identifier)
    if not ProcessModelService.is_group(parent_group_identifier):
        process_group = ProcessGroup(id=parent_group_identifier, display_name=parent_group_identifier)
        ProcessModelService.add_process_group(process_group)
    if not ProcessModelService.is_group(group_identifier):
        process_group = ProcessGroup(id=group_identifier, display_name=group_identifier)
        ProcessModelService.add_process_group(process_group)
    process_instances = load_acceptance_test_fixtures()

    assert len(process_instances) > 2
    assert process_instances[0].start_in_seconds is not None
    assert process_instances[1].start_in_seconds is not None
    assert (process_instances[0].start_in_seconds - 3600) == (
        process_instances[1].start_in_seconds
    )
