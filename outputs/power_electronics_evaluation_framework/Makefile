PYTHON ?= python
PYTHONPATH := src:.

.PHONY: install test example clean

install:
	$(PYTHON) -m pip install -e . --no-build-isolation

test:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m unittest discover -s tests

example:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) agents/example_agent.py benchmarks/power_flow_benchmark/tasks/example_radial_bus.json results/example_agent_output.json
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m evaluation_harness.cli run-power-flow benchmarks/power_flow_benchmark/tasks/example_radial_bus.json results/example_agent_output.json --report results/example_report.json

clean:
	$(PYTHON) -c "import pathlib, shutil; [shutil.rmtree(p) for p in pathlib.Path('.').rglob('__pycache__') if p.is_dir()]"
	$(PYTHON) -c "import pathlib; [p.unlink() for p in pathlib.Path('.').rglob('*.pyc')]"
