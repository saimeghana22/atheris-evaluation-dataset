import atheris
import sys
from bs4 import BeautifulSoup

def vulnerable_html_parser(data):
    try:
        # BeautifulSoup parses the input HTML
        soup = BeautifulSoup(data, "html.parser")
        
        # We can check for an expected output (parsed content, or error detection)
        if soup:
            pass  # Do nothing on valid parsing, or add assertions as needed

    except Exception as e:
        # Catch unexpected exceptions
        if isinstance(e, AssertionError):
            print(f"Unexpected AssertionError with input: {data}")
        elif isinstance(e, ValueError):
            print(f"Unexpected ValueError with input: {data}")
        elif isinstance(e, TypeError):
            print(f"Unexpected TypeError with input: {data}")
        else:
            print(f"Unexpected exception with input: {data}: {e}")

def test_html_input(data):
    fdp = atheris.FuzzedDataProvider(data)
    # Consume fuzzed input up to 100 characters
    fuzz_input = fdp.ConsumeUnicodeNoSurrogates(100)
    # Pass fuzzed data to BeautifulSoup parser
    vulnerable_html_parser(fuzz_input)

if __name__ == "__main__":
    atheris.Setup(sys.argv, test_html_input)
    atheris.Fuzz()
