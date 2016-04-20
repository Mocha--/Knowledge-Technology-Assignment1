For task 1, I have implemented 2 approximate matching methods which are local alignment and global alignment.

Make sure the file of film titles is called 'film_titles.txt'.
Make sure the reviews are stored in the folder which is called 'revs'.
If the reviews is not extracted, please run command 'tar -zxvf xibow1-revs.tgz'.

For local alignment approximate matching method, nothing extra needs installing.
Just run the command 'python filmtitle-local.py'.

For global alignment approximate matching method, package 'editdistance' is a pre-condition for launching the program.
To install package 'editdistance', please make sure 'pip' is already installed in your computer. If so, things are easy.
You only need to run command 'pip install editdistance' in your terminal.
To run the program, type command 'python filmtitle-global.py'.

Both of the two programs output results into two files located in the same folder whose name are 'result-global.txt' and 'result-local.txt' respectively.
If there is a best match, the output format will be like 'review file name : film title'. For example, '1000.txt : spider man'.
If there is no match the output will just be 'No matched film title.'.
