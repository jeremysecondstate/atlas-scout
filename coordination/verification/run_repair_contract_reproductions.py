"""Run synthetic PR43/PR44 defect reproductions against caller-chosen checkouts."""
from __future__ import annotations

import argparse
import importlib.util
from pathlib import Path
import sys


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, required=True,
                        help="Isolated checkout containing Atlas PR44 dispatcher")
    parser.add_argument("--repair-root", type=Path,
                        help="Isolated PR43 checkout; defaults to source root")
    parser.add_argument("--suite", choices=("repair", "restart", "all"), default="repair",
                        help="Historical defect reproductions to collect")
    args = parser.parse_args()
    source = args.source_root.resolve(strict=True)
    repair_root = (args.repair_root or source).resolve(strict=True)
    helper = repair_root / "ml" / "nightly_stage_repair.py"
    fixtures = repair_root / "tests" / "test_nightly_stage_repair.py"
    for required in (source / "ml" / "nightly_dispatch.py", helper, fixtures):
        if not required.is_file():
            parser.error(f"Required reviewed source missing: {required}")
    sys.dont_write_bytecode = True
    sys.path[:0] = [str(source), str(repair_root / "tests")]
    spec = importlib.util.spec_from_file_location("ml.nightly_stage_repair", helper)
    if spec is None or spec.loader is None:
        parser.error("Cannot load the reviewed repair module")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    import pytest
    fixture_root = Path(__file__).parent
    names = {"repair": "test_pr43_dispatch_integration.py",
             "restart": "test_restart_continuation_paths.py"}
    selected = names.values() if args.suite == "all" else [names[args.suite]]
    return pytest.main([*[str(fixture_root / name) for name in selected],
                        "-q", "-p", "no:cacheprovider", "--confcutdir", str(fixture_root)])


if __name__ == "__main__":
    raise SystemExit(main())
