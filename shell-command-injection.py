import atheris
import os
import sys  # Required for Atheris to parse arguments

def vulnerable_shell(data):
    """
    Executes a shell command without printing each input.
    """
    try:
        # Vulnerable to shell injection
        command = f"echo {data} > /dev/null"  # Redirects output to /dev/null
        result = os.system(command)

        # Log potential issues when command fails
        if result != 0:
            print(f"Potential vulnerability detected with input: {data}")
    except Exception as e:
        print(f"Error encountered: {e} for {data}")

def test_shell_input(data):
    fdp = atheris.FuzzedDataProvider(data)
    fuzz_input = fdp.ConsumeUnicodeNoSurrogates(20).strip()
    if fuzz_input:  # Ensure input is non-empty
        vulnerable_shell(fuzz_input)

if __name__ == "__main__":
    atheris.Setup(sys.argv, test_shell_input)
    atheris.Fuzz()
