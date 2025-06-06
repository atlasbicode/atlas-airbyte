#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#


import json
import os
import shutil
from pathlib import Path
from typing import Any, Mapping

from source_google_search_console.config_migrations import MigrateCustomReports
from source_google_search_console.source import SourceGoogleSearchConsole

from airbyte_cdk.models import OrchestratorType, Type
from airbyte_cdk.sources import Source


# BASE ARGS
CMD = "check"
TEST_CONFIG_PATH = "unit_tests/test_migrations/test_config.json"
BACKUP_CONFIG_PATH = str(Path(__file__).parent / "test_config.json.bak")
NEW_TEST_CONFIG_PATH = "unit_tests/test_migrations/test_new_config.json"
SOURCE_INPUT_ARGS = [CMD, "--config", TEST_CONFIG_PATH]


# HELPERS
def load_config(config_path: str = TEST_CONFIG_PATH) -> Mapping[str, Any]:
    with open(config_path, "r") as config:
        return json.load(config)


def backup_config():
    """Create a backup of the original test config file"""
    shutil.copyfile(TEST_CONFIG_PATH, BACKUP_CONFIG_PATH)


def restore_config():
    """Restore the original test config from backup"""
    if os.path.exists(BACKUP_CONFIG_PATH):
        shutil.copyfile(BACKUP_CONFIG_PATH, TEST_CONFIG_PATH)
        os.remove(BACKUP_CONFIG_PATH)


def test_migrate_config():
    # Create a backup of the original config
    backup_config()

    try:
        migration_instance = MigrateCustomReports()
        original_config = load_config()

        source: Source = SourceGoogleSearchConsole(catalog=None, config=original_config, state=None)

        # migrate the test_config
        migration_instance.migrate(SOURCE_INPUT_ARGS, source)
        # load the updated config
        test_migrated_config = load_config()
        # check migrated property
        assert "custom_reports_array" in test_migrated_config
        assert isinstance(test_migrated_config["custom_reports_array"], list)
        # check the old property is in place
        assert "custom_reports" in test_migrated_config
        assert isinstance(test_migrated_config["custom_reports"], str)
        # check the migration should be skipped, once already done
        assert not migration_instance.should_migrate(test_migrated_config)
        # load the old custom reports VS migrated
        assert json.loads(original_config["custom_reports"]) == test_migrated_config["custom_reports_array"]
        # test CONTROL MESSAGE was emitted
        control_msg = migration_instance.message_repository._message_queue[0]
        assert control_msg.type == Type.CONTROL
        assert control_msg.control.type == OrchestratorType.CONNECTOR_CONFIG
        # old custom_reports are stil type(str)
        assert isinstance(control_msg.control.connectorConfig.config["custom_reports"], str)
        # new custom_reports are type(list)
        assert isinstance(control_msg.control.connectorConfig.config["custom_reports_array"], list)
        # check the migrated values
        assert control_msg.control.connectorConfig.config["custom_reports_array"][0]["name"] == "custom_dimensions"
        assert control_msg.control.connectorConfig.config["custom_reports_array"][0]["dimensions"] == ["date", "country", "device"]
    finally:
        # Always restore the original config file
        restore_config()


def test_config_is_reverted():
    # check the test_config state, it has to be the same as before tests
    test_config = load_config()
    # check the config no longer has the migarted property
    assert "custom_reports_array" not in test_config
    # check the old property is still there
    assert "custom_reports" in test_config
    assert isinstance(test_config["custom_reports"], str)


def test_should_not_migrate_new_config():
    new_config = load_config(NEW_TEST_CONFIG_PATH)
    migration_instance = MigrateCustomReports()
    assert not migration_instance.should_migrate(new_config)
