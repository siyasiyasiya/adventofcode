def main():
    #part 1
    file_path = "input.txt"
    dial = 50
    password = 0
    try: 
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if line.startswith('R'):
                    dial += int(line[1:])

                    while dial > 99:
                        dial -= 100

                        #part 2
                        if dial != 0:
                            password += 1

                else:
                    #part 2
                    if dial == 0:
                        password -= 1
                    dial -= int(line[1:])

                    while dial < 0:
                        dial += 100

                        #part 2
                        password += 1
                if dial == 0:
                    password += 1
            
            print(password)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()