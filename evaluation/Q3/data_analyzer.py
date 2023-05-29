import json

def read_json(file_path):
    with open(file_path, 'r') as f:
        res = json.load(f)
    return res
results_basepath = "results/"

# rules threshold
rules_threshold_souffle_path = results_basepath + "max_rules/souffle/"
rules_threshold_ddlog_path = results_basepath + "max_rules/ddlog/"
rules_config = [5, 10, 20, 40, 60, 80, 100]
souffle_ratio = ""
souffle_ref_weight = ""
souffle_opt_weight = ""

ddlog_ratio = ""
ddlog_ref_weight = ""
ddlog_opt_weight = ""

for conf in rules_config:
    souffle_result = read_json(rules_threshold_souffle_path + str(conf) + "/statis.json")
    souffle_ratio += "(%s, %s) " % (conf, souffle_result["average_execution_time_for_optimized_program"]/souffle_result["average_execution_time_for_reference_program"])
    souffle_ref_weight += "(%s, %s) " % (conf, souffle_result["total_time_for_reference_program"]/(souffle_result["total_time_for_reference_program"] + souffle_result["total_time_for_optimized_program"]))
    souffle_opt_weight += "(%s, %s) " % (conf, souffle_result["total_time_for_optimized_program"]/(souffle_result["total_time_for_reference_program"] + souffle_result["total_time_for_optimized_program"]))
    ddlog_result = read_json(rules_threshold_ddlog_path + str(conf) + "/statis.json")
    ddlog_ratio += "(%s, %s) " % (conf, ddlog_result["average_execution_time_for_optimized_program"]/ddlog_result["average_execution_time_for_reference_program"])
    ddlog_ref_weight += "(%s, %s) " % (conf, ddlog_result["total_time_for_reference_program"]/(ddlog_result["total_time_for_reference_program"] + ddlog_result["total_time_for_optimized_program"]))
    ddlog_opt_weight += "(%s, %s) " % (conf, ddlog_result["total_time_for_optimized_program"]/(ddlog_result["total_time_for_reference_program"] + ddlog_result["total_time_for_optimized_program"]))

print("The results for Max_rules: ")
print("execution time ratio for souffle: ")
print(souffle_ratio)
print("reference program execution time percentage for souffle: ")
print(souffle_ref_weight)
print("optimized program execution time percentage for souffle: ")
print(souffle_opt_weight)

print("execution time ratio for ddlog: ")
print(ddlog_ratio)
print("reference program execution time weight for ddlog: ")
print(ddlog_ref_weight)
print("optimized program execution time weight for ddlog: ")
print(ddlog_opt_weight)


print("")
print("")

# attemtps
attempts_path = results_basepath + "max_att/"

attempts_configs = [1, 10, 20, 30, 40, 50, 60, 70]
average_program_size_results = ""
total_test_case = ""

for conf in attempts_configs:
    result = read_json(attempts_path + str(conf) + "/statis.json")
    average_program_size_results += "(%s, %s)" % (conf, result["average_rule_number"])
    total_test_case += "(%s, %s)" % (conf, result["test_case_number"])

print("The results for Max_att: ")
print("number of rules in each test iteration: ")
print(average_program_size_results)
print("total test case number: ")
print(total_test_case)

print("")
print("")


# emtpy
empty_path = results_basepath + "p_empty/"
empty_configs = [0, 20, 40, 60, 80, 100]
opt_empty_prob = ""
final_empty_prob = ""
total_test_case = ""
for conf in empty_configs:
    result = read_json(empty_path + str(conf) + "/statis.json")
    opt_empty_prob += "(%s, %s) " % (conf, result["probability_of_optimized_program_with_enmpty_result"])
    final_empty_prob += "(%s, %s) " % (conf, result["probability_of_final_program_with_empty_result"])
    total_test_case += "(%s, %s)" % (conf, result["test_case_number"])
print("The results for P_empty: ")
print("probability of optimized program with empty results: ")
print(opt_empty_prob)
print("probability of final test case in each test iteration with empty results: ")
print(final_empty_prob)
print("total test iterations number: ")
print(total_test_case)

print()
print()


