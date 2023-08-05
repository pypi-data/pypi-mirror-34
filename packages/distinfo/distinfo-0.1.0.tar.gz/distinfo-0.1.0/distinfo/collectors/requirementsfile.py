from pathlib import Path

from .collector import Collector


class RequirementsFile(Collector):

    TEST_REQUIREMENTS = (
        "requirements-test.txt",
        "requirements-tests.txt",
        "test-requirements.txt",
        "requirements/test.txt",
        "requirements/tests.txt",
    )

    def _collect(self):
        for req in self.TEST_REQUIREMENTS:
            if Path(req).exists():
                self.add_requirements_file(req)
