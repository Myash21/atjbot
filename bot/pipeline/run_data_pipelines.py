from get_links import GetLinks
from get_pending_cases import GetChipStats, GetPendingCases
from get_tables import GetTables
from get_whats_new import GetWhatsNew
import argparse


def main() -> None:
    arg_parse = argparse.ArgumentParser(
        prog="Run data pipeline.",
        description="Script to run the entire data pipeline. Use cli args to control what pipeline to run.",
    )
    arg_parse.add_argument("pipeline", type=str)
    arg_parse.add_argument("url", type=str)
    args = arg_parse.parse_args()

    pipeline_dict = {
        "links": GetLinks,
        "chips": GetChipStats,
        "njdg": GetPendingCases,
        "tables": GetTables,
        "whatsnew": GetWhatsNew,
    }

    pipeline_dict[args.pipeline](args.url).run_pipeline()


if __name__ == "__main__":
    main()
