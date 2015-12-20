
def split_lines(output_result_file, html_script,test_file_path):
    with open(html_script, 'r') as template:
        template_str = template.read().rstrip()

    with open(test_file_path,'r') as results_file:
        for line in results_file:
            splitted = line.split(",", 1)
            path = splitted[0].strip()
            result_lst = splitted[1].strip()

            with open(output_result_file, 'a') as results_first:
                results_first.write("<html><body><table border=1>"  + "\n")
            with open(output_result_file, 'a') as results_html:
                replaced_line = template_str.replace("split[0]", path).replace( "split[1]", str(result_lst))
                results_html.write(replaced_line + "\n")
            with open(output_result_file, 'a') as results_last:
                results_last.write("</table></body></html>")



def main():

    html_script='/home/dev/Yolodemotest/html.txt'
    test_file_path='/home/dev/Yolodemotest/test.csv'
    output_result_file='/home/dev/Yolodemotest/results.html'
    split_lines(output_result_file, html_script, test_file_path)



if __name__ == '__main__':
    main()
