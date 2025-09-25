.PHONY: demo plan run-dry clean setup

# Setup directories
setup:
	mkdir -p out/plans logs

# Run full demo pipeline (rule-based)
demo: setup
	python src/normalize.py
	python src/plan_stub.py
	python src/tm_adapter.py out/plans/10038554138.json

# Run demo with Amazon Q
demo-q: setup
	python src/normalize.py
	python src/plan_stub.py --use-q
	python src/tm_adapter.py out/plans/10038554138.json

# Generate plans only (rule-based)
plan: setup
	python src/normalize.py
	python src/plan_stub.py

# Generate plans with Amazon Q
plan-q: setup
	python src/normalize.py
	python src/plan_stub.py --use-q

# Run dry-run for specific work order
run-dry: setup
	@if [ -z "$(WO)" ]; then echo "Usage: make run-dry WO=10038554138"; exit 1; fi
	python src/tm_adapter.py out/plans/$(WO).json

# Run live for specific work order (use with caution)
run-live: setup
	@if [ -z "$(WO)" ]; then echo "Usage: make run-live WO=10038554138"; exit 1; fi
	python src/tm_adapter.py out/plans/$(WO).json --live

# Clean generated files
clean:
	rm -rf out/ logs/*.log