# 13. SAVE OUTPUTS

cv_results_df.to_csv("cross_validation_results.csv", index=False)
test_results_df.to_csv("test_results.csv", index = False)

print("\nSaved Files:")
print("- cross_validation_results.csv")
print("- test_results.csv")