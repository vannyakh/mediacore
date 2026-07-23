"""MediaCore local development entrypoint."""


def main() -> None:
    from apps.api.main import run

    run()


if __name__ == "__main__":
    main()
