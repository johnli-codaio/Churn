import os

MAX_ITER = 25
#os.system("cp EmailEnron email_input.txt")
os.system("cp GNPn100p05  email_input.txt")
for i in range(MAX_ITER):
    os.system("python pagerank_map.py < email_input.txt | sort | python "
            "pagerank_reduce.py | python process_map.py | sort | python "
            "process_reduce.py > email_output.txt")
    os.system("python pagerank_map.py < email_output.txt | sort | python "
            "pagerank_reduce.py | python process_map.py | sort | python "
            "process_reduce.py > email_input.txt")

# os.system("python pagerank_map.py < email_output.txt | sort | python "
#         "pagerank_reduce.py | python process_map.py | sort | python "
#         "process_reduce.py > email_input.txt")
# os.system("python pagerank_map.py < email_input.txt | sort | python "
#         "pagerank_reduce.py | python process_map.py | sort | python "
#         "process_reduce.py > email_output.txt")
# os.system("python pagerank_map.py < email_output.txt | sort | python "
#         "pagerank_reduce.py | python process_map.py | sort | python "
#         "process_reduce.py > email_input.txt")
