#!/bin/bash

py.test --cov pyansys --cov-report html
xdg-open htmlcov/index.html
