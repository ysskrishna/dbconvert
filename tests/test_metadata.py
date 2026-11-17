import os
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

import dbconvert.core.metadata as metadata


class LoadMetadataTests(unittest.TestCase):
    def setUp(self):
        self.original_cwd = Path.cwd()
        metadata._metadata_cache = None

    def tearDown(self):
        os.chdir(self.original_cwd)
        metadata._metadata_cache = None

    def test_source_tree_ignores_the_current_directory(self):
        with TemporaryDirectory() as temporary:
            os.chdir(temporary)
            loaded = metadata.load_pyproject_metadata()

        self.assertEqual(loaded["version"], "1.2.0")
        self.assertEqual(loaded["name"], "dbconvert")
        self.assertEqual(loaded["repository"], "https://github.com/ysskrishna/dbconvert.git")
        self.assertEqual(loaded["internalurls"]["author_name"], "Y. Siva Sai Krishna")

    def test_installed_copy_reads_version_from_package_metadata(self):
        class FakeMetadata(dict):
            def get_all(self, key):
                if key == "Project-URL":
                    return ["Repository, https://github.com/ysskrishna/dbconvert.git"]
                return None

        with TemporaryDirectory() as temporary:
            os.chdir(temporary)
            with patch.object(Path, "is_file", return_value=False), patch.object(
                metadata, "package_version", return_value="9.9.9"
            ), patch.object(
                metadata, "package_metadata", return_value=FakeMetadata({"Name": "dbconvert"})
            ):
                loaded = metadata.load_pyproject_metadata()

        self.assertEqual(loaded["version"], "9.9.9")
        self.assertEqual(loaded["name"], "dbconvert")
        self.assertEqual(loaded["repository"], "https://github.com/ysskrishna/dbconvert.git")
        self.assertEqual(loaded["internalurls"]["author_linkedin"], "https://linkedin.com/in/ysskrishna")


if __name__ == "__main__":
    unittest.main()
