def read_employees(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.readlines()
        print(f"амжилттай уншлаа  {file_path}.")
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []

def write_employees(file_path, employees):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(employees)
    print(f"амжилттай шивэгдлээ {file_path}.")


def main():
    # текст файлаас ажилчдын өгөгдлийг унших
    employees = read_employees("C:\\Users\\User\\PycharmProjects\\buteelt2\\employees1.txt")




    # Дарханы сервер рүү бүх мэдээллийг шилжүүлэх
    write_employees("C:\\Users\\User\\PycharmProjects\\buteelt2\\darkhan_database1.txt", employees)

    # үндсэн серверээс бүх ажилтны мэдээллийг хасах
    write_employees("C:\\Users\\User\\PycharmProjects\\buteelt2\\employees1.txt", [])

    # Дарханы серверт хандаж амжилттай орсон эсэхийг шалга
    darkhan_employees = read_employees("C:\\Users\\User\\PycharmProjects\\buteelt2\\darkhan_database1.txt")



    non_retired = [emp for emp in darkhan_employees if "тэтгэвэрт гарсан" not in emp]
    if non_retired:
        # Step 6: тэтгэвэрт гараагүй ажилтнуудыг үндсэн серверт хуулах
        write_employees("C:\\Users\\User\\PycharmProjects\\buteelt2\\employees1.txt", non_retired)

        # Step 7: Хуулсан мэдээллээ дарханы серверээс хасах
        remaining = [emp for emp in darkhan_employees if emp not in non_retired]
        write_employees("C:\\Users\\User\\PycharmProjects\\buteelt2\\darkhan_database1.txt", remaining)




if __name__ == "__main__":
    main()