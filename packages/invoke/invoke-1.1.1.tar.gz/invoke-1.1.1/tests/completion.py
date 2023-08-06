import sys

from invoke import Program

import pytest

from _util import expect, trap


pytestmark = pytest.mark.usefixtures("integration")


@trap
def _complete(invocation, collection=None):
    colstr = ""
    if collection:
        colstr = "-c {}".format(collection)
    command = "inv --complete {0} -- inv {0} {1}".format(colstr, invocation)
    Program().run(command, exit=False)
    return sys.stdout.getvalue()


class ShellCompletion:
    """
    Shell tab-completion behavior
    """

    def no_input_means_just_task_names(self):
        expect("-c simple_ns_list --complete", out="z-toplevel\na.b.subtask\n")

    def no_input_with_no_tasks_yields_empty_response(self):
        expect("-c empty --complete", out="")

    def task_name_completion_includes_aliases(self):
        for name in ("z\n", "toplevel"):
            assert name in _complete("", "alias_sorting")

    def top_level_with_dash_means_core_options(self):
        output = _complete("-")
        # No point mirroring all core options, just spot check a few
        for flag in ("--no-dedupe", "-d", "--debug", "-V", "--version"):
            assert "{}\n".format(flag) in output

    def bare_double_dash_shows_only_long_core_options(self):
        output = _complete("--")
        assert "--no-dedupe" in output
        assert "-V" not in output

    def task_names_only_complete_other_task_names(self):
        # Because only tokens starting with a dash should result in options.
        assert "print-name" in _complete("print-foo", "integration")

    def task_name_completion_includes_tasks_already_seen(self):
        # Because it's valid to call the same task >1 time.
        assert "print-foo" in _complete("print-foo", "integration")

    def per_task_flags_complete_with_single_dashes(self):
        for flag in ("--name", "-n"):
            assert flag in _complete("print-name -", "integration")

    def per_task_flags_complete_with_double_dashes(self):
        output = _complete("print-name --", "integration")
        assert "--name" in output
        assert "-n\n" not in output  # newline because -n is in --name

    def flag_completion_includes_inverse_booleans(self):
        output = _complete("basic-bool -", "foo")
        assert "--no-mybool" in output

    def tasks_with_positional_args_complete_with_flags(self):
        # Because otherwise completing them is invalid anyways.
        # NOTE: this currently duplicates another test because this test cares
        # about a specific detail.
        output = _complete("print-name --", "integration")
        assert "--name" in output

    def core_flags_taking_values_have_no_completion_output(self):
        # So the shell's default completion is available.
        assert _complete("-f") == ""

    def per_task_flags_taking_values_have_no_completion_output(self):
        assert _complete("basic-arg --arg", "foo") == ""

    def core_bool_flags_have_task_name_completion(self):
        assert "mytask" in _complete("--echo", "foo")

    def per_task_bool_flags_have_task_name_completion(self):
        assert "mytask" in _complete("basic-bool --mybool", "foo")

    def core_partial_or_invalid_flags_print_all_flags(self):
        for flag in ("--echo", "--complete"):
            for given in ("--e", "--nope"):
                assert flag in _complete(given)

    def per_task_partial_or_invalid_flags_print_all_flags(self):
        for flag in ("--arg1", "--otherarg"):
            for given in ("--ar", "--nope"):
                completion = _complete("multiple-args {}".format(given), "foo")
                assert flag in completion