# probability of duplicate head
rq_path = results_basepath + "p_head/"
rq_configs = [0, 2, 4, 6, 8, 10]
average_circle_number = ""
average_circle_length = ""
for conf in rq_configs:
    result = read_json(rq_path + str(conf) + "/statis.json")
    average_circle_number += "(%s, %s) " % (conf, result["average_recursive_query_number"])
    average_circle_length += "(%s, %s) " % (conf, result["average_recursive_query_length"])

print("The results for P_head:")
print("average cycle number for each test case: ")
print(average_circle_number)
print("average cycle length for each circle: ")
print(average_circle_length)


print()
print()

# max iteration
iteration_path = results_basepath + "max_iter/"
iter_configs = [10, 50, 100, 200, 300]
average_circle_number = ""
average_circle_length = ""
for conf in iter_configs:
    result = read_json(iteration_path + str(conf) + "/statis.json")
    average_circle_number += "(%s, %s) " % (conf, result["average_recursive_query_number"])
    average_circle_length += "(%s, %s) " % (conf, result["average_recursive_query_length"])

print("The results for Max_iter: ")
print("average circle number for each test case: ")
print(average_circle_number)
print("average circle length for each circle: ")
print(average_circle_length)


print()
print()


# compare with random
random_path = results_basepath + "compare_with_random/"
souffle_random_path = random_path + "souffle/"
ddlog_random_path = random_path + "ddlog/"
random_configs = [20, 40, 60, 80]
souffle_inc_total = ""
souffle_inc_valid = ""
souffle_inc_nonempty = ""
souffle_ran_total = ""
souffle_ran_valid = ""
souffle_ran_nonempty = ""
ddlog_inc_total = ""
ddlog_inc_valid = ""
ddlog_inc_nonempty = ""
ddlog_ran_total = ""
ddlog_ran_valid = ""
ddlog_ran_nonempty = ""
for conf in random_configs:
    result = read_json(souffle_random_path + "normal_" + str(conf) + "/statis.json")
    souffle_inc_total += "(%s, %s) " % (conf, result["test_case_number"])
    souffle_inc_valid += "(%s, %s) " % (conf, result["total_final_program_normal"])
    souffle_inc_nonempty += "(%s, %s) " % (conf, result["number_of_optimized_prog_with_final_non_empty_result"])
    result = read_json(souffle_random_path + "random_" + str(conf) + "/statis.json")
    souffle_ran_total += "(%s, %s) " % (conf, result["test_case_number"])
    souffle_ran_valid += "(%s, %s) " % (conf, result["total_final_program_normal"])
    souffle_ran_nonempty += "(%s, %s) " % (conf, result["number_of_optimized_prog_with_final_non_empty_result"])

    result = read_json(ddlog_random_path + "normal_" + str(conf) + "/statis.json")
    ddlog_inc_total += "(%s, %s) " % (conf, result["test_case_number"])
    ddlog_inc_valid += "(%s, %s) " % (conf, result["total_final_program_normal"])
    ddlog_inc_nonempty += "(%s, %s) " % (conf, result["number_of_optimized_prog_with_final_non_empty_result"])
    result = read_json(ddlog_random_path + "random_" + str(conf) + "/statis.json")
    ddlog_ran_total += "(%s, %s) " % (conf, result["test_case_number"])
    ddlog_ran_valid += "(%s, %s) " % (conf, result["total_final_program_normal"])
    ddlog_ran_nonempty += "(%s, %s) " % (conf, result["number_of_optimized_prog_with_final_non_empty_result"])

print("The results for comparing with random test case generation: ")
print("souffle inc total: ")
print(souffle_inc_total)
print("souffle inc valid: ")
print(souffle_inc_valid)
print("souffle inc non-empty: ")
print(souffle_inc_nonempty)
print("souffle random total: ")
print(souffle_ran_total)
print("souffle random valid: ")
print(souffle_ran_valid)
print("souffle random non-empty: ")
print(souffle_ran_nonempty)

print("ddlog inc total: ")
print(ddlog_inc_total)
print("ddlog inc valid: ")
print(ddlog_inc_valid)
print("ddlog inc non-empty: ")
print(ddlog_inc_nonempty)
print("ddlog random total: ")
print(ddlog_ran_total)
print("ddlog random valid: ")
print(ddlog_ran_valid)
print("ddlog random non-empty: ")
print(ddlog_ran_nonempty)