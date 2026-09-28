from src.dataset_loader import load_all_sheets
from src.llm_client import generate_response
from src.evaluator import evaluate_response
from src.report_generator import save_report

# Load all sheets from Excel
all_sheets = load_all_sheets("data/Hallucination_Sample_Dataset.xlsx")

results = []

# Loop through each sheet
for sheet_name, dataset in all_sheets.items():

    print("\n" + "=" * 60)
    print(f"Processing Sheet: {sheet_name}")
    print("=" * 60)

    # Remove .head(5) later if you want all rows
    dataset = dataset.head(20)

    # Loop through each row in the sheet
    for index, row in dataset.iterrows():

        print(f"\nQuestion {index + 1}")

        input_text = row["Input"]
        ground_truth = row["Ground_Truth"]

        print("Generating Response...")
        llm_response = generate_response(input_text)

        print("Evaluating...")
        score, result, reason = evaluate_response(
            input_text,
            ground_truth,
            llm_response
        )

        # Save result
        results.append({
            "Sheet_Name": sheet_name,
            "ID": row["ID"],
            "Input": input_text,
            "Ground_Truth": ground_truth,
            "LLM_Response": llm_response,
            "Score": score,
            "Result": result,
            "Reason": reason
        })

# Save all results into one report
save_report(results)

print("\nAll sheets processed successfully!")