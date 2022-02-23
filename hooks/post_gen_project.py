import os
from pathlib import Path

ALLOWED_BUILD_SYSTEMS = ["flit", "poetry"]
"""A list of all allowed build systems by the template."""


def remove_tool_files(tool_name, basedir):
    """Removes files matching given glob expression within desired base
    directory.

    Parameters
    ----------
    tool_name: str
        Name of the tool used as build system.
    basedir: Path
        Base directory path.
    """

    for filepath in basedir.glob(f"**/*_{tool_name}*"):
        filepath.unlink()


def rename_tool_files(tool_name, basedir):
    """Rename tool filenames within desired base directory.

    Parameters
    ----------
    tool_name: str
        Name of the tool used as build system.
    basedir: Path
        Base directory path.
    """

    for original_filepath in basedir.glob(f"**/*_{tool_name}*"):
        new_filename = original_filepath.name.replace(f"_{tool_name}", "")
        original_filepath.rename(Path(original_filepath.parent, new_filename))


def main():
    """Entry point of the script."""

    # Get baked project location path
    project_path = Path(os.getcwd())

    # Get the desired build system
    build_system = "{{ cookiecutter.build_system }}"

    # Remove non-desired build system files
    for tool in ALLOWED_BUILD_SYSTEMS:
        if tool != build_system:
            remove_tool_files(tool, project_path)

    # Rename any files including tool name suffix
    rename_tool_files(build_system, project_path)


if __name__ == "__main__":
    main()
