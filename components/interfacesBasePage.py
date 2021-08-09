import datetime
import csv

filename = 'data/BA02210713.TCL'

class POCInterface:
    @staticmethod
    def test_analisis():
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    print(f'\t{row[4]} Nombre de la cuenta')
                    line_count += 1
            print(f'Processed {line_count} lines.')

    @staticmethod
    def check_date(date):
        date_format = "%Y%m%d"

        try:
            datetime.datetime.strptime(date, date_format)
        except ValueError:
            print("Este no es el formato correcto de fecha. Deberia ser YYYYMMDD")

    @staticmethod
    def test_analisis2():
        output = open('xyz.txt', 'w')
        with open(filename, "rt", encoding='ascii') as f:
            line_count = 0
            date_format = "%Y%m%d"
            for line in f:
                row_count = 0
                output.write(line)
                line_count += 1

                string_list = line.split(",")
                assert len(string_list) ==23 or len(string_list)  == 3, "la celda deberia ser 23 o 3- SE OBTUVO: " + len(string_list)
                assert string_list[0] == "CL" or string_list[0] == "99", "LA PRIMERA CELDA DEBERIA SER CL O 99 - SE OBTUVO: " + cell
                assert datetime.datetime.strptime(string_list[1], date_format), "el formato de fecha deberia ser YYYYMMDD - SE OBTUVO: "+ string_list[1]
                assert len(string_list[1]) == 8, "el formato de fecha deberia ser YYYYMMDD - SE OBTUVO: "+ string_list[1]
                #VALIDACIONES DE LA ULTIMA FILA?
                #assert "BA02" in string_list[2] , "Deberia contener BA02 o el total de filas "+str(total_of_lines)+" - Se Obtuvo: "+ string_list[2]
                #assert total_of_lines in string_list[2] , "Deberia contener BA02 o el total de filas "+str(total_of_lines)+" - Se Obtuvo: "+ string_list[2]

                assert string_list[3] =="53", "la celda deberia ser 53- SE OBTUVO: " + string_list[3]
                assert len(string_list[5]) == 10, "el largo de la celda deberia ser 10  - SE OBTUVO: " + string_list[5]
                assert string_list[6] == "CLP", "Moneda siempre deberia ser CLP  - SE OBTUVO: " + string_list[6]
                assert datetime.datetime.strptime(string_list[7], date_format), "el formato de fecha deberia ser YYYYMMDD - SE OBTUVO: "+ string_list[7]
                assert string_list[8] == "+" or string_list[8] == "-", "EXISTEN DOS SIMBOLOS + Y - . SE OBTUVO: " + string_list[8]
                for cell in string_list:
                    #print(cell)

                    #assert cell == "CL" or cell == "99", "LA PRIMERA CELDA DEBERIA SER CL O 99 - SE OBTUVO: " + cell

                    row_count += 1
               # print(row)
               # print(row_count)
