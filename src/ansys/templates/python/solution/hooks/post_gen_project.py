from ansys.templates.utils import keep_files


DESIRED_STRUCTURE = [
    ".github/workflows/ci_cd.yml",
    ".vscode/launch.json",
    "doc/source/_static/ansys-solutions-logo-black-background.png",
    "doc/source/_static/README.md",
    "doc/source/_templates/README.md",
    "doc/source/_templates/sidebar-nav-bs.html",
    "doc/source/conf.py",
    "doc/source/index.rst",
    "doc/styles/Vocab/ANSYS/accept.txt",
    "doc/styles/Vocab/ANSYS/reject.txt",
    "doc/styles/.gitignore",
    "doc/.vale.ini",
    "doc/make.bat",
    "doc/Makefile",
    "examples/README.md",
    "requirements/requirements_build.txt",
    "requirements/requirements_doc.txt",
    "requirements/requirements_style.txt",
    "requirements/requirements_tests.txt",
    f"src/ansys/solutions/{{ cookiecutter.__solution_name_slug }}/scripts/README.md",
    f"src/ansys/solutions/{{ cookiecutter.__solution_name_slug }}/solution/definition.py",
    f"src/ansys/solutions/{{ cookiecutter.__solution_name_slug }}/solution/first_step.py",
    f"src/ansys/solutions/{{ cookiecutter.__solution_name_slug }}/solution/other_step.py",
    f"src/ansys/solutions/{{ cookiecutter.__solution_name_slug }}/ui/assets/Graphics/ansys-solutions-horizontal-logo.png",
    f"src/ansys/solutions/{{ cookiecutter.__solution_name_slug }}/ui/assets/style.css",
    f"src/ansys/solutions/{{ cookiecutter.__solution_name_slug }}/ui/app.py",
    f"src/ansys/solutions/{{ cookiecutter.__solution_name_slug }}/ui/first_page.py",
    f"src/ansys/solutions/{{ cookiecutter.__solution_name_slug }}/ui/other_page.py",
    f"src/ansys/solutions/{{ cookiecutter.__solution_name_slug }}/ui/page.py",
    f"src/ansys/solutions/{{ cookiecutter.__solution_name_slug }}/__init__.py",
    f"src/ansys/solutions/{{ cookiecutter.__solution_name_slug }}/main.py",
    "tests/common_test_files/README.md",
    "tests/integration/test_integration_dummy.py",
    "tests/unit/test_unit_dummy.py",
    "tests/conftest.py",
    ".codespell.exclude",
    ".codespell.ignore",
    ".flake8",
    ".gitignore",
    ".pre-commit-config.yaml",
    "CHANGELOG.md",
    "CODE_OF_CONDUCT.md",
    "CODEOWNERS",
    "CONTRIBUTING.md",
    "LICENSE.rst",
    "pyproject.toml",
    "README.rst",
    "setup_environment.py",
    "tox.ini"
]
"""A list holding all desired files to be included in the project."""


def main():
    """Entry point of the script."""
    # Apply the desired structure to the project
    keep_files(DESIRED_STRUCTURE)

if __name__ == "__main__":
    main()
