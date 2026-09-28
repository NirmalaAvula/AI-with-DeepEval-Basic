
import os
import pandas as pd


def save_report(results):

    df = pd.DataFrame(results)

    # Create reports folder if it doesn't exist
    os.makedirs("reports", exist_ok=True)

    output_file = "reports/Hallucination_Report.xlsx"

    df.to_excel(output_file, index=False)

    print("\nReport Generated Successfully")
    print(f"Saved at: {output_file}")

