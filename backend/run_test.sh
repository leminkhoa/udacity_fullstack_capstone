#!/bin/bash
bash setup_db.sh budget_db_test
pytest . --disable-pytest-warnings
