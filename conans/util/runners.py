from conan.internal.util.runners import check_output_runner as check_output_runner_new

def check_output_runner(cmd, stderr=None, ignore_error=False):
	check_output_runner_new(cmd, stderr=stderr, ignore_error=ignore_error)
