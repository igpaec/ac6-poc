"""Package marker for the AC6 workshop lab repository.

This file is REQUIRED and must not be deleted.

Nautobot loads Jobs from a Git repository by walking the repository with
`pkgutil.walk_packages()` (see `nautobot/core/utils/module_loading.py`,
`import_modules_privately`). `walk_packages` only descends into a directory
that is an importable package -- i.e. one containing an `__init__.py`.

Without this file, Nautobot never imports `ac6_poc.jobs`, `registry["jobs"]`
stays empty, and the repository sync finishes SUCCESS while logging:

    No jobs were registered on loading the `ac6_poc.jobs` submodule.
    Did you miss a `register_jobs()` call? ...

which is misleading -- `register_jobs()` is fine; the package was never
imported at all.

Documented upstream in `nautobot/docs/user-guide/platform-functionality/
gitrepository.md`: "the top-level directory of Git repositories that provide
jobs must now contain an `__init__.py` file." (behaviour since Nautobot 2.0)

Verified against Nautobot 3.2.3.
"""
