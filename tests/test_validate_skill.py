import subprocess
import sys
import textwrap
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory


REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = REPO_ROOT / "scripts" / "validate_skill.py"


def write_valid_skill(path: Path) -> None:
    (path / "agents").mkdir()
    (path / "SKILL.md").write_text(
        textwrap.dedent(
            """\
            ---
            name: image2video
            description: Use when turning reference images into video briefs or local clips.
            ---

            # Image to Video
            """
        ),
        encoding="utf-8",
    )
    (path / "agents" / "openai.yaml").write_text(
        textwrap.dedent(
            """\
            interface:
              display_name: "Image to Video"
              short_description: "Turn images into video plans"
              default_prompt: "Use $image2video to plan a short image-to-video clip."
            """
        ),
        encoding="utf-8",
    )


def run_validator(path: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


class ValidateSkillTests(unittest.TestCase):
    def test_valid_skill_passes_without_external_yaml_dependency(self) -> None:
        with TemporaryDirectory() as raw_tmp:
            tmp_path = Path(raw_tmp)
            write_valid_skill(tmp_path)

            result = run_validator(tmp_path)

        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("OK: skill validation passed", result.stdout)

    def test_missing_agent_field_fails_with_clear_message(self) -> None:
        with TemporaryDirectory() as raw_tmp:
            tmp_path = Path(raw_tmp)
            write_valid_skill(tmp_path)
            (tmp_path / "agents" / "openai.yaml").write_text(
                textwrap.dedent(
                    """\
                    interface:
                      display_name: "Image to Video"
                      short_description: "Turn images into video plans"
                    """
                ),
                encoding="utf-8",
            )

            result = run_validator(tmp_path)

        self.assertEqual(result.returncode, 1)
        self.assertIn("agents/openai.yaml missing interface.default_prompt", result.stdout)


if __name__ == "__main__":
    unittest.main()
