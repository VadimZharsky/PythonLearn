import tasks

def main():
    # print(tasks.task_01_do_twice("py"))

    # assert tasks.task_01_do_twice("text") == "texttext"
    # assert tasks.task_01_do_twice("python") == "pythonpython"

    # result = tasks.task_02_count_calls()
    result = [tasks.task_02_count_calls() for _ in [1, 2, 3, 4]]
    print(result)


if __name__ == "__main__":
    main()