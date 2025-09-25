"""CLI entry for EverLight APM assistant - placeholder."""

import argparse


def main():
    parser = argparse.ArgumentParser(prog="everlight-apm-assistant")
    parser.add_argument('--run-example', action='store_true', help='Run sample session')
    args = parser.parse_args()
    if args.run_example:
        print('Running example (placeholder)')


if __name__ == '__main__':
    main()
